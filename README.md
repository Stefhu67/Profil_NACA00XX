# Génération d'un Profil NACA00XX

Ce script propose une manière de générer un profil NACA00XX à partir d'une discrétisation de points uniforme ou non-uniforme selon la transformation de Glauert.
Ces profils sont définis par 2 paramètres:

- la corde du profil $c$,
- le pourcentage de l'épaisseur maximale $t$.
  
$$ t = \frac{XX}{100}$$

On définit ensuite deux coordonnées adimensionnelles $(x_c, y_t)$ avec $x_c$ une distribution de point allant de 0 à 1. Cette distribution peut être:

- linéraire,
- non-uniforme avec la transformée de Glauert.

$$ x_c = \frac{1}{2} (1 - cos(\theta)), $$
avec $\theta$ qui varie entre $0$ et $\pi$.

$y_t$ est obtenue avec la relation:

$$y_t = 5 t \left( 0.2969 \sqrt{x_c} - 0.1260 x_c -0.3516 x_c^2 + 0.2843 x_c^3 - 0.1036 x_c^4 \right)$$

Les coordonnées de l'extrados $(x_{up}, y_{up})$ et intrados $(x_{down}, y_{down})$ sont obtenus avec:

$$ (x_{up}, y_{up}) = (x_{up} c, y_{up} c)$$
$$(x_{down}, y_{down}) = (x_{down} c, - y_{down} c)$$

## Package et Modules

Ce script fait appelle aux modules ```numpy``` et ```matplotlib```. 

## Fonction du script

- La fonction ```transformate_glauert()``` calcule la distribution de points selon la formule $ x_c = \frac{1}{2} (1 - cos(\theta))$.
- La fonction ```calculate_coordinate_yt()``` calcule $y_t$ selon $y_t = 5 t \left( 0.2969 \sqrt{x_c} - 0.1260 x_c -0.3516 x_c^2 + 0.2843 x_c^3 - 0.1036 x_c^4 \right)$.
- La fonction ```calculate_coordinate_xy_up()``` calcule $ (x_{up}, y_{up}) = (x_{up} c, y_{up} c)$. Elle fait appelle à la fonction précédente ```calculate_coordinate_yt()```.
- La fonction ```generer_tableau()``` les coordonnées de l'extrados $(x_{up}, y_{up})$ et intrados $(x_{down}, y_{down})$.
- La fonction ```trouver_coordonnees_maximale()``` retourne l'index de coordonnée maximale de $y_{up}$.
- La fonction ```obtenir_epaisseur_maximale_et_positon()``` retourne l'épaisseur du profil et la position $x_{up}$. Elle fait appelle à la fonction ```trouver_coordonnees_maximale()```.
- La fonction ```dessiner_graphique()``` permet d'afficher et de sauvegarder en png ou pdf le profil.

## Déroulement du script

L'utilisateur définira lui même le profil spécifique qu'il souhaitera étudier en choisissant la valeur X du profil NACA00XX avec ```input()```. Il définira ensuite la corde $c$ en mètre, la discrétisation du nombre de point ```nombre_point_corde``` et le type de distribution. 

- Pour le choix ```1```: $x_c$ est défini par ```np.linspace(0, 1, nombre_point_corde)```.
- Pour ```2```: $x_c$ est obtenu grâce à la fonction ```transformate_glauert()```.

À partir de $x_c$, le script emploie les fonction ```calculate_coordinate_yt()``` et ```calculate_coordinate_xy_up()``` pour obtenir $(x_{up}, y_{up}$. Il génère ensuite des tableaux ```numpy``` pour les coordonnées $(x_{up}, y_{up})$ et $(x_{down}, y_{down})$. Il retourne ensuite l'épaisseur du profil et la position $x_{up}$. avec ```trouver_coordonnees_maximale()``` et ```obtenir_epaisseur_maximale_et_positon()```. Finalement, il affiche et sauvegarde le tracé du profil avec ```dessiner_graphique()```.




