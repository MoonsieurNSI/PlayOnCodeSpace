import donnees
import donnees_completes
from math import sqrt

def salaire_moyen_condition(employes, champ, valeur):
    '''Renvoie le salaire moyen des employes ayant val comme valeur associée
    au champ donné en argument.
    Si le nombre d'employés considéré est nul, cette fonction renvoie None'''
    # à implémenter
    assert type(employes) == list and all(type(elt) == dict for elt in employes)
    total = 0
    cpt = 0
    for employe in employes:
        if employe[champ] == valeur:
            total += employe["salaire"]
            cpt += 1
    return None if cpt == 0 else total / cpt

def test_salaire_moyen_condition():
    e = donnees.employes
    assert salaire_moyen_condition([], 'sexe', 'F') == None
    assert salaire_moyen_condition(e, 'sexe', 'F') == 2400.0
    assert salaire_moyen_condition(e, 'etudes', 3) == 2550.0
    assert salaire_moyen_condition(e, 'etudes', 12) == None
    # ajout
    return "bvo, les tests sont passés"

def effectif_par_sexe(employes):
    '''Renvoie un dictionnaire ayant deux clés 'F' et 'M'
    associée respectivement au nombre d'employées femmes et au
    nombre d'employés hommes dans les données en arguments.'''
    # à implémenter
    dico = { "F" : 0, "M": 0}
    for employe in employes:
        if employe["sexe"] == "F":
            dico["F"] += 1
        elif employe["sexe"] == "M":  # on ne sait pas après tout !
            dico["M"] += 1
    return dico

def test_effectif_par_sexe():
    e = donnees.employes
    assert effectif_par_sexe(e) == { 'F' : 3, 'M' : 3 }
    return "bvo, le test est passé"

def calcul_ecart_sexe(employes):
    '''Renvoie l'écart de salaire en pourcentage pour les femmes 
    par rapport aux hommes'''
    if not all([val > 0 for val in effectif_par_sexe(employes).values()]):
        return None
    moy_h = salaire_moyen_condition(employes, 'sexe', 'M')
    # on modifie le parametre 'employes' en employe
    moy_f = salaire_moyen_condition(employes, 'sexe', 'F')
    # on ajoute une valeur absolue et le ratio
    return abs(moy_h - moy_f) / moy_h * 100

# Attribution d'un premier salaire après embauche par les k plus proches voisins

def sexe_vers_entier(e):
    if e['sexe'] == 'F':
        return 1
    else:
        return -1

def distance(e1, e2):
    '''Renvoie la mesure de distance entre deux personnes.'''
    s = 0
    s = s + (sexe_vers_entier(e1) - sexe_vers_entier(e2))**2
    s = s + (e1['experience'] - e2['experience'])**2
    s = s + (e1['etudes'] - e2['etudes'])**2
    return sqrt(s)

def k_plus_proches(k, employes, e):
    '''Renvoie les k employes les plus proches de e par la 
    distance définie au dessus.'''
    e_d = [(distance(e, employes[i]), i) for i in range(len(employes))]
    e_d.sort() # va trier en premier sur la distance
    voisins = []
    for i in range(k):
        voisins.append(employes[e_d[i][1]])
    return voisins

def salaire_moyen(employes):
    '''Renvoie le salaire moyen pour une liste d'employes'''
    if len(employes) == 0:
        return None
    s = sum(e['salaire'] for e in employes)
    return s/len(employes)

def salaire_par_proximite(employes, e):
    '''Prend en entrée une liste d'employés et un dictionnaire comportant
    les champs experience, etudes et sexe et renvoie le salaire le plus
    proche en moyennant les 3 plus proches voisins'''
    voisins = k_plus_proches(3, employes, e)
    return salaire_moyen(voisins)


#q1
print(test_salaire_moyen_condition())
e = donnees_completes.employes
print(f'le salaire moyen des femmes est environ {salaire_moyen_condition(e, "sexe", "F"):.2f} €.')
print(f'le salaire moyen des hommes est environ {salaire_moyen_condition(e, "sexe", "M"):.2f} €.')

#q2
print(test_effectif_par_sexe())

#q3
print(f"l'écart de salaire moyen est environ {calcul_ecart_sexe(e):.2f}%.")

#q4
femme = {'experience': 3, 'etudes': 3, 'sexe': 'F'}
homme = {'experience': 3, 'etudes': 3, 'sexe': 'M'}
print(salaire_par_proximite(e, homme))
print(salaire_par_proximite(e, femme))
# le calcul de la distance prend en compte le sexe donc les écarts à l'embauche
# sont déterminés par les écarts actuels
