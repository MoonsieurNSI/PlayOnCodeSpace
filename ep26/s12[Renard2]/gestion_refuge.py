import csv

class Renard:
    """
    Classe représentant un renard dans le refuge.
    Attributs : identifiant, nom, poids, date_arrivee.
    """
    def __init__(self, identifiant, nom, poids, date_arrivee):
        # Question 1 à compléter
        self.id = identifiant
        self.nom = nom
        self.poids = poids
        self.date_arrivee = date_arrivee

    def __str__(self):
        # Question 2 à compléter
        return f"Renard ID {self.id} - {self.nom} (Arrivé le {self.date_arrivee})"
#test
#q2
renard1 = Renard(200, "Oscar", 5.1, "2026-01-01")
print(renard1)


class Refuge:
    """
    Classe représentant le refuge contenant la liste des renards.
    """
    def __init__(self, nom, adresse):
        self.nom = nom
        self.adresse = adresse
        self.liste_renards = []
        
    def recueillir(self, un_renard):
        """
        Méthode d'ajout d'un renard au refuge.
        """
        self.liste_renards.append(un_renard)

    def lister_peu_corpulents(self):
        """
        Méthode qui renvoie une liste des Renards dont le poids est < 6.0 kg.
        """
        return [renard for renard in self.liste_renards if renard.poids < 6.0]

    def pourcentage_peu_corpulents(self):
        """
        Méthode qui renvoie le pourcentage des renards peu corpulents.
        """
        if len(self.liste_renards) == 0:
            return 0.0
        return len(self.lister_peu_corpulents()) / len(self.liste_renards) * 100

    def importer_donnees(self, nom_fichier):
        """
        Fonction qui importe les données des renards à partir d'un fichier CSV.
        """
        print(f"Tentative d'importation depuis {nom_fichier}...")
        with open(nom_fichier, 'r', encoding='utf-8') as f:
            lignes = csv.DictReader(f, delimiter=';')
            for ligne in lignes:
                renard = Renard(int(ligne['id']), ligne['nom'], float(ligne['poids']), ligne['date_arrivee'])
                self.recueillir(renard)
#q3
refuge = Refuge("SOS_Goupil", "")
print(f"{len(refuge.liste_renards)} renard(s) dans le refuge")
refuge.importer_donnees("./donnees_renard.csv")
print(f"{len(refuge.liste_renards)} renard(s) dans le refuge")

#q4
print(f"nombre renards peu corpulents: {len(refuge.lister_peu_corpulents())}")
print(f"Fraction renards peu corpulents: {refuge.pourcentage_peu_corpulents()}%")
print(f"{len(refuge.lister_peu_corpulents())/len(refuge.liste_renards) * 100}%")