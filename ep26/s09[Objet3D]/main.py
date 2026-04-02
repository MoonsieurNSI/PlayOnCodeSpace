from Objet3D import Objet3D

#############################################################################
# Variables et fonctions fournies pour la question 3                        #
#############################################################################
parametres_imprimante = {'remplissage': 20,
                         'vitesse_extrusion': 8}  # 8mm3 / seconde


def volume_cube(cube):
    a, b = cube.sommets_adjacents()
    taille_cote = a.distance(b)  # distance donnee en mm
    return taille_cote ** 3

#############################################################################
# Écrire le code de la fonction estimation_impression de la question 3      #
#############################################################################
def estimation_impression(volume_reel, parametres):
    """
    renvoie le temps total d'impression sous la forme d'un
    flottant, exprimé en seconde
    """
    assert type(volume_reel) == int
    assert type(parametres) == dict and parametres["vitesse_extrusion"] > 0
    volume_impression = volume_reel * parametres["remplissage"] / 100
    return volume_impression / parametres["vitesse_extrusion"]

#############################################################################
# Programme à modifier de la question 4 et 5                                #
#############################################################################
objet = Objet3D()
objet.ajouter_sommet(0, 0, 0)
objet.ajouter_sommet(0, 2, 0)
objet.ajouter_sommet(2, 2, 0)
objet.ajouter_sommet(2, 0, 0)
objet.ajouter_sommet(1, 1, 2)
objet.ajouter_face([1, 2, 3, 4])
objet.ajouter_face([1, 2, 5])
objet.ajouter_face([1, 4, 5])
objet.ajouter_face([3, 4, 5])
objet.ajouter_face([2, 3, 5])
objet.afficher()
o = objet.transformer(2)
o.afficher()