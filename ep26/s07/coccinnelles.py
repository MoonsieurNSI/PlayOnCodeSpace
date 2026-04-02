import random


class Coccinelle:
    def __init__(self, sexe, age, niv_nutrition):
        self.age = age
        self.esperance_de_vie = random.randint(200, 350)
        self.sexe = sexe
        self.niv_nutrition = niv_nutrition

    def chasser(self, nb_proies, nb_coccinelles):
        """
        retourne:
        - nb_proies si plus de coccinelles
        - nb_proies restantes après chasse/consommation sinon
        
        """
        #si plus de coccinelles
        if nb_coccinelles == 0: 
            return nb_proies

        proies_par_cocci = nb_proies / nb_coccinelles

        # caclul de la consommation selon les cas
        if proies_par_cocci > 20:
            consomme = random.randint(12, 20)
        elif proies_par_cocci > 10:
            consomme = random.randint(8, 15)
        else:
            consomme = random.randint(3, 8)

        # on ajuste si la valeur aléatoire obtenue est > nb_poies
        # au max on consomme donc le nb_proies
        consomme = min(consomme, nb_proies)

        # ajustement du niveau de nutrition selon la consommation
        # ce niveau peut atteindre 0
        if consomme >= 10:
            self.niv_nutrition += 1
        else:
            self.niv_nutrition = max(0, self.niv_nutrition - 1)

        # on retourne le nb_proies restantes après la chasse
        return nb_proies - consomme

    def reproduction(self):
        """
        Une femelle avec un niveau de nutrition >= 2 engendre exactement
        deux descendants : un mâle et une femelle.
        """
        descendants = []
        if self.sexe == "femelle" and self.niv_nutrition >= 2 and self.age >= 20:
            descendants.append(Coccinelle("male", 0, 0))
            descendants.append(Coccinelle("femelle", 0, 0))
            self.niv_nutrition = 0

        return descendants

    def a_survecu(self):
        """
        Met à jour l'âge de la coccinelle et indique si elle est encore en vie.
        """
        if self.niv_nutrition == 0 and random.random() < 1 / 3:
            self.age = self.esperance_de_vie
        else:
            self.age = self.age + 1
        return self.age < self.esperance_de_vie

    def __repr__(self):
        return f"Coccinelle {self.sexe}, âge: {self.age}/{self.esperance_de_vie}, niv_nutrition: {self.niv_nutrition}"


def evolution(population, nb_proies):
    """
    Simule une journée dans l'écosystème :
    - chasse des coccinelles
    - reproduction
    - vieillissement et mortalité
    - croissance des pucerons

    population est une liste d'instances de la classe Coccinelle
    nb_proies est un entier indiquant le nombre de proies

    Cette fonction renvoie un couple (population_suivante, nouveau_nb_proies) indiquant
    la nouvelle population à la fin de la journée et le nombre de proies.
    """
    population_suivante = []
    nouveau_nes = []
    nb_coccinelles = len(population)

    for coccinelle in population:
        nb_proies = coccinelle.chasser(nb_proies, nb_coccinelles)

        if coccinelle.a_survecu():
            population_suivante.append(coccinelle)

        nouveau_nes += coccinelle.reproduction()

    # Croissance naturelle des pucerons (augmentation de 20% par jour)
    nb_proies = int(nb_proies * 1.2)

    # Ajout des nouveau-nés en fin de journée
    population_suivante += nouveau_nes

    return population_suivante, nb_proies


#############################################################################
# Écrire ci-dessous le code pour les questions de l'énoncé                  #
#############################################################################
# q1
c1, c2, c3 = Coccinelle('F', 10, 2), Coccinelle('F', 10, 2), Coccinelle('M', 10, 2)
population = [c1, c2, c3] # lire la docstring de la fonc. evolution
proies = 200
for jour in range(5):
    population, proies = evolution(population, proies)
    print(f"Fin du jour {jour + 1:02d}: il reste {len(population)} coccinelle(s) et {proies} proie(s)")

######output
# Fin du jour 01: il reste 3 coccinelle(s) et 189 proie(s)
# Fin du jour 02: il reste 3 coccinelle(s) et 166 proie(s)
# Fin du jour 03: il reste 3 coccinelle(s) et 142 proie(s)
# Fin du jour 04: il reste 3 coccinelle(s) et 111 proie(s)
# Fin du jour 05: il reste 3 coccinelle(s) et 79 proie(s)


#q2
def simulation_simple(population, nb_proies):
    """
    renvoyer un triplet (tuple) contenant :
    le nombre final de coccinelles, le nombre final de pucerons,
    et le nombre de jours effectivement simulés.
    """
    assert type(population) == list
    assert all(isinstance(elt, Coccinelle) for elt in population)
    assert type(nb_proies) == int and nb_proies > 0
    jour = 0
    while len(population) > 0 and nb_proies > 0 and jour < 30:
        population, nb_proies = evolution(population, nb_proies)
        jour += 1
    return len(population), nb_proies, jour

#test
coccinelles, pucerons, jour = simulation_simple(population, 1000)
print(f"Après {jour} jour(s), il reste {coccinelles} coccinelle(s) et {pucerons} puceron(s)")
####output
# Après 30 jour(s), il reste 3 coccinelle(s) et 168644 puceron(s)

# q4
# voir code