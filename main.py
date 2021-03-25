#On importe la librairie turtle
from turtle import *
from random import *

#Paramètres généraux
hideturtle()
#On met la vitesse maximale pour la tortue
speed(0)

#Fonction qui génère et dessine une courbe de koch
def courbe_de_koch (nombre_iteration, couleur):
  #On met un assert pour que le nombre d'itération soit bien un nombre entier et que la boucle puisse se faire. De plus, il faut que ce nombre soit positif ou nul mais on le limite a 5 maximum pour que ça ne prenne pas trop de temps et que ça reste avec une épaisseur et un centrage acceptable.
  assert type(nombre_iteration) == int and nombre_iteration >= 0 and nombre_iteration <= 5
  #On définit les variables initiales.
  #Variable qui stocke de combien est-ce que la tortue avance lorsqu'elle a une instruction qui lui dit d'avancer
  avant=200
  #Variable qui stocke l'épaisseur de la tortue
  epaisseur = 10
  #Variable qui stocke le décalage de la tortue au début
  decalage = 100
  #Variable qui stock de combien de degrés la tortue doit tourner lorsqu'elle a une instruction qui lui dit de tourner
  angle = 90
  #Variable qui stock la chaine de départ
  chaine_actuelle="F"
  #Variable qui stock les regles de création de la chaine
  regle=["F","F+F-F-F+F"]
  #Génère la chaine
  #Fait une boucle qui tourne autant de fois qu'on veut itérer la chaine
  for i in range(nombre_iteration):
    #A chaque itération la chaine et donc le dessin devient de plus en plus gros donc on rapetisse les variables d'avancement et d'épaisseur pour que la taille reste convenable
    avant = avant * 0.4
    epaisseur = epaisseur * 0.6
    #A chaque itération, on décale le dessin a chaque fois un peu plus du centre pour qu'il reste centré
    decalage = decalage * 1.2
    #On créé une nouvelle chaine vide
    nouvelle_chaine = ""
    #On parcours tous les caractères de l'ancienne chaine
    for caractere in chaine_actuelle:
      #Si on rencontre le caractère de la regle alors on ajoute à la nouvelle chaine les caractères correspondants
      if caractere == regle[0]:
        nouvelle_chaine = nouvelle_chaine + regle[1]
      #Si on ne trouve pas de caractères qui correpond a la regle alors on remet le même caractère
      else:
        nouvelle_chaine = nouvelle_chaine + caractere
    #On remplace l'ancienne chaine par la nouvelle
    chaine_actuelle = nouvelle_chaine
  #Initialisation de la tortue
  #On se déplace à l'endroit où l'on commence à dessiner
  up()
  goto(decalage, -decalage)
  #On fixe la direction à laquelle on veut que la tortue commence
  setheading(180)
  down()
  #On met l'épaisseur a la valeur définie auparavant
  width(epaisseur)
  #On définie la couleur
  color(couleur)
  #Dessine
  #Parcours tous les caractères de la chaine
  for caractere in chaine_actuelle:
    #Si l'on rencontre un F alors on avance de la valeur définie auparavant
    if caractere == "F":
      forward(avant)
    #Si l'on rencontre un + alors on tourne a droite de la valeur définie auparavant
    elif caractere == "+":
      right(angle)
    #Si l'on rencontre un - alors on tourne a gauche de la valeur définie auparavant
    elif caractere == "-":
      left(angle)

