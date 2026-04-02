#############################################################################
# Jeux de données fournis                                                   #
#############################################################################
from plantes import plantes, Plante
from mesures import mesures

#############################################################################
# Écrire le code de la fonction croissance_moyenne de la question 1         #
#############################################################################
# q1
# on a modifié l'import (lig 4) de façon à tester une précondition
def croissance_moyenne(plantes):
    """
    renvoie la moyenne des durées de croissance de l’ensemble de
    ces plantes (en jours)
    """
    assert type(plantes) == list
    assert all([type(elt) is Plante for elt in plantes])
    n = len(plantes)
    if n == 0:
        return None
    total = 0
    for plante in plantes:
        total += plante.croissance
    return total / n

assert croissance_moyenne([]) == None
assert croissance_moyenne(plantes) == 79.0
print("bvo, les tests de q1 sont passés")
#############################################################################
# Écrire le code de la fonction dictionnaire_mesure de la question 2      #
#############################################################################
# q2
def dictionnaire_mesure(plantes, mesures):
    """
    retourne un dictionnaire
     - cle : nom d'une plantes
     - valeur : liste de dictionnaire de mesures pour le nom de la plante
    """
    assert type(plantes) == list and type(mesures) == list
    assert all([type(elt) is Plante for elt in plantes])
    assert all([type(elt) is dict for elt in mesures])
    dico = {plante.nom:[] for plante in plantes}
    for mesure in mesures:
        dico[mesure['plante']].append(mesure)
    return dico


mesures_test01 = [
    {'jour': 1, 'plante': 'Basilic', 'hauteur': 0.85, 'temperature': 29.3, 'humidite': 50.89} ,
    {'jour': 1, 'plante': 'Tomate', 'hauteur': 1.27, 'temperature': 21.51, 'humidite': 47.19} ,
    {'jour': 1, 'plante': 'Menthe', 'hauteur': 0.67, 'temperature': 27.75, 'humidite': 61.14} ,
    {'jour': 1, 'plante': 'Tournesol', 'hauteur': 2.29, 'temperature': 18.42, 'humidite': 49.3},
    {'jour': 29, 'plante': 'Menthe', 'hauteur': 23.42, 'temperature': 22.19, 'humidite': 69.26}]

resultat01 = {'Basilic': [{'jour': 1, 'plante': 'Basilic', 'hauteur': 0.85, 'temperature': 29.3, 'humidite': 50.89}],
            'Tomate': [{'jour': 1, 'plante': 'Tomate', 'hauteur': 1.27, 'temperature': 21.51, 'humidite': 47.19}],
            'Menthe': [{'jour': 1, 'plante': 'Menthe', 'hauteur': 0.67, 'temperature': 27.75, 'humidite': 61.14}, 
                       {'jour': 29, 'plante': 'Menthe', 'hauteur': 23.42, 'temperature': 22.19, 'humidite': 69.26}],
            'Tournesol': [{'jour': 1, 'plante': 'Tournesol', 'hauteur': 2.29, 'temperature': 18.42, 'humidite': 49.3}],
            'Fougère': []}
mesures_test02 = []
resultat02 = {'Basilic': [], 'Tomate': [], 'Menthe': [], 'Tournesol': [], 'Fougère': []}

assert dictionnaire_mesure(plantes, mesures_test01) == resultat01
assert dictionnaire_mesure(plantes, mesures_test02) == resultat02
print("bvo, les tests de q2 sont passés")
#############################################################################
# Fonction défaillante à analyser et corriger pour les questions 3 et 4     #
#############################################################################

def purger_mesures_extremes(liste_mesures):
    """
    Supprime de la liste toutes les mesures dont la température 
    n'est pas comprise entre 20 et 25°C inclus.
    """
    
    # for mesure in liste_mesures:
    #     if mesure['temperature'] < 20 or mesure['temperature'] > 25:
    #         liste_mesures.remove(mesure)
    # return liste_mesures
    return [mesure for mesure in liste_mesures if 20 <= mesure['temperature'] <= 25]

def test_purger():
    mesures_test = [
         {'jour': 1, 'plante': 'Basilic', 'temperature': 18.0},
         {'jour': 2, 'plante': 'Basilic', 'temperature': 19.0},
         {'jour': 3, 'plante': 'Basilic', 'temperature': 22.0},
         {'jour': 4, 'plante': 'Basilic', 'temperature': 28.0},
         {'jour': 5, 'plante': 'Basilic', 'temperature': 29.0}
    ]
    

    mesures_test = purger_mesures_extremes(mesures_test)

    print("Résultat après la purge :")
    for m in mesures_test:
        print(f"Jour {m['jour']} : {m['temperature']}°C")
    print("bvo, les tests q3 sont passés")

#q3
test_purger()
# La méthode remove (qui n'est pas au programme) entraine un décalage des élémens en cours de boucle
# D'une manière générale, on se méfie de la suppression des éléments d'une liste en boucle
# On utilise une compréhension de liste ou une copie de la liste initiale (ce qui revient au même)

#q4
# voir le code