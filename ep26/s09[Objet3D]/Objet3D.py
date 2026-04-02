from Sommet import Sommet
from Face import Face
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection


class Objet3D:

    """
    Représente un objet 3D composé de sommets, de faces et d'un nom.
    """

    def __init__(self):
        """
        Initialise un objet 3D vide.
        """
        self.sommets = []
        self.faces = []
        self.nom = ""

    def ajouter_sommet(self, x, y, z):
        """
        Ajoute un sommet à l'objet 3D.
        """
        self.sommets.append(Sommet(x, y, z))

    def ajouter_face(self, liste_sommets):
        """
        Ajoute une face à l'objet 3D.
        """
        self.faces.append(Face(liste_sommets))

    def __str__(self):
        """
        Renvoie une représentation textuelle de l'objet 3D.
        """
        return str({'nom': self.nom, 'sommets': len(self.sommets), 'faces': len(self.faces)})

    def afficher(self):
        """
        Affiche l'objet 3D à l'aide de matplotlib.
        """
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        f = []
        for face in self.faces:
            print(face.sommets)
            x = [(self.sommets[s-1].x, self.sommets[s-1].y, self.sommets[s-1].z)
                 for s in face.sommets]
            f.append(x)
        mesh = Poly3DCollection(f, alpha=0.4, edgecolor='black')
        ax.add_collection3d(mesh)
        # plt.show()
        plt.savefig('./ep26/s09[Objet3D]/pyramide.png')

#############################################################################
# Méthode à modifier de la question 5                                       #
#############################################################################
    def transformer(self, rapport):
        """
        Applique une transformation d'échelle à l'objet 3D en renvoyant un nouvel
        objet résultant de la transformation, sans modifier l'instance d'origine.
        """
        sommets = []
        for sommet in self.sommets:
            sommets.append(
                Sommet(sommet.x*rapport, sommet.y*rapport, sommet.z*rapport))
        obj = Objet3D()
        obj.sommets = sommets
        obj.faces = self.faces
        obj.nom = self.nom + "*" + str(rapport)
        return obj


#############################################################################
# Écrire le code de la méthode trouver_sommets_adjacents de la question 2   #
#############################################################################
    def trouver_sommets_adjacents(self):
        """
        renvoie le premier couple de sommets adjacents trouvé ou None
        """
        n = len(self.sommets)
        for i in range(n):
            sommet_courant = self.sommets[i]
            for j in range(i + 1, n):
                sommet_compare = self.sommets[j]
                if sommet_courant.est_adjacent(sommet_compare):
                    return sommet_courant, sommet_compare
        return None

#############################################################################
# Programme pour tester votre méthode de la question 2                                  #
#############################################################################
objet = Objet3D()
objet.ajouter_sommet(0, 0, 0)  # s1
objet.ajouter_sommet(1, 0, 0)  # s2
objet.ajouter_sommet(0, 1, 0)  # s3
objet.ajouter_sommet(0, 0, 1)  # s4
print(objet.trouver_sommets_adjacents())