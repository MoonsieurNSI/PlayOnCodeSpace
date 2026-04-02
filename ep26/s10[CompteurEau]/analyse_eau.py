donnees = [
    {"jour": "2025-02-04", "heure": "00:00", "chaude": 2, "froide": 3},
    {"jour": "2025-02-04", "heure": "01:00", "chaude": 1, "froide": 2},
    {"jour": "2025-02-04", "heure": "02:00", "chaude": 0, "froide": 0},
    {"jour": "2025-02-04", "heure": "03:00", "chaude": 0, "froide": 0},
    {"jour": "2025-02-04", "heure": "04:00", "chaude": 0, "froide": 1},
    {"jour": "2025-02-04", "heure": "05:00", "chaude": 0, "froide": 0},
    {"jour": "2025-02-04", "heure": "06:00", "chaude": 4, "froide": 6},
    {"jour": "2025-02-04", "heure": "07:00", "chaude": 6, "froide": 8},
    {"jour": "2025-02-05", "heure": "00:00", "chaude": 0, "froide": 0},
    {"jour": "2025-02-05", "heure": "01:00", "chaude": 1, "froide": 1},
    {"jour": "2025-02-05", "heure": "02:00", "chaude": 1, "froide": 1},
    {"jour": "2025-02-05", "heure": "03:00", "chaude": 1, "froide": 1},
    {"jour": "2025-02-05", "heure": "04:00", "chaude": 0, "froide": 0},
    {"jour": "2025-02-05", "heure": "05:00", "chaude": 0, "froide": 0},
]


# -----------------------------
# Fonctions à compléter
# -----------------------------

def total_conso(donnees, jour):
    """
    renvoie la consommation totale d'eau (somme de l'eau chaude et de l'eau froide)
    de toutes les mesures pour ce jour.
    """
    total, existe = 0, False
    for dico in donnees:
        if dico['jour'] == jour:
            existe = True
            total += dico['chaude'] + dico['froide']     
    return total if existe else None

# test
# q1
assert total_conso(donnees, "2025-02-04") == 33
assert total_conso(donnees, "2025-12-25") is None
print("bvo, les tests q1 sont passés")


def fuite_possible(donnees, jour):
    """
    renvoie True si une fuite est possible ce jour-là,
    False sinon.
    Une fuite est possible si un mếme jour entre 00:00 et 05:00,
    une consommation est détéctée pendant 3 heures consécutives
    """
    compteur = 0
    for dico in donnees:
        if dico['jour'] == jour and "00:00" <= dico['heure'] <= "05:00":
            if dico['chaude'] + dico['froide'] > 0:
                compteur += 1
            else:
                compteur = 0
            if compteur >= 3:
                return True
    return False

#test
# q2
print(fuite_possible(donnees, "2025-02-04"))
print(fuite_possible(donnees, "2025-02-05"))

# -----------------------------
# Fonction fournie (erronée)
# -----------------------------

def lissage_conso(valeurs):
    """
    Calcule une moyenne glissante sur les valeurs.
    Pour chaque valeur, on calcule la moyenne avec ses voisins.
    """
    if len(valeurs) == 1:
        return valeurs[0]
    lisse = []
    for i in range(len(valeurs)):
        if i == 0:
            m = (valeurs[i] + valeurs[i+1]) / 2
        elif i == len(valeurs) - 1:
            m = (valeurs[i-1] + valeurs[i]) / 2
        else:
            m = (valeurs[i-1] + valeurs[i] + valeurs[i+1]) / 3
        lisse.append(m)
    
    return lisse


# -----------------------------
# Espace pour les tests
# -----------------------------

def test_lissage():
    # À compléter : produire au moins 3 tests révélant les erreurs
    print(lissage_conso([10, 20, 30, 40, 50]))

#test
# q3
test_lissage()
###output
# [15.0, 30.0, 45.0, 60.0, 45.0]
# on divise toujours par 2

# q4
# si la liste ne contient qu'une seule valeur, on la retourne