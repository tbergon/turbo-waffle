from test import *


def main():
    c = Couleur(255,0,0)
    v = Voiture('Ferrari', 350, c)
    print(v.vitesse)
    v.vitesse=80
    print(v.vitesse)
    v.klaxon()


main()