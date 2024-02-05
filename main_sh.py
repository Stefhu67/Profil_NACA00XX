from fonction_sh import *

texte_utilisateur = "Ce script permet de calculer des profils NACA-00XX."
print(texte_utilisateur)

# Profil NACA-00XX
valeur_X = input(f"Veuillez taper la valeur X et appuyer sur 'Entrer': \n")
nom_naca = valeur_X + valeur_X
print("Le profil étudié est: NACA-00" + nom_naca)

# Calcul du pourcentage de l'épaisseur maximale
epaisseur_maximale = np.intc(nom_naca) / 100

# Définition de la corde, du nombre de point le long de la corde et du type de distribution
corde = np.single(input("Entrer la corde en mètre: \n"))
nombre_point_corde = np.intc(input("Le nombre de points le long de la corde: \n"))
type_distribution = np.intc(input("Choisisser le type de distribution de point le long de la corde: \n"
                                  "1: Distribution de points uniforme.\n"
                                  "2: Distribution de points non-uniforme selon la transformation de Glauert.\n"))

# Choix de distribution uniforme
if type_distribution == 1:
    print('Pour une distribution uniforme: \n')

    # Calcul des coordonnée x_up, y_up
    coordonnee_x_c = np.linspace(0, 1, nombre_point_corde)
    coordonnee_x_up, coordonnee_y_up = calculate_coordinate_xy_up(coordonnee_x_c, epaisseur_maximale, corde)

    # Construction des tableaux (x_up, y_up) et (x_down, y_down)
    tableau_coordonnee_up, tableau_coordonnee_down = generer_tableau(coordonnee_x_up, coordonnee_y_up)

    # Determination de la position maximale et l'épaisseur maximale du profil
    position_maximale, epaisseur_profile = obtenir_epaisseur_maximale_et_positon(tableau_coordonnee_up,
                                                                                 tableau_coordonnee_down,
                                                                                 coordonnee_y_up)
    print(f"L'épaisseur maximale du profil est {epaisseur_profile}m "
          f"et se situe à la position x = {position_maximale}.")

    # Afficher et sauvegarder le graphique du profil
    dessiner_graphique(coordonnee_x_up, coordonnee_y_up, nom_naca)

elif type_distribution == 2:
    print('Pour une distribution non-uniforme selon la transformée de glauert: \n')

    # Calcul des coordonnée x_up, y_up avec la transformée de Glauert
    coordonnee_x_c = transformate_glauert(nombre_point_corde)
    coordonnee_x_up, coordonnee_y_up = calculate_coordinate_xy_up(coordonnee_x_c, epaisseur_maximale, corde)

    # Construction des tableaux (x_up, y_up) et (x_down, y_down)
    tableau_coordonnee_up, tableau_coordonnee_down = generer_tableau(coordonnee_x_up, coordonnee_y_up)

    # Determination de la position maximale et l'épaisseur maximale du profil
    position_maximale, epaisseur_profile = obtenir_epaisseur_maximale_et_positon(tableau_coordonnee_up,
                                                                                 tableau_coordonnee_down,
                                                                                 coordonnee_y_up)
    print(f"L'épaisseur maximale du profil est {epaisseur_profile}m "
          f"et se situe à la position x = {position_maximale}.")

    # Afficher et sauvegarder le graphique du profil
    dessiner_graphique(coordonnee_x_up, coordonnee_y_up, nom_naca)

else:
    # Cas si l'utilisateur ne rentre pas le bon type de distribution
    print("Les valeurs attendues sont: 1 ou 2. Veuillez relancer le script!")
