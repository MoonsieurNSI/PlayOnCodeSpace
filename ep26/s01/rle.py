from PIL import Image


def codage_rle(liste_octets):
    '''Renvoie une liste d'octets obtenue par compression RLE'''
    liste_rle = []
    i = 0
    while i < len(liste_octets):
        c = liste_octets[i]
        k = 1
        while i+k < len(liste_octets) and liste_octets[i+k] == c:
            k += 1
        print(k)
        liste_rle.append(k)
        liste_rle.append(c)
        i += k
    return liste_rle

def decodage_rle(liste_rle):
    '''Renvoie la liste d'octets obtenue à partir de la liste liste_rle obtenue
    par compression RLE'''
    # A VOUS D'ÉCRIRE LE CODE LA FONCTION
    reponse = []
    for i in range(0, len(liste_rle), 2):
        reponse += [liste_rle[i + 1]] * liste_rle[i]
    return reponse

def test_codage():
    assert codage_rle([255, 255, 0, 255, 255, 255]) == [2, 255, 1, 0, 3, 255]
    assert decodage_rle([2, 255, 1, 0, 3, 255]) == [255, 255, 0, 255, 255, 255]
    #######ajout##########
    assert decodage_rle([4, 85]) == [85, 85, 85, 85]
    assert decodage_rle([1, 9, 1, 250, 1, 128]) == [9, 250, 128]
    assert decodage_rle([1, 0]) == [0]
    print("bvo")

def enregistrer_octets(nom_fichier, liste_octets):
    '''Enregistre une liste de valeurs numériques entre 0 et 255 dans un
    le fichier nom_fichier. Si une valeur est plus grande que 255 on considère
    que c'est 255. De même pour les valeur plus petite que 0.'''
    # Le fichier est ouvert en mode binaire pour pouvoir écrire sans restriction toute valeur
    # entre 0 et 255
    with open(nom_fichier, 'wb') as fichier:
        # Pour convertir une liste de valeur entre 0 et 255 en une liste d'octets qui peuvent
        # être écrits dans le fichier, on utilise `bytes`
        fichier.write(bytes([max(0, min(255, b)) for b in liste_octets]))


def charger_octets(nom_fichier):
    '''Renvoie la liste des octets présents dans le fichier nom_fichier'''
    with open(nom_fichier, 'rb') as fichier:
        liste_octets = list(fichier.read())
        return liste_octets


def enregistrer_image(nom_image, largeur, liste_niveaux):
    '''Enregistre un fichier image nom_image de la largeur donnée et dont les 
    valeurs de niveaux de gris des pixels sont celles de la liste
    liste_niveaux'''
    hauteur = len(liste_niveaux) // largeur
    im = Image.frombytes('L', (largeur, hauteur), bytes(liste_niveaux))
    im.save(nom_image)


def charger_image(nom_image):
    '''Étant donné une image nom_image, renvoie un couple (largeur, liste_niveaux) où 
    largeur est la largeur de l'image et liste_niveaux est la liste des valeurs de niveaux 
    de gris de l'image ligne par ligne'''

    image = Image.open(nom_image).convert('L')
    return (image.width, list(image.tobytes()))

#############################################################################
# Fonction nécessaire pour les tests de la question 3                       #
#############################################################################


def encoder_decoder_image(nom_image):
    '''Fonction de test permettant d'encoder puis décoder une image avec un
    codage RLE. Le fichier rle est nommé nom_image.rle et le fichier decodé
    est nom_image.dec.png'''
    w, l = charger_image(nom_image)
    print(w)
    enregistrer_octets(nom_image+'.rle', codage_rleV2(l))
    l = charger_octets(nom_image+'.rle')
    enregistrer_image(nom_image+'.dec.png', w, decodage_rle(l))
#############################
def codage_rleV2(liste_octets):
    '''Renvoie une liste d'octets obtenue par compression RLE'''
    liste_rle = []
    i = 0
    while i < len(liste_octets):
        c = liste_octets[i]
        k = 1
        while i+k < len(liste_octets) and liste_octets[i+k] == c:
            k += 1
        q = k // 255               # combien de fois 255 pixels identiques
        r = k % 255                # plus eventuellement un petit reste < 255
        for _ in range(q):         # q fois
            liste_rle.append(255)  # on ajoute le "couple"
            liste_rle.append(c)    # 255 fois c
        if r != 0:                 # on ajoute r fois c
            liste_rle.append(r)    
            liste_rle.append(c)
        i += k
    return liste_rle
#############################

#tests
#q1
print(codage_rle([0]))
# output : [1, 0] => len([1, 0]) > len([0])
# donc la liste obtenue n'est pas forcément de longueur inférieure

#q2
print(decodage_rle([1, 0]))
test_codage()

#q3
#encoder_decoder_image("./ep26/s01/bac_nsi_32.png")
#tout est ok
encoder_decoder_image("./ep26/s01/bac_nsi_256.png")
#le fichier bac_nsi_256.png.dec.png ne correspond pas à l'original

#q4
# le problème qui intervient sur "les gros fichiers" proviendrait des grosses images
# la fonction  'encoder_decoder_image' commence par appeler 'charger_image'
# cette dernière n'est pas à comprendre....donc le pb ne vient pas de là
# le texte invite à modifier 'codage_rle' et 'decodage_rle'
# le décodage ne doit pas poser de problème...
# dans le codage on compte combien de paquets de 255 bits identiques on a à la suite
# On ajoute alors les paquets

# on modifie la ligne 84 pour utiliser la version 2 de la fonction