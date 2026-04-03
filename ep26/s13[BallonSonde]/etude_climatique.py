# ///////////////////////////////////////////////////////////////////////////
# FONCTIONS DONNEES
# ///////////////////////////////////////////////////////////////////////////

def recupere_donnees_fichier_csv(nom_fichier):
    """ Fonction qui récupère les données relevées du ballon sonde sans les en-têtes de la 1ère ligne """
    altitudes = []                                  # Initialisation des listes de valeurs relevées
    temperatures = []
    longitudes = []
    latitudes = []
    # Ouverture du fichier csv au format npm.csv en mode "read"
    contenu_fichier = open(nom_fichier, 'r')
    # Supprime la 1ère ligne avec les en-têtes
    contenu_fichier.readline()
    # Parcours des lignes du fichier csv contenant les donnees relevées
    for ligne in contenu_fichier.readlines():
        # rstrip() supprime les \n et espaces en fin de ligne
        ligne = ligne.rstrip()
        # création d'une listeValeurs. split(";") sépare les valeurs grâce au ;
        listeValeurs = ligne.split(";")
        # conversion string en int de l'altitude et insertion dans la liste correspondante
        altitudes.append(int(listeValeurs[0]))
        # conversion string en float de l'altitude et insertion dans la liste correspondante
        temperatures.append(float(listeValeurs[1]))
        # conversion string en float de l'altitude et insertion dans la liste correspondante
        longitudes.append(float(listeValeurs[2]))
        # conversion string en float de l'altitude et insertion dans la liste correspondante
        latitudes.append(float(listeValeurs[3]))
    return altitudes, temperatures, longitudes, latitudes


def genere_kml(liste_longitudes, liste_latitudes):
    """ Fonction qui génère un fichier de données géographiques au format standard international KML
        Ce fichier est visionnable ensuite dans différents logiciels
    """
    #q4
    assert len(liste_latitudes) == len(liste_longitudes)
    fichier_kml = open(
        'ballon sonde.kml', 'w')    # Création et ouverture du fichier kml en mode "write"
    entete_fichier = '<?xml version="1.0" encoding="UTF-8"?>\n'
    entete_fichier += '<kml xmlns="http://www.opengis.net/kml/2.2">\n'
    entete_fichier += '<Document>\n'
    entete_fichier += '<name>Trajectoire ballon sonde</name>\n'
    # Ecriture du contenu de la variable entete_fichier dans le fichier kml
    fichier_kml.write(entete_fichier)
    for i in range(len(liste_longitudes)):
        corps_fichier = '<Placemark>\n'
        corps_fichier += f'<name>Point {i}</name>\n'
        corps_fichier += '<Point>\n'
        corps_fichier += f'<coordinates>{liste_longitudes[i]},{liste_latitudes[i]}</coordinates>\n'
        corps_fichier += '</Point>\n'
        corps_fichier += '</Placemark>\n'
        fichier_kml.write(corps_fichier)
    bas_fichier = '</Document>\n'
    fichier_kml.write(bas_fichier)
    fichier_kml.write('</kml>\n') #q6
    fichier_kml.close()                         # Fermeture du fichier kml


# ///////////////////////////////////////////////////////////////////////////
# TRAVAIL DEMANDE
# ///////////////////////////////////////////////////////////////////////////

# QUESTION 1
altitudes, temperatures, longitudes, latitudes = recupere_donnees_fichier_csv("./releves_ballon_sonde.csv")
print(altitudes)
print(temperatures)
print(longitudes)
print(latitudes)

# QUESTION 2
def conversion_K_en_C(liste_temperatures):
    return [round(temperature - 273.15, 1) for temperature in temperatures]

#test
#q2
assert conversion_K_en_C(temperatures) == [15.0, 13.7, 11.7, 7.9, 3.4, 0.5, -2.3, -17.7, -28.9, -42.5, -48.3, -56.0, -56.2, -56.5, -56.5, -56.0, -56.1, -53.0, -50.1, -48.0]
print("bvo, le test q2 est passé")


# QUESTION 3
def altitude_la_plus_froide(liste_altitudes, liste_temperatures):
    min_temp = min(liste_temperatures)
    min_alti = [alt for alt, temp in zip(liste_altitudes, liste_temperatures) if temp == min_temp]
    return min_temp, min_alti

#test
#q3
assert altitude_la_plus_froide([7000, 10125, 13896, 14211], [-35.2, -52.1, -57.4, -57.4]) == (-57.4, [13896, 14211])
assert altitude_la_plus_froide([6000, 7250, 11542, 15214, 17300], [-33.7, -45, -53, -58.5, -60.1]) == (-60.1, [17300])
print("bvo, les tests q3 sont passés") 

# AUTRES ELEMENTS DE CODE
#q5
genere_kml(longitudes, latitudes)