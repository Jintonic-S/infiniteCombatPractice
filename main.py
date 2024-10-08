# Programme permettant un combat entre un héros et une infinité de monstres avec un système d'armes
# Auteur : Jintonic
# Date : 2024

from random import randint
from math import ceil

# Constantes
PV_INITIAUX_HÉROS = 100  # Points de vie initiaux du héros
PV_INITIAUX_MONSTRE = 80  # Points de vie initiaux du monstre
CHANCE_CRITIQUE = 5  # Pourcentage de chance de coup critique
POTION_COOLDOWN = 4  # Nombre de tours avant de pouvoir utiliser une potion
POTION_POURCENTAGE = 0.3  # Pourcentage de PV restaurés par la potion

# Définition des armes disponibles
ARMES = {
    'Épée': {'dégâts_min': 15, 'dégâts_max': 25},
    'Hache': {'dégâts_min': 20, 'dégâts_max': 30},
    'Bâton': {'dégâts_min': 10, 'dégâts_max': 20},
    'Dague': {'dégâts_min': 12, 'dégâts_max': 18},
}

def choisir_arme():
    #Permet au joueur de choisir une arme parmi les disponibles.
    print("Choisissez votre arme :")
    for idx, (arme, stats) in enumerate(ARMES.items(), 1):
        print(f"{idx}. {arme} (Dégâts : {stats['dégâts_min']} - {stats['dégâts_max']})")
    while True:
        choix = input("Entrez le numéro de l'arme choisie : ")
        if choix.isdigit() and 1 <= int(choix) <= len(ARMES):
            arme_nom = list(ARMES.keys())[int(choix)-1]
            arme_stats = ARMES[arme_nom]
            print(f"Vous avez choisi l'arme : {arme_nom}\n")
            return arme_nom, arme_stats
        else:
            print("Choix invalide. Veuillez réessayer.")

def calculer_dégâts(dégâts_min, dégâts_max, critique_chance):
    #Calcule les dégâts infligés, en tenant compte des coups critiques.
    dégâts = randint(dégâts_min, dégâts_max)
    if randint(1, 100) <= critique_chance:
        dégâts = ceil(dégâts * 1.5)
        critique = True
    else:
        critique = False
    return dégâts, critique

def tour_héros(tour, héros_pv, monstre_pv, potion_pv, arme_stats, nb_monstre):
    #Gère le tour du héros, y compris l'utilisation des potions et l'attaque avec l'arme
    if tour % POTION_COOLDOWN == 0 and héros_pv < PV_INITIAUX_HÉROS:
        soins = min(potion_pv, PV_INITIAUX_HÉROS - héros_pv)
        héros_pv += soins
        print(f"Le héros boit une potion de soin et récupère {soins} points de vie !")
    else:
        dégâts, critique = calculer_dégâts(arme_stats['dégâts_min'], arme_stats['dégâts_max'], CHANCE_CRITIQUE)
        action = "fait un coup critique et inflige" if critique else "inflige"
        print(f"Le héros {action} {dégâts} dégâts au monstre ({nb_monstre}) avec une {arme_nom}.")
        monstre_pv -= dégâts
    return héros_pv, monstre_pv

def tour_monstre(monstre_num, héros_pv):
    #Gère le tour du monstre
    dégâts_min = 5 * monstre_num
    dégâts_max = 15 * monstre_num
    dégâts, critique = calculer_dégâts(dégâts_min, dégâts_max, CHANCE_CRITIQUE)
    action = "fait un coup critique et inflige" if critique else "inflige"
    print(f"Le monstre ({monstre_num}) {action} {dégâts} dégâts au héros.")
    héros_pv -= dégâts
    return héros_pv

# Initialisation des variables
points_vie_joueur = PV_INITIAUX_HÉROS
points_vie_monstre = PV_INITIAUX_MONSTRE
pv_potion = ceil(PV_INITIAUX_HÉROS * POTION_POURCENTAGE)
nb_tours = 1
nb_monstre = 1

# Choix de l'arme par le héros
arme_nom, arme_stats = choisir_arme()

# Boucle principale du jeu
while points_vie_joueur > 0:
    print(f"Tour {nb_tours} :")
    # Tour du héros
    points_vie_joueur, points_vie_monstre = tour_héros(nb_tours, points_vie_joueur, points_vie_monstre, pv_potion, arme_stats, nb_monstre)
    # Vérifie si le monstre est vaincu
    if points_vie_monstre <= 0:
        print(f"Vous avez gagné, le monstre {nb_monstre} a été vaincu !")
        nb_monstre += 1
        points_vie_monstre = nb_monstre * PV_INITIAUX_MONSTRE
        print("Le prochain monstre arrive.\n")
        nb_tours += 1
        continue
    # Tour du monstre
    points_vie_joueur = tour_monstre(nb_monstre, points_vie_joueur)
    # Affichage des points de vie restants
    print(f"Points de vie restants du héros : {points_vie_joueur}.")
    print(f"Points de vie restants du monstre ({nb_monstre}) : {points_vie_monstre}.\n")
    # Vérifie si le héros est vaincu
    if points_vie_joueur <= 0:
        print("Vous avez perdu, le héros a été vaincu.")
        break
    nb_tours += 1

print("Game Over !")