#Fonction qui génère et dessine un flocon de koch
def flocon_de_koch (nombre_iteration, couleur):
  #On met un assert pour que le nombre d'itération soit bien un nombre entier et que la boucle puisse se faire. De plus, il faut que ce nombre soit positif ou nul mais on le limite a 4 maximum pour que ça ne prenne pas trop de temps et que ça reste avec une épaisseur et un centrage acceptable.
  assert type(nombre_iteration) == int and nombre_iteration >= 0 and nombre_iteration <= 4
  #On définit les variables initiales.
  #Variable qui stocke de combien est-ce que la tortue avance lorsqu'elle a une instruction qui lui dit d'avancer
  avant = 200
  #Variable qui stocke l'épaisseur de la tortue
  epaisseur = 10
  #Variable qui stocke le décalage de la tortue au début
  decalage = 100
  #Variable qui stock de combien de degrés la tortue doit tourner lorsqu'elle a une instruction qui lui dit de tourner
  angle = 60
  #Variable qui stock la chaine de départ
  chaine_actuelle = "F++F++F"
  #Variable qui stock les regles de création de la chaine
  regle = ["F", "F-F++F-F"]
  #Génère la chaine
  #Fait une boucle qui tourne autant de fois qu'on veut itérer la chaine
  for i in range(nombre_iteration):
    #A chaque itération la chaine et donc le dessin devient de plus en plus gros donc on rapetisse les variables d'avancement et d'épaisseur pour que la taille reste convenable
    avant = avant * 0.37
    epaisseur = epaisseur * 0.6
    #A chaque itération, on décale le dessin a chaque fois un peu plus du centre pour qu'il reste centré
    decalage = decalage * 1.02
    #On créé une nouvelle chaine vide
    nouvelle_chaine = ""
    #On parcours tous les caractères de l'ancienne chaine
    for caractere in chaine_actuelle:
      #Si on rencontre le caractère de la regle alors on ajoute à la nouvelle chaine les caractères correspondants
      if caractere == regle[0]:
        nouvelle_chaine = nouvelle_chaine + regle[1]
      #Si on ne trouve pas de caractères qui correpond a la regle alors on remet le même caractère
      else:
        nouvelle_chaine = nouvelle_chaine + caractere
    #On remplace l'ancienne chaine par la nouvelle
    chaine_actuelle = nouvelle_chaine
  #Initialisation de la tortue
  #On se déplace à l'endroit où l'on commence à dessiner
  up()
  goto(-decalage, decalage)
  #On fixe la direction sur 0 pour être que ce soit la direction souhaitée
  setheading(0)
  down()
  #On met l'épaisseur a la valeur définie auparavant
  width(epaisseur)
  #On définie la couleur
  color(couleur)
  #Dessine
  #Parcours tous les caractères de la chaine
  for caractere in chaine_actuelle:
    #Si l'on rencontre un F alors on avance de la valeur définie auparavant
    if caractere == "F":
      forward(avant)
    #Si l'on rencontre un + alors on tourne a droite de la valeur définie auparavant
    elif caractere == "+":
      right(angle)
    #Si l'on rencontre un - alors on tourne a gauche de la valeur définie auparavant
    elif caractere == "-":
      left(angle)

