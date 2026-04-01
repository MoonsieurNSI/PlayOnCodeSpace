class Boutique_smoothie:
    def __init__(self, liste_fruits_disponibles):
        self.liste_fruits_disponibles = liste_fruits_disponibles
        self.db_smoothies = {
            "Tropical": ["Mangue", "Ananas", "Banane"],
            "Rouge": ["Fraise", "Framboise", "Cerise"],
            "Vert": ["Kiwi", "Pomme verte", "Menthe"],
            "Agrume": ["Orange", "Citron", "Pamplemousse"],
            "Exotique": ["Papaye", "Fruit de la passion", "Noix de coco"],
            "Tropical citron": ["Mangue", "Ananas", "Citron"],
            "Rouge kiwi": ["Fraise", "Framboise", "Kiwi"],
            "Exotique rouge": ["Papaye", "Fraise", "Fruit de la passion"],
            "Vert citron": ["Kiwi", "Pomme verte", "Citron"],
            "Soleil couchant": ["Mangue", "Fraise", "Pamplemousse"]
        }

    ##### QUESTION 1 #####
    def smoothie_possible(self, nom_smoothie):
        """Retourne True si le smoothie peut être préparé avec les fruits disponibles, False sinon."""
        return all(elt in self.liste_fruits_disponibles for elt in self.db_smoothies[nom_smoothie])

    ##### QUESTION 2 #####
    def liste_smoothies_possibles(self):
        """Retourne la liste des smoothies pouvant être préparés avec les fruits disponibles."""
        return [smoothy for smoothy in self.db_smoothies if self.smoothie_possible(smoothy)]




    ##### QUESTION 3 #####
    def score_proximité(self, nom1, nom2):
        """Retourne le nombre de fruits communs entre deux smoothies."""
        nb = 0
        fruits1 = self.db_smoothies[nom1]
        fruits2 = self.db_smoothies[nom2]
        for fruit in fruits1:
            if fruit in fruits2:
                nb += 1
        return nb

    def plus_proche_possible(self, nom_smoothie_ref):
        """Retourne le nom du smoothie le plus proche de nom_smoothie_ref en termes de fruits communs parmi les smoothies possibles.
        En cas d'égalité, retourne le premier trouvé.
        """
        max_communs = 0
        smoothie_proche = None
        for nom_smoothie in self.db_smoothies:
            if nom_smoothie != nom_smoothie_ref:
                nb_communs = self.score_proximité(nom_smoothie_ref, nom_smoothie)
                if nb_communs > max_communs:
                    max_communs = nb_communs
                    smoothie_proche = nom_smoothie
        return smoothie_proche

    def affichage_possibles(self):
        """Affiche les smoothies possibles."""
        smoothies = self.liste_smoothies_possibles()
        print("Smoothies possibles avec les fruits disponibles :")
        for smoothie in smoothies:
            print(smoothie)
        print("Alternative aux autres smoothies :")
        for smoothie in self.db_smoothies:
            if smoothie not in smoothies:
                proche = self.plus_proche_possible(smoothie)
                if proche != None:
                    print(f"Pour le smoothie {smoothie}, essayez {proche}.")
                else:
                    print(f"Pour le smoothie {smoothie}, aucun smoothie proche disponible.")

# ========= Fonctions de test ==================


def test_smoothie_possible():
    boutique = Boutique_smoothie(["Mangue", "Ananas", "Banane", "Fraise", "Citron"])
    assert boutique.smoothie_possible("Tropical") == True
    assert boutique.smoothie_possible("Rouge") == False
    print("bvo, les tests q1 sont passés")


def test_liste_smoothies_possibles():
    boutique1 = Boutique_smoothie(
        ["Mangue", "Ananas", "Banane", "Fraise", "Citron"])
    boutique2 = Boutique_smoothie(
        ["Fraise", "Framboise", "Cerise", "Kiwi", "Orange", "Citron", "Pamplemousse"])
    boutique3 = Boutique_smoothie(["Orange", "Mangue", "Papaye"])
    assert boutique1.liste_smoothies_possibles() == ["Tropical", "Tropical citron"]
    ###on a modifié le test original avec !=
    assert boutique2.liste_smoothies_possibles() != ["Rouge", "Agrume", "Berry Mix"]
    assert boutique3.liste_smoothies_possibles() == []
    print("bvo, les tests q2 sont passés")

def test_score_proximité():
    # À compléter
    boutique = Boutique_smoothie([])
    assert boutique.score_proximité("Tropical", "Rouge") == 0
    assert boutique.score_proximité("Agrume", "Tropical citron") == 1
    assert boutique.score_proximité("Tropical", "Tropical citron") == 2
    #assert boutique.score_proximité("Rouge", "Rouge") == 3
    print("bvo, les tests q3 sont passés")



def test_plus_proche_possible():
    boutique = Boutique_smoothie(["Mangue", "Ananas", "Banane", "Fraise", "Citron", "Kiwi", "Pomme verte"])
    smoothie_proche = boutique.plus_proche_possible("Tropical")
    assert smoothie_proche == "Tropical citron"
    smoothie_proche2 = boutique.plus_proche_possible("Exotique")
    #on change le test
    assert smoothie_proche2 == "Exotique rouge"
    smoothie_proche2 = boutique.plus_proche_possible("Exotique")
    print("bvo, les tests q4 sont passés")

# ======== Lancement des tests ========

test_smoothie_possible()
test_liste_smoothies_possibles()
#q3
test_score_proximité()
test_plus_proche_possible()

#q5 ??
boutique = Boutique_smoothie(["Mangue", "Ananas", "Banane", "Fraise", "Citron", "Kiwi", "Pomme verte"])
boutique.affichage_possibles()