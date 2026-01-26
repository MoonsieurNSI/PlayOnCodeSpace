# Correction DST - Réseaux, Routage et Graphes
## Partie A : Réseau et adressage

### Question 1
Réponse : `137.254.128.200`

Justification :

- Le sous-réseau Commerces a l'adresse 137.254.128.0/24
- Il y a déjà 207 machines connectées (sans compter le routeur)
- Les machines sont numérotées dans l'ordre croissant à partir de la plus petite IP disponible.
- La première IP disponible est généralement 137.254.128.1 (la .0 étant l'adresse réseau).
- Si le routeur/passerelle prend la première adresse (.1), les machines occupent de .2 à .208.
- Si les machines commencent à .1, elles occupent de .1 à .207

Dans les deux cas, l'adresse 137.254.128.200 fait partie des adresses déjà attribuées.
L'adresse 137.254.128.210 serait au-delà des 207 machines déjà connectées.

### Question 2
Réponse : Non, ce n'est pas possible.
Justification :

- Avec un masque /24 (255.255.255.0), on dispose de 8 bits pour la partie hôte:
- Nombre d'adresses total : $2^8 = 256$ adresses
- Adresses utilisables : $256 - 2 = 254$ (on retire l'adresse réseau .0 et l'adresse de broadcast .255)
- Machines déjà connectées : 207 + 1 routeur = 208 adresses utilisées
- Adresses disponibles : 254 - 208 = 46 adresses

On ne peut donc ajouter que 46 machines, ce qui est insuffisant pour les 132 machines souhaitées

-----------------
## Partie B : Programmation d'un protocole de routage
### Question 3
Donner la liste des routeurs par lesquels transite un message envoyé depuis une machine du sous-réseau Navigation à destination d'une machine du sous-réseau Commerces.
Réponse : R1 → R3 → R6 → R7

Justification :
- Le sous-réseau Navigation est connecté à R1
- Le sous-réseau Commerces est connecté à R7

En consultant la table de routage :

R1 veut atteindre R7 : passerelle = R3 <br>
R3 veut atteindre R7 : passerelle = R6 <br>
R6 veut atteindre R7 : passerelle = R7 <br>


Donc le chemin est : `R1 → R3 → R6 → R7`

Note : la question pourrait aussi faire référence à R1→R3→R4→R7 selon le schéma du réseau mais cela ne correspondrait à la passerelle de R3 pour R7.

### Question 4

Réponse : Il y a une boucle de routage infinie.
Justification :
En consultant la table de routage :

R7 veut atteindre R1 : passerelle = R4
R4 veut atteindre R1 : passerelle = R6
R6 veut atteindre R1 : passerelle = R4

Les paquets vont donc circuler indéfiniment entre R4 et R6 sans jamais atteindre R1. C'est une boucle de routage. Le *TTL (Time To live)* permet par exemple d'éviter ce genre de problèmes.

### Question 5
```python
g = {
    'R1': ['R2', 'R3'],
    'R2': ['R1', 'R3', 'R5'],
    'R3': ['R1', 'R2'],
    'R5': ['R2']
}
```
### Question 6

Une fonction récursive est une fonction qui s'appelle elle-même dans sa propre définition. Elle doit comporter :

Un ou plusieurs cas de base (ou cas d'arrêt) : situations où la fonction retourne directement un résultat sans rappel récursif
Un ou plusieurs cas récursifs : situations où la fonction s'appelle elle-même avec des paramètres modifiés, se rapprochant progressivement du cas de base

### Question 7

```python
def plus_court_chemin(graphe, r_depart, r_arrivee):
    chemins = liste_chemins(graphe, r_depart, r_arrivee)
    
    # Initialisation avec le premier chemin
    chemin_minimal = chemins[0]
    longueur_min = len(chemins[0])
    
    # Parcours de tous les chemins pour trouver le plus court
    for chemin in chemins:
        if len(chemin) < longueur_min:
            longueur_min = len(chemin)
            chemin_minimal = chemin
    
    return chemin_minimal
```


### Question 8

```python
def plus_court_chemin_largeur(graphe, r_depart, r_arrivee):
    dict_chemins = {}
    L = [r_depart]
    sommets_marques = [r_depart]
    dict_chemins[r_depart] = [r_depart]
    
    for r in L:
        for s_r in graphe[r]:
            if not s_r in sommets_marques:
                sommets_marques.append(s_r)  # Ligne à compléter
                dict_chemins[s_r] = dict_chemins[r] + [s_r]
                if s_r == r_arrivee:
                    return dict_chemins[s_r]  # Ligne à compléter
                L.append(s_r)
```

On marque le sommet `s_r` comme visité en l'ajoutant à `sommets_marques`
Si on atteint le routeur d'arrivée, on retourne le chemin stocké dans `dict_chemins[s_r]`. <br>
On peut éventuellement retourner le dictionnaire entier. 

### Question 9

```python
def table_routage(graphe, routeur):
    table = {}
    
    # Pour chaque routeur destination dans le graphe
    for destination in graphe:
        if destination != routeur:  # On ne route pas vers soi-même
            # Trouver le plus court chemin
            chemin = plus_court_chemin_largeur(graphe, routeur, destination)
            # La passerelle est le premier routeur après le routeur source
            passerelle = chemin[1]
            table[destination] = passerelle
    
    return table
```

---------------

## Partie C : Utilisation du protocole OSPF

### Question 10

Formule : $coût = \frac{10^9}{débit}$ (débit en bits par seconde)

- Ethernet (E) : $débit = 10 Mbps = 10 × 10^6$ bps

$=> Coût = \frac{10^9}{(10 × 10^6)} = 100$


- Fast Ethernet (FE) : $débit = 100 Mbps = 100 × 10^6$ bps

$=>Coût = \frac{10^9}{(100 × 10^6) }= 10$


- Fibre (F) : $débit = 500 Mbps = 500 × 10^6$ bps

$=>Coût = \frac{10^9}{(500 × 10^6)} = 2$

### Question 11

|||R1|R2|R3|R4|R5|R6|R7|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|R1|=>|$0_{R1}$|$10_{R1}$|$2_{R1}$|$\infty_{R1}$|$\infty_{R1}$|$\infty_{R1}$|$\infty_{R1}$|
|R3|=>|#|$4_{R3}$|#|$102_{R3}$|$\infty_{R1}$|$102_{R3}$|$\infty_{R1}$|
|R2|=>|#|#|#|$102_{R3}$|$14_{R2}$|$102_{R3}$|$\infty_{R1}$|
|R5|=>|#|#|#|$102_{R3}$|#|$16_{R5}$|$\infty_{R1}$|
|R6|=>|#|#|#|$18_{R6}$|#|#|$26_{R6}$|
|R4|=>|#|#|#|#|#|#|$20_{R4}$|

Le tableau précédent est obtenu grâce à l'algorithme glouton de Dijsktra. Le chemin de coût minimal (coût: 20) est R1→R3→R2→R5→R6→R4→R7.


### Question 12
Dijsktra donne:
|||R1|R2|R3|R4|R5|R6|R7|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|R2|=>|$10_{R2}$|$0_{R2}$|$2_{R2}$|$\infty_{R2}$|$10_{R2}$|$\infty_{R2}$|$\infty_{R2}$|
|R3|=>|$4_{R3}$|#|#|$102_{R3}$|$10_{R2}$|$102_{R3}$|$\infty_{R2}$|
|R1|=>|#|#|#|$102_{R3}$|$10_{R2}$|$102_{R3}$|$\infty_{R2}$|
|R5|=>|#|#|#|$102_{R3}$|#|$12_{R5}$|$\infty_{R2}$|
|R6|=>|#|#|#|$14_{R6}$|#|#|$22_{R6}$|
|R4|=>|#|#|#|#|#|#|$16_{R4}$|
--------------

### Table de Routage de R2
|Destination|Suivant|Métrique|
|:---:|:---:|:---|
|R1|R3|$4_{R3}$:  R2 → R3 → R1|
|R2|||
|R3|R3|$2_{R2}$:  R2 → R3|
|R4|R5|$14_{R6}$: R2 → R5 → R6 → R4|
|R5|R5|$10_{R2}$: R2 → R5|
|R6|R5|$12_{R5}$: R2 → R5 → R6|
|R7|R5|$16_{R4}$: R2 → R5 → R6 → R4→ R7|