#Fonction qui génère et dessine un arbre en 2D
def arbre_2D (nombre_iteration):
  #On met un assert pour que le nombre d'itération soit bien un nombre entier et que la boucle puisse se faire. De plus, il faut que ce nombre soit positif ou nul mais on le limite a 4 maximum pour que ça ne prenne pas trop de temps et que ça reste avec une épaisseur et un centrage acceptable.
  assert type(nombre_iteration) == int and nombre_iteration >= 0 and nombre_iteration <= 4
  #On définit les variables initiales
  #Variable qui va stocker les positions de la tortue quand on en aura besoin
  memoire = []
  #Variable qui stocke de combien est-ce que la tortue avance lorsqu'elle a une instruction qui lui dit d'avancer
  avant = 200
  #Variable qui stocke l'épaisseur de la tortue
  epaisseur = 10
  #Variable qui stock de combien de degrés la tortue doit tourner lorsqu'elle a une instruction qui lui dit de tourner
  angle = 22.5
  #Variable qui stock la chaine de départ
  chaine_actuelle = "F"
  #Variable qui stock les regles de création de la chaine
  regle= ["F", "FF+[+F-F-F]-[-F+F+F]"]
  #Génère la chaine
  #Fait une boucle qui tourne autant de fois qu'on veut itérer la chaine
  for i in range(nombre_iteration):
    #A chaque itération la chaine et donc le dessin devient de plus en plus gros donc on rapetisse les variables d'avancement et d'épaisseur pour que la taille reste convenable
    avant = avant * 0.4
    epaisseur = epaisseur * 0.7
    #On créé une nouvelle chaine vide
    nouvelle_chaine = ""
    #On parcours tous les caractères de l'ancienne chaine
    for caractere in chaine_actuelle:
      #Si on rencontre le caractère de la regle alors on ajoute à la nouvelle chaine les caractères correspondants
      if caractere == regle[0]:
        nouvelle_chaine = nouvelle_chaine + regle[1]
      #Si on ne trouve pas de caractères qui correpond a la regle alors on remet le même caractère
      else:
        nouvelle_chaine = nouvelle_chaine + caractere
    #On remplace l'ancienne chaine par la nouvelle
    chaine_actuelle = nouvelle_chaine
  #Initialisation de la tortue
  #On se déplace à l'endroit où l'on commence à dessiner
  up()
  goto(0, -200)
  #On fixe la direction à laquelle on veut que la tortue commence
  setheading(90)
  down()
  #Dessine
  #On définit une variable facteur qui va varier en fonction de l'éloignement de la branche centrale
  facteur = 1
  #Parcours tous les caractères de la chaine
  for caractere in chaine_actuelle:
    #On met l'épaisseur a la la valeur définie auparavant et on applique le facteur dessus
    width(epaisseur * facteur)
    #Si le facteur est supérieur à 0.8 alors on dessine en brun (donc le tronc et les grosses branches)
    if facteur > 0.8:
      color("brown")
    #Autrement, si le facteur est inférieur ou égal à 0.8 alors on dessine en vert (donc les feuilles et petites branches)
    else:
      color("green")
     #Si l'on rencontre un F alors on avance de la valeur définie auparavant
    if caractere == "F":
      forward(avant*facteur)
     #Si l'on rencontre un + alors on tourne à droite de la valeur définie auparavant
    elif caractere == "+":
      right(angle)
     #Si l'on rencontre un - alors on tourne à gauche de la valeur définie auparavant
    elif caractere == "-":
      left(angle)
    #Si l'on rencontre un [ alors on sauvegarde la position et la direction de la tortue et on modifie le facteur
    elif caractere == "[":
      #On ajoute à la fin de la variable mémoire une liste contenant une liste qui contient la coordonnée x et la coordonnée y. La liste contient ensuite la direction de la tortue.
      memoire.append([[xcor(), ycor()], heading()])
      #On réduit le facteur de 10%
      facteur = facteur * 0.9
    #Si l'on rencontre un ] alors on restaure la position et la direction de la tortue et on remet le facteur à la valeur d'avant
    elif caractere == "]":
      #On lève la tortue pour que ça ne dessine plus
      up()
      #On récupère la dernière liste de la varible mémoire, donc la dernière position enregistrée et on la supprime de tableau
      etat = memoire.pop()
      #On va aux coordonnées x et y comprises dans un liste
      goto(etat[0])
      #On met la tortue à la direction sauvegardée
      setheading(etat[1])
      #On baisse la tortue pour qu'elle soit de nouveau prête à dessiner
      down()
      #On fait l'opération inverse sur le facteur pour qu'il retrouve sa valeur d'avant
      facteur = facteur / 0.9

def arbre_2D_recursif (longueur):
  #Cela sera vrai que lors du premier appel car ensuite longueur sera toujours forcément plus petit que 90
  if longueur == 90:
    #Initialisation de la tortue
    #On se déplace à l'endroit où l'on commence à dessiner
    up()
    goto(0, -200)
    #On fixe la direction à laquelle on veut que la tortue commence
    setheading(90)
    down()
  #On met l'épaisseur proportionnelle à la longueur de la branche, donc plus elle est loin, donc courtes, plus elle est fine.
  width(longueur/10)
  #On prend un angle aléatoire entre 25 et 30° pour qu'il y ait des petites variations dans l'arbre et donner un coté plus naturel.
  angle = randint(25,30)
  #On choi
  retrecissement = 0.7 + 0.1*random()
  if longueur <= 30:
    color("green")
    stamp()
    color("brown")
  if longueur > 15 :
    color("brown")
    forward(longueur)
    #On tourne à gauche pour faire la prochaine branche à gauche
    left(angle)
    #On ré appelle la fonction pour faire une autre branche
    arbre_2D_recursif(longueur*retrecissement)
    #Ensuite, (quand on a atteint la limite de longueur de 15), on tourne à droite pour faire les branches à droite.
    right(angle*2)
    #Et on ré appelle la fonction pour faire une autre branche
    arbre_2D_recursif(longueur*retrecissement)
    #Finalement, quand on a atteint la limite pour la droite aussi, on reviens sur ses pas
    left(angle)
    backward(longueur)

