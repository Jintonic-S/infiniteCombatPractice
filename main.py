# Programme permettant un combat entre un héros et une infinité de monstres
#Auteur = Jintonic

from random import randint
from math import ceil

PV_INITIAUX_HÉROS = 100 # Points de vie initiaux du héros
PV_INITIAUX_MONSTRE = 80 # Points de vie initiaux du monstre

points_vie_joueur: int # Points de vie du héros au cours du combat
points_vie_monstre: int # Points de vie du monstre au cours du combat
dégâts_joueur: int # Dégâts infligés par le héros
dégâts_monstre: int # Dégâts infligés par le monstre
nb_tours: int
taux_critique: int # Valeur du critique
victoire: int
nb_monstre: int # Numéro du monstre
pv_potion: int # PV rendu par potion

pv_potion = ceil(PV_INITIAUX_HÉROS * 0.3)
points_vie_joueur = PV_INITIAUX_HÉROS
points_vie_monstre = PV_INITIAUX_MONSTRE
nb_tours = 1
victoire = 0
nb_monstre = 1

while points_vie_joueur >= 0: # and points_vie_monstre >= 0 : Condition de combat
    print(f"Tour {nb_tours} :")
    dégâts_joueur = randint(10, 20)
    taux_critique = randint(0, 100)

    if nb_tours % 4 == 0 and points_vie_joueur != PV_INITIAUX_HÉROS: # Permet l'utilisation d'une potion
        print(f"Le héros boit une potion de soin et récupère {min(pv_potion, (PV_INITIAUX_HÉROS - points_vie_joueur))} points de vie!")
        points_vie_joueur += (min(pv_potion, (PV_INITIAUX_HÉROS - points_vie_joueur)))
    else:
        if taux_critique <= 5: # Détermination si coup critique
            dégâts_joueur = ceil(dégâts_joueur * 1.5)
            print(f"Le héros fait un coup critique et inflige {dégâts_joueur} dégâts au monstre  ({nb_monstre}).")
        else:
            print(f"Le héros inflige {dégâts_joueur} dégâts au monstre ({nb_monstre}).")
        points_vie_monstre -= dégâts_joueur

    if points_vie_monstre >= 0: # Vérifie si le monstre est encore en vie
        dégâts_monstre = randint(5 * nb_monstre, 15 * nb_monstre) # Détermine les dégâts du monstre
        taux_critique = randint(0, 100) # Détermine la valeur de taux critique
        if taux_critique <= 5: # Détermine s'il y a coup critique
            dégâts_monstre = ceil(dégâts_monstre * 1.5)
            print(f"Le monstre ({nb_monstre}) fait un coup critique et inflige {dégâts_monstre} dégâts au héros.")
        else:
            print(f"Le monstre ({nb_monstre}) inflige {dégâts_monstre} dégâts au héros.")
        points_vie_joueur -= dégâts_monstre
    print(f"Points de vie restants du héros: {points_vie_joueur}.")
    print(f"Points de vie restants du monstre ({nb_monstre}) : {points_vie_monstre}.")
    print()
    nb_tours += 1

    if points_vie_joueur <= 0: # Vérifie si le héros perd
        print("Vous avez perdu, le héros à été vaincu.")
        break

    if points_vie_monstre <= 0: # Vérifie si le monstre perd
        print(f"Vous avez gagné, le monstre {nb_monstre} à été vaincu!")
        print("Le prochain monstre arrive.", end="\n\n")
        nb_monstre += 1 # Ajoute un monstre
        points_vie_monstre = nb_monstre * PV_INITIAUX_MONSTRE # Ajuste les pv du nouveau monstre

print("Game Over !")