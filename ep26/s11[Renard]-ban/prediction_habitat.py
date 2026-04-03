from math import sqrt
from donnees_habitats import zones_connues

nouveau0 = {'vegetation': 5, 'proximite_eau': 2, 'densite_urbaine': 4, 'disponibilite_proies': 6, 'presence_renard': 0}
nouveau1 = {'vegetation': 5, 'proximite_eau': 2, 'densite_urbaine': 4, 'disponibilite_proies': 6, 'presence_renard': 1}

def distance(habitat_1, habitat_2):
    '''
    Calcule la distance euclidienne entre deux habitats.
    entrée : 
        - habitat_1 : dictionnaire représentant un habitat.
        - habitat_2 : dictionnaire représentant un autre habitat.
    sortie : 
        - float : distance euclidienne entre habitat_1 et habitat_2.
    '''
    d = 0
    for caracteristique in habitat_1:
        d += (habitat_1[caracteristique] - habitat_2[caracteristique])**2
    return sqrt(d)

#test
# q1
h1 = {'vegetation': 9, 'proximite_eau': 6, 'densite_urbaine': 0,'disponibilite_proies': 4, 'presence_renard': 1}
h2 = {'vegetation': 10, 'proximite_eau': 5, 'densite_urbaine': 9, 'disponibilite_proies': 10, 'presence_renard': 0}
print(distance(h1, h2))



def distance_d_un_habitat(habitat, habitats):
    '''
    Calcule la distance entre un habitat et chaque habitat de la liste.
    entrée : 
        - habitat : dictionnaire représentant un habitat.
        - habitats : liste de dictionnaires représentant des habitats.
    sortie : 
        - list[tuple] : liste de tuples (distance, habitat) où distance est la distance entre habitat et chaque habitat de la liste.
    '''
    reponse = []
    for h in habitats:
        reponse.append((distance(h, habitat), habitat))
    return reponse
#test
# q2 ,q3
zones_connues = [
{'vegetation': 9, 'proximite_eau': 6, 'densite_urbaine': 0, 'disponibilite_proies': 4, 'presence_renard': 1},
{'vegetation': 10, 'proximite_eau': 5, 'densite_urbaine': 9, 'disponibilite_proies': 10, 'presence_renard': 0},
{'vegetation': 8, 'proximite_eau': 5, 'densite_urbaine': 1, 'disponibilite_proies': 6, 'presence_renard': 0},
]
##### ALERTE ERREUR
##### nouveau ne contient pas la cle 'presence_renard'
##### on crée nouveau0 et nouveau1 selon que le renard est présent ou pas
print(distance_d_un_habitat(nouveau0, zones_connues))
print(distance_d_un_habitat(nouveau1, zones_connues))

def k_plus_proches(k, habitat, habitats):
    '''
    Calcule les k habitats les plus proches de l'habitat donné.
    entrée : 
        - k : entier représentant le nombre d'habitats à retourner.
        - habitat : dictionnaire représentant un habitat.
        - habitats : liste de dictionnaires représentant des habitats.
    sortie : 
        - list[tuple] : liste de tuples (distance, habitat) l'élément à l'indice 0 est la distance euclidienne entre habitat 
                        et chaque habitat de la liste et l'élément à l'indice 1 est le dictionnaire correspondant à l'habitat correspondant.
    '''
    # On calcule les distances
    distances = distance_d_un_habitat(habitat, habitats)
    # On cherche à trier les distances en fonction de la distance euclidienne.
    distances.sort(key = lambda x: x[0])
    return distances[:k] # renvoie les distances jusque la borne k non comprise

def presence_renard(k, habitat, habitats):
    '''
    Vérifie si l'habitat donné a plus de k/2 voisins avec des renards.
    entrée : 
        - k : entier représentant le nombre d'habitats à considérer.
        - habitat : dictionnaire représentant un habitat.
        - habitats : liste de dictionnaires représentant des habitats.
    sortie : 
        - bool : True si l'habitat a plus de k/2 voisins avec des renards, False sinon.
    '''
    habitats = k_plus_proches(k, habitat, habitats)
    n_renards = 0
    for habitat in habitats:
        #distance = habitat[0]
        caracteristiques = habitat[1]
        if caracteristiques['presence_renard'] == 1:
            n_renards += 1
    return n_renards >= k/2