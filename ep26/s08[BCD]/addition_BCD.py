#############################################################################
# Question 1 : Mise en évidence du problème des flottants                   #
#############################################################################
# Écrire ci-dessous la fonction calcul_recettes() et son appel
def calcul_recettes():
    """
    retourne une recette
    """
    nb_resto = 1000
    nb_repas = 500
    prix_entree = 2.27
    prix_plat  = 5.19
    prix_dessert = 1.81
    print(f"{prix_entree :.50f}")
    print(f"{prix_plat :.50f}")
    print(f"{prix_dessert :.50f}")
    prix_repas = prix_entree + prix_plat + prix_dessert
    return prix_repas * nb_repas * nb_resto

#test
print(calcul_recettes())
#### output:
# 4635000.000000001
# 2.27000000000000001776356839400250464677810668945312
# 5.19000000000000039079850466805510222911834716796875
# 1.81000000000000005329070518200751394033432006835938
#
# il y a une différence entre le résultat obtenu par le calcul réalisé
# par la fonction et la valeur théorique : la représentation des réels décimaux en binaire
# peut ne pas être finie. Une approximation est nécessaire.

#############################################################################
# Question 2 : Conversion BCD vers Décimal                                  #
#############################################################################
# Écrire ci-dessous la fonction convertir_BCD_vers_decimal(liste_quartets)
# et l'assertion de test demandée
def convertir_BCD_vers_decimal(liste_quartets):
    """
    renvoie la valeur décimale correspondante  à une liste de chaînes de caractères 
    représentant des quartets BCD
    """
    assert type(liste_quartets) == list and len(liste_quartets) >= 3
    assert all(type(elt) == str for elt in liste_quartets)
    nb_str = ''
    chaine = ''
    n = len(liste_quartets)
    for i in range(n):
        chaine = str(int(liste_quartets[i], base = 2))
        if i == n - 3:
            chaine = chaine +  '.'
        nb_str += chaine
    return float(nb_str)

# q2
assert convertir_BCD_vers_decimal(['0001','0011', '0101', '0110']) == 13.56
assert convertir_BCD_vers_decimal(['0001', '0111', '0101']) == 1.75
print("bvo, les tests q2 sont passés")
#############################################################################
# Code fourni pour les questions 3 et 4                                     #
#############################################################################

def convertir_dec_vers_BCD(decimal):
    """
    Convertit une chaîne représentant un décimal vers une liste de quartets BCD.
    Convention : virgule implicite avant les deux derniers quartets.
    """
    ajouter_zero = False
    liste_quartets = []

    if '.' not in decimal:
        decimal = decimal + '.00'

    for i in range(len(decimal)):
        if decimal[i] != '.':
            quartet = bin(int(decimal[i]))[2:].zfill(4)
            liste_quartets.append(quartet)

        # Si le nombre n'a qu'un seul chiffre après la virgule
        if decimal[i] == '.' and i == len(decimal) - 2:
            ajouter_zero = True

    if ajouter_zero:
        liste_quartets.append('0000')

    return liste_quartets


def additionner_binaire_quartets(quartet1, quartet2, retenue):
    """
    Additionne bit à bit deux quartets binaire purs.
    Renvoie un tuple (somme_binaire_str, nouvelle_retenue_int).
    """
    somme = ""
    for i in range(4):
        # Lecture de la droite vers la gauche
        bit1 = int(quartet1[3 - i])
        bit2 = int(quartet2[3 - i])
        total = bit1 + bit2 + retenue

        if total == 0:
            somme = '0' + somme
            retenue = 0
        elif total == 1:
            somme = '1' + somme
            retenue = 0
        elif total == 2:
            somme = '0' + somme
            retenue = 1
        elif total == 3:
            somme = '1' + somme
            retenue = 1

    return somme, retenue


def corriger_BCD(somme, retenue):
    """
    Applique la correction BCD si le quartet dépasse 9 ou génère une retenue.
    Ajoute '0110' (6) au quartet invalide.
    """
    # Si somme >= 10 ('1010' ou '1011' ou '1100' etc.)
    if somme[0] == '1' and (somme[1] == '1' or somme[2] == '1'):
        somme, retenue = additionner_binaire_quartets(somme, '0110', 0)
        return somme, retenue

    # S'il y a eu dépassement naturel lors de l'addition binaire
    if retenue == 1:
        somme, _ = additionner_binaire_quartets(somme, '0110', 0)
        return somme, retenue
        
    return somme, retenue


def aligner_quartets(q1: list, q2: list) -> tuple:
    """
    Doit équilibrer les deux listes en ajoutant des '0000' à gauche 
    de la liste la plus courte.
    """
    n = max(len(q1), len(q2))
    q1 = ['0000'] * (n - len(q1)) + q1
    q2 = ['0000'] * (n - len(q2)) + q2           

    return q1, q2


def additionner_nombres_format_BCD(a, b):
    """
    Additionne deux nombres au format BCD, quartet par quartet.
    """
    liste_quartets1 = convertir_dec_vers_BCD(a)
    liste_quartets2 = convertir_dec_vers_BCD(b)
    
    # Ajustement de la longueur
    liste_quartets1, liste_quartets2 = aligner_quartets(liste_quartets1, liste_quartets2)
 
    retenue = 0
    resultat = []
    longueur_max = max(len(liste_quartets1), len(liste_quartets2)) 

    for i in range(longueur_max):
        index = longueur_max - i - 1
        
        # Addition binaire simple des quartets
        somme, retenue = additionner_binaire_quartets(liste_quartets1[index], liste_quartets2[index], retenue)
        if somme >= '1010' or retenue > 0:
            somme, retenue = corriger_BCD(somme, retenue)
        resultat.insert(0, somme) 

    # Gestion de la dernière retenue éventuelle
    if retenue == 1:
        resultat.insert(0, '0001')
        
    return resultat

# q3
# print(additionner_nombres_format_BCD('27', '35'))

# q4
print(additionner_nombres_format_BCD('23', '4'))
print(additionner_nombres_format_BCD('19', '1'))