def arbre_2D_aleatoire (nombre_iteration):
  #On met un assert pour que le nombre d'itération soit bien un nombre entier et que la boucle puisse se faire. De plus, il faut que ce nombre soit positif ou nul mais on le limite a 4 maximum pour que ça ne prenne pas trop de temps et que ça reste avec une épaisseur et un centrage acceptable.
  assert type(nombre_iteration) == int and nombre_iteration >= 0 and nombre_iteration <= 6
  #On définit les variables initiales
  #Variable qui va stocker les positions de la tortue quand on en aura besoin
  memoire = []
  #Variable qui stocke de combien est-ce que la tortue avance lorsqu'elle a une instruction qui lui dit d'avancer
  avant = 200
  #Variable qui stocke l'épaisseur de la tortue
  epaisseur = 25
  #Variable qui stock la chaine de départ
  chaine_actuelle = "FX"
  #Variable qui stock les regles de création de la chaine
  #Résumé des règles :
  #1ere règle : génération normale, on avance de 1 et les branches se font de chaque coté.
  #2ème règle : génération normale mais on avance de 2 à gauche au lieu de 1.
  #3ème règle : génération normale mais on avance de 2 à droite au lieu de 1.
  #4ème règle : génération normale, mais il n'y aura pas de prochaine branche à gauche
  #5ème règle : génération normale, mais il n'y aura pas de prochaine branche à droite
  regle= [["X", "[-FX][+FX]"], ["X", "[-FFX][+FX]"], ["X", "[-FX][+FFX]"], ["X", "[-F][+FX]"], ["X", "[-FX][+F]"]]
  #Génère la chaine
  #Fait une boucle qui tourne autant de fois qu'on veut itérer la chaine
  for i in range(nombre_iteration):
    #A chaque itération la chaine et donc le dessin devient de plus en plus gros donc on rapetisse les variables d'avancement et d'épaisseur pour que la taille reste convenable
    avant = avant * 0.8
    epaisseur = epaisseur * 0.8
    #On créé une nouvelle chaine vide
    nouvelle_chaine = ""
    #On parcours tous les caractères de l'ancienne chaine
    for caractere in chaine_actuelle:
      #A chaque fois, on prend un nombre aléatoire entre 0 et 99 (donc 100 possibilités au total)
      choix_generation = randint(0, 99)
      #Si on rencontre le caractère de la regle alors on ajoute à la nouvelle chaine les caractères correspondants
      #Si le nombre choisit est entre 0 et 59, alors on applique la première règle. On a donc environ 60% de chance de prendre la première règle à chaque fois
      if caractere == regle[0][0] and choix_generation < 60:
        nouvelle_chaine = nouvelle_chaine + regle[0][1]
      #Si le nombre choisit est entre 60 et 69, alors on applique la deuxième règle. On a donc environ 10% de chance de prendre la deuxième règle à chaque fois
      elif caractere == regle[1][0] and choix_generation >= 60 and choix_generation < 70:
        nouvelle_chaine = nouvelle_chaine + regle[1][1]
      #Si le nombre choisit est entre 70 et 79, alors on applique la troisième règle. On a donc environ 10% de chance de prendre la troisième règle à chaque fois
      elif caractere == regle[2][0] and choix_generation >= 70 and choix_generation < 80:
        nouvelle_chaine = nouvelle_chaine + regle[2][1]
      #Si le nombre choisit est entre 80 et 89, alors on applique la quatrième règle. On a donc environ 10% de chance de prendre la quatrième règle à chaque fois
      elif caractere == regle[3][0] and choix_generation >= 80 and choix_generation < 90:
        nouvelle_chaine = nouvelle_chaine + regle[3][1]
      #Si le nombre choisit est entre 90 et 99, alors on applique la cinquième règle. On a donc environ 10% de chance de prendre la cinquième règle à chaque fois
      elif caractere == regle[4][0] and choix_generation >= 90 and choix_generation < 100:
        nouvelle_chaine = nouvelle_chaine + regle[4][1]
      #Si on ne trouve pas de caractères qui correpond a la regle alors on remet le même caractère
      else:
        nouvelle_chaine = nouvelle_chaine + caractere
    #On remplace l'ancienne chaine par la nouvelle
    chaine_actuelle = nouvelle_chaine
  #Initialisation de la tortue
  #On se déplace à l'endroit où l'on commence à dessiner
  up()
  #couleur_tronc =choice([ "#430505" , " #561c1c ", " #683737 ", " #694747 "])
  #couleur_feuilles = choice([" #07833e " , " #27c26b " , " #09be0f ", " #6fd372 "])
  goto(0, -200)
  #On fixe la direction à laquelle on veut que la tortue commence
  setheading(90)
  down()
  #Dessine
  #On définit une variable facteur qui va varier en fonction de l'éloignement de la branche centrale
  facteur = 1
  #Parcours tous les caractères de la chaine
  for caractere in chaine_actuelle:
    #On met l'épaisseur a la la valeur définie auparavant et on applique le facteur dessus
    width(epaisseur * facteur)
    #Si le facteur est supérieur à 0.8 alors on dessine en brun (donc le tronc et les grosses branches)
    if facteur > 0.7:
      color(choice([ "#430505" , " #561c1c ", " #683737 ", " #694747 "]))
    #Autrement, si le facteur est inférieur ou égal à 0.8 alors on dessine en vert (donc les feuilles et petites branches)
    else:
      color(choice([" #07833e " , " #27c26b " , " #09be0f ", " #6fd372 "]))
     #Si l'on rencontre un F alors on avance de la valeur définie auparavant
    if caractere == "F":
      forward(avant*facteur)
     #Si l'on rencontre un + alors on tourne à droite de la valeur définie auparavant
    elif caractere == "+":
      right(randint(35,42))
     #Si l'on rencontre un - alors on tourne à gauche de la valeur définie auparavant
    elif caractere == "-":
      left(randint(35,42))
    #Si l'on rencontre un [ alors on sauvegarde la position et la direction de la tortue et on modifie le facteu
    elif caractere == "[":
      #On ajoute à la fin de la variable mémoire une liste contenant une liste qui contient la coordonnée x et la coordonnée y. La liste contient ensuite la direction de la tortue.
      memoire.append([[xcor(), ycor()], heading()])
      #On réduit le facteur de 10%
      facteur = facteur * 0.9
    #Si l'on rencontre un ] alors on restaure la position et la direction de la tortue et on remet le facteur à la valeur d'avant
    elif caractere == "]":
      #On lève la tortue pour que ça ne dessine plus
      up()
      #On récupère la dernière liste de la varible mémoire, donc la dernière position enregistrée et on la supprime de tableau
      etat = memoire.pop()
      #On va aux coordonnées x et y comprises dans un liste
      goto(etat[0])
      #On met la tortue à la direction sauvegardée
      setheading(etat[1])
      #On baisse la tortue pour qu'elle soit de nouveau prête à dessiner
      down()
      #On fait l'opération inverse sur le facteur pour qu'il retrouve sa valeur d'avant
      facteur = facteur / 0.9      

