from turtle import *
#from random import *
#test = [["-YF", [["X", "XFX-YF-YF+FX+FX-YF-YFFX+YF+FXFXYF-FX+YF+FXFX+YF-FXYF-YF-FX+FX+YFYF-"], ["Y", "+FXFX-YF-YF+FX+FXYF+FX-YFYF-FX-YF+FXYFYF-FX-YFFX+FX+YF-YF-FX+FX+YFY"]], 90, [200, -200], 180], ["F++F++F", ["F", "F-F++F-F"], 60, [100, -100], 180], ["F", ["F", "FF+[+F-F-F]-[-F+F+F]"], 22.5, [0, -200], 90]]
#chaine_actuelle = test[2][0]
#regles = test[0][1]
#avant = 10
#angle = test[0][2]
#memoire = []
#mniveau = []
#niv = 1
hideturtle()
speed(0)

def generer(nombre_iteration):
  global chaine_actuelle
  for i in range(nombre_iteration):
    nouvelle_chaine = ""
    for caractere in chaine_actuelle:
      if caractere == regles[0][0]:
        nouvelle_chaine = nouvelle_chaine + regles[0][1]
      else :
        nouvelle_chaine = nouvelle_chaine + caractere 
    chaine_actuelle = nouvelle_chaine 

def dessiner():
  global niv
  for j in chaine_actuelle:
    width(niv)
    if j == "F":
      forward(avant)
    elif j == "+":
      right(angle)
    elif j == "-":
      left(angle)
    elif j == "[":
      memoire.append([xcor(), ycor()])
      niv = niv - 1
    elif j == "]":
      up()
      goto(memoire.pop())
      down()
      niv = niv + 1

def flocon_de_koch (nombre_iteration):
  avant = 10
  angle = 60
  chaine_actuelle = "F++F++F"
  regle = ["F", "F-F++F-F"]
  #Generer la chaine
  for i in range(nombre_iteration):
    nouvelle_chaine = ""
    for caractere in chaine_actuelle:
      if caractere == regle[0]:
        nouvelle_chaine = nouvelle_chaine + regle[1]
      else:
        nouvelle_chaine = nouvelle_chaine + caractere
    chaine_actuelle = nouvelle_chaine
  #Initialisation de la tortue
  up()
  goto(-100, 100)
  down()
  #Dessiner
  for caractere in chaine_actuelle:
    if caractere == "F":
      forward(avant)
    elif caractere == "+":
      right(angle)
    elif caractere == "-":
      left(angle)

#flocon_de_koch(3)

def arbre_2D (nombre_iteration):
  memoire = []
  avant = 10
  angle = 22.5
  chaine_actuelle = "F"
  regle= ["F", "FF+[+F-F-F]-[-F+F+F]"]
  #Generer la chaine
  for i in range(nombre_iteration):
    nouvelle_chaine = ""
    for caractere in chaine_actuelle:
      if caractere == regle[0]:
        nouvelle_chaine = nouvelle_chaine + regle[1]
      else:
        nouvelle_chaine = nouvelle_chaine + caractere
    chaine_actuelle = nouvelle_chaine
  #Initialisation de la tortue
  up()
  goto(0, -200)
  left(90)
  down()
  #Dessiner
  for caractere in chaine_actuelle:
    if caractere == "F":
      forward(avant)
    elif caractere == "+":
      right(angle)
    elif caractere == "-":
      left(angle)
    elif caractere == "[":
      memoire.append([[xcor(), ycor()], heading()])
    elif caractere == "]":
      up()
      etat = memoire.pop()
      goto(etat[0])
      setheading(etat[1])
      down()

arbre_2D (4)
  
def courbe_de_koch (nombre_iteration):
  angle= 90
  chaine_actuelle="F"
  regle=["F","F+F-F-F+F"]
  #Generer la chaine
  for i in range(nombre_iteration):
    nouvelle_chaine = ""
    for caractere in chaine_actuelle:
      if caractere == regle[0]:
        nouvelle_chaine = nouvelle_chaine + regle[1]
      else:
        nouvelle_chaine = nouvelle_chaine + caractere
    chaine_actuelle = nouvelle_chaine
  #Initialisation de la tortue
  up()
  goto(200, -200)
  right(180)
  down()
  #Dessiner
  for caractere in chaine_actuelle:
    if caractere == "F":
      forward(avant)
    elif caractere == "+":
      right(angle)
    elif caractere == "-":
      left(angle)

def labyrinthe (nombre_iteration):
  angle= 90
  chaine_actuelle="-YF"
  regles=[["X", "XFX-YF-YF+FX+FX-YF-YFFX+YF+FXFXYF-FX+YF+FXFX+YF-FXYF-YF-FX+FX+YFYF-]"], ["Y", "+FXFX-YF-YF+FX+FXYF+FX-YFYF-FX-YF+FXYFYF-FX-YFFX+FX+YF-YF+FX+FX+YFY"]]
  #Generer la chaine
  for i in range(nombre_iteration):
    nouvelle_chaine = ""
    for caractere in chaine_actuelle:
      if caractere == regles[0][0]:
        nouvelle_chaine = nouvelle_chaine + regles[0][1]
      elif caractere == regles[1][0]:
        nouvelle_chaine = nouvelle_chaine + regles[1][1]
      else:
        nouvelle_chaine = nouvelle_chaine + caractere
    chaine_actuelle = nouvelle_chaine
  #Initialisation de la tortue
  up()
  goto(0, 0)
  right(180)
  down()
  #Dessiner
  for caractere in chaine_actuelle:
    if caractere == "F" or caractere == "Y" or caractere == "X":
      forward(avant)
    elif caractere == "+":
      right(angle)
    elif caractere == "-":
      left(angle)


#regle : F -> F+F-F-F+F
#generer(3)
#left(test[0][4])
#up()
#goto(test[0][3])
#down()
#niv = 4
#dessiner ()