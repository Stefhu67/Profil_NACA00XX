import numpy as np
import matplotlib.pyplot as plt

# calculer la transformation de Glauert
def transformate_glauert(nombre_point):
    theta = np.linspace(0, np.pi, nombre_point)
    return 1 / 2 * (1 - np.cos(theta))

# Calculer la coordonnée yt avec la formule de l'énoncé
def calculate_coordinate_yt(coordinate_x, epaisseur):
    yt = 5 * epaisseur * (0.2969 * np.sqrt(coordinate_x)
                          - 0.1260 * coordinate_x
                          - 0.3516 * np.power(coordinate_x, 2)
                          + 0.2843 * np.power(coordinate_x, 3)
                          - 0.1036 * np.power(coordinate_x, 4))
    return yt

# Obtenir les coordonnées (x_up, y_up)
def calculate_coordinate_xy_up(x_c, epaisseur, corde_valeur):
    y_t = calculate_coordinate_yt(x_c, epaisseur)
    return x_c * corde_valeur, y_t * corde_valeur

# Générer des tableaux (x_up, y_up) et (x_down, y_down)
def generer_tableau(x_up, y_up):
    tableau_up = np.array([x_up, y_up])
    tableau_down = np.array([x_up, -y_up])
    return tableau_up.transpose(), tableau_down.transpose()

# Fonction pour trouver l'index de coordonnée maximale de yt
def trouver_coordonnees_maximale(tableau, y):
    return tableau[np.argmax(y)]

# Fonction qui retourne l'épaisseur du profil et la position x_up
def obtenir_epaisseur_maximale_et_positon(tableau_up, tableau_down, y_up):
    coordonnee_max_up = trouver_coordonnees_maximale(tableau_up, y_up)
    coordonnee_max_down = trouver_coordonnees_maximale(tableau_down, y_up)
    return np.around(coordonnee_max_up[0], 3), np.around(coordonnee_max_up[1] - coordonnee_max_down[1], 3)

# Fonction pour tracer le profil
def dessiner_graphique(x_up, y_up, epaisseur):
    # Paramètres du graphique
    plt.rcParams['font.size'] = 14
    plt.rcParams['figure.autolayout'] = True  # s'assure que tout rentre dans la figure
    plt.rcParams['figure.dpi'] = 100

    # Courbe de l'extrados
    plt.plot(x_up, y_up, label='Extrados', color='b')

    # Courbe de l'intrados
    plt.plot(x_up, -y_up, label='Intrados', color='r')

    # Garder la même échelle sur les axes
    plt.axis('equal')

    # Définition du label x et y
    plt.xlabel('x [m]')
    plt.ylabel('y [m]')

    # Afficher la légende
    plt.legend()

    # Afficher une grille
    plt.grid()

    # Définition du titre
    plt.title('Profil NACA-00' + epaisseur)  # on spécifie que l'on veut un titre

    # Sauvegarde du fichier en png et pdf
    plt.savefig('NACA-00' + epaisseur + '.png')
    plt.savefig('NACA-00' + epaisseur + '.pdf')

    # Afficher le graphique
    plt.show()