#Fonction qui met beaucoup de sauts a la ligne pour nettoyer la console lors de la navigation dans le menu
def menu_espace ():
  print("\n\n\n\n\n\n\n\n\n\n\n")

#Variable qui stocke ce que le menu doit proposer en fonction du choix du motif de l'utilisateur
configuration_menu = {
  "1" : {
    "nom" : "Courbe de Koch",
    "iteration_max" : 5,
    "couleur" : True
  },
  "2" : {
    "nom" : "Flocon de Koch",
    "iteration_max" : 4,
    "couleur" : True
  },
  "3" : {
    "nom" : "Arbre standard",
    "iteration_max" : 4,
    "couleur" : False
  },
  "4" : {
    "nom" : "Arbre recursif",
    "iteration_max" : 0,
    "couleur" : False
  },
  "5" : {
    "nom" : "Arbre aleatoire",
    "iteration_max" : 6,
    "couleur" : False
  }
}
#Fonction qui stock les couleurs que l'utilisateur peut choisir et leur valeur hexadecimale a passer en argument des fonctions
couleurs = {
  "1" : {
    "nom" : "Bleu",
    "Hexa" : "#5766b9"
    },
  "2" : {
    "nom" : "Rouge",
    "Hexa" : "#F23636" 
    },
  "3" : {
    "nom" : "Vert",
    "Hexa" : "#57b9a1"
    },
  "4" : {
    "nom" : "Jaune",
    "Hexa" : "#F2E436 "
    },
  "5" : {
    "nom" : "Orange",
    "Hexa" : "#F2B936 "
    },
  "6" : {
    "nom" : "Violet",
    "Hexa" : "#D836F2 "
  }
}

