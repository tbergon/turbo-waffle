import random

class Joueur:
    """( ͡°( ͡° ͜ʖ( ͡° ͜ʖ ͡°)ʖ ͡°) ͡°)"""

    def __init__(self,nom,argent):
        self.nom=nom
        self.argent=argent
        self.main=list()
    
    def __str__(self):
        return "Je m'appelle {} et j'ai utilisé Cheat Engine pour avoir {} $".format(self.nom,self.argent)
    
    def pari(self,m):
        self.argent -= m
        return m

    def nouvelleMain(self,a,b):
        self.main.append(a)
        self.main.append(b)


class Carte:
    """Bah c'est une carte quoi *_*"""

    noms_couleurs = ['Trèfle', 'Carreau', 'Cœur', 'Pique']
    noms_valeurs = [None,'As', '2', '3', '4', '5', '6', '7', 
              '8', '9', '10', 'Valet', 'Dame', 'Roi']

    def __init__(self, couleur = 0, valeur = 2):
        self.couleur = couleur
        self.valeur = valeur

    def __str__(self):
        """Une fonction qui donne le nom de la carte OwO"""
        return '{} de {}'.format(Carte.noms_valeurs[self.valeur],Carte.noms_couleurs[self.couleur])

    def __lt__(self, other):
        """Une fonction qui compare UwU"""
        if self.couleur < other.couleur: return True
        if self.couleur > other.couleur: return False

        return self.valeur < other.valeur



class Paquet:
    """A big deck of 52 cards ;)"""

    def __init__(self):
        self.cartes = []
        for couleur in range(4):
                for valeur in range(1, 14):
                    carte = Carte(couleur, valeur)
                    self.cartes.append(carte)

    def __str__(self):
        """Pour afficher les noms des cartes du paquet IwI"""
        res = []
        for carte in self.cartes:
            res.append(str(carte))
        return "\n".join(res)

    def pop_carte(self):
        """On prend une carte OwU"""
        self.cartes.pop()
    def ajouter_carte(self, carte):
        """On rajoute une carte UwO"""
        self.cartes.append(carte)
    def battre(self):
        """On mélange sinon c'est pas cool :c"""
        random.shuffle(self.cartes)
    
    def deplacer_cartes(self, main, nombre):
        for i in range(nombre):
            main.ajouter_carte(self.pop_carte())

# class Main(Paquet):
#     """Représente une main au jeu de cartes o_O"""

#     def __init__(self, etiquette = ''):
#         self.cartes = []
#         self.etiquette = etiquette

    

cartes=Carte()
paquet = Paquet()
main=[]
# main=Main('première main')
# print("La",main.etiquette,"comprend :")
paquet.deplacer_cartes(main,2)
# print(main.cartes)
print(main)
