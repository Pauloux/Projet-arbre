#On importe la librairie turtle
from turtle import *
from random import *

#Paramètres généraux
hideturtle()
#On met la vitesse maximale pour la tortue
speed(0)

#Fonction qui génère et dessine un flocon de koch
def flocon_de_koch (nombre_iteration):
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

#Fonction qui génère et dessine une courbe de koch
def courbe_de_koch (nombre_iteration):
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

#/!\
#En cours de création
#/!\

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
  #regle= ["F", "FF+[+F-F-F]-[-F+F+F]"]
  regle= ["X", "[-FX][+FX]"]
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



#Pour voir les arbres, vous pouvez appeler les fonctions :
#flocon_de_koch() avec un nombre entre 0 et 4 en argument
#courbe_de_koch() avec un nombre entre 0 et 5 en argument
#arbre_2D() avec un nombre entre 0 et 4 en argument
#arbre_2D_recursif(90)
#arbre_2D_aleatoire() avec un nombre entre 0 et 6 en argument

arbre_2D_aleatoire(5)