#Fonction qui affiche le menu
def menu():
  #Affiche "Menu principal"
  print("Menu principal")
  #Compte à partir de 1 pour indiquer la ligne à selectionner pour l'utilisateur
  numerotation = 1
  #On fait une boucle pour tous les motifs disponibles dans le dictionnaire configuration_menu
  for numero_menu in configuration_menu:
    #Et on affiche le nom et le numéro de la ligne en face
    print(configuration_menu[numero_menu]["nom"] + " (" + str(numerotation) + ")")
    #A chaque ligne, on ajoute 1 a la numerotation de la ligne
    numerotation = numerotation + 1
  #On demande le numero de la ligne a l'utilisateur et on stock sa reponse dans une variable locale
  reponse_motif = input("Veuillez entrer le nombre correspondant au motif a dessiner")
  #Si la reponse n'est pas dans les choix possibles, alors on affiche une erreur et on revient au debut du menu
  if int(reponse_motif) < 1 or int(reponse_motif) > 5:
    menu_espace()
    print("Erreur, mauvais input. Retour au menu principal.\n")
    menu()
  #Si on peut choisir un nombre d'iteration pour ce motif... (pas pour l'arbre recursif pas exemple) (information recuperee dans configuration_menu)
  if configuration_menu[reponse_motif]["iteration_max"] > 0:
    #On nettoie la console
    menu_espace()
    #On affiche le motif que l'utilisateur a choisit pour qu'il voit si jamais il s'est trompe
    print("Vous avez choisit le motif " + configuration_menu[reponse_motif]["nom"])
    #On demande le nombre d'iteration a l'utilisateur et on stock sa reponse dans une variable locale
    reponse_iteration = input("Veuillez indiquer le nombre d'iteration voulu (entre 0 et " + str(configuration_menu[reponse_motif]["iteration_max"]) + ")")
    #Si la reponse n'est pas dans les choix possibles, alors on affiche une erreur et on revient au debut du menu
    if int(reponse_iteration) < 0 or int(reponse_iteration) > configuration_menu[reponse_motif]["iteration_max"]:
      menu_espace()
      print("Erreur, mauvais input. Retour au menu principal.\n")
      menu()
  #Si on peut choisir une couleur pour le motif...
  if configuration_menu[reponse_motif]["couleur"] == True:
    #On nettoie la console
    menu_espace()
    #On affiche le nombre d'iterations que l'utilisateur a choisit pour qu'il voit si jamais il s'est trompe
    print("Vous avez selectionne " + reponse_iteration + " iterations")
    print("Veuillez choisir une couleur pour le motif")
    #Compte à partir de 1 pour indiquer la ligne à selectionner pour l'utilisateur
    numerotation = 1
    #Pour chaque couleur dans la liste couleurs...
    for numero_couleur in couleurs:
      #On affiche le nom de la couleur et le numero de la ligne
      print(couleurs[numero_couleur]["nom"] + "(" + str(numerotation) + ")")
      #A chaque ligne, on ajoute 1 a la numerotation de la ligne
      numerotation = numerotation + 1
    #On demande la couleur a l'utilisateur et on stock sa reponse dans une variable locale
    reponse_couleur = input("Veuillez entrer le nombre correspondant a la couleur choisit")
    #Si la reponse n'est pas dans les choix possibles, alors on affiche une erreur et on revient au debut du menu
    if int(reponse_couleur) < 1 or int(reponse_couleur) > len(couleurs):
      menu_espace()
      print("Erreur, mauvais input. Retour au menu principal.\n")
      menu()
  #Une fois que tous les choix on ete faits...
  #On nettoie la console
  menu_espace()
  #On affiche le motif qui est en train de se dessiner
  print("Le motif " + configuration_menu[reponse_motif]["nom"] + " est en train de se dessiner...")
  #Si l'utilisateur avait selectionne la courbe de koch...
  if reponse_motif == "1":
    #On la dessine avec les arguments choisit
    courbe_de_koch(int(reponse_iteration), couleurs[reponse_couleur]["Hexa"])
    #Une fois que le motif est termine...
    #On nettoie la console
    menu_espace()
    #Et on affiche que le motif est termine avec son nom et  les parametres choisit si jamais l'utilisateur veut le refaire par la suite
    print("Le motif " + configuration_menu[reponse_motif]["nom"] + " est termine ! (" + reponse_iteration + " iterations, couleur : " + couleurs[reponse_couleur]["nom"] + ")")
  #Si l'utilisateur avait selectionne le flocon de koch...
  if reponse_motif == "2":
    #On le dessine avec les arguments choisit
    flocon_de_koch(int(reponse_iteration), couleurs[reponse_couleur]["Hexa"])
    #Une fois que le motif est termine...
    #On nettoie la console
    menu_espace()
    #Et on affiche que le motif est termine avec son nom et les parametres choisit si jamais l'utilisateur veut le refaire par la suite
    print("Le motif " + configuration_menu[reponse_motif]["nom"] + " est termine ! (" + reponse_iteration + " iterations, couleur : " + couleurs[reponse_couleur]["nom"] + ")")
  #Si l'utilisateur avait selectionne l'arbre standard...
  if reponse_motif == "3":
    #On le dessine avec l'argument choisit
    arbre_2D(int(reponse_iteration))
    #Une fois que le motif est termine...
    #On nettoie la console
    menu_espace()
    #Et on affiche que le motif est termine avec son nom et le parametre choisit si jamais l'utilisateur veut le refaire par la suite
    print("Le motif " + configuration_menu[reponse_motif]["nom"] + " est termine ! (" + reponse_iteration + " iterations)")
  #Si l'utilisateur avait selectionne l'arbre recursif...
  if reponse_motif == "4":
    #On le dessine
    arbre_2D_recursif(90)
    #Une fois que le motif est termine...
    #On nettoie la console
    menu_espace()
    #Et on affiche que le motif est termine avec son nom si jamais l'utilisateur veut le refaire par la suite
    print("Le motif " + configuration_menu[reponse_motif]["nom"] + " est termine !")
  #Si l'utilisateur avait selectionne l'arbre aleatoire...
  if reponse_motif == "5":
    #On le dessine avec l'argument choisit
    arbre_2D_aleatoire(int(reponse_iteration))
    #Une fois que le motif est termine...
    #On nettoie la console
    menu_espace()
    #Et on affiche que le motif est termine avec son nom et le parametre choisit si jamais l'utilisateur veut le refaire par la suite
    print("Le motif " + configuration_menu[reponse_motif]["nom"] + " est termine ! (" + reponse_iteration + " iterations)")

#Au debut du programme...
#On nettoie la console pour que le menu s'affiche ensuite en partant du bas de l'ecran et ainsi etre regulier puisque si l'utilisateur fait une erreur, le menu sera affiche en partant du bas de l'ecran donc comme ça on est regulier.
menu_espace()
#On affiche le menu
menu()