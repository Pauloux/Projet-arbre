#On importe la librairie turtle
from turtle import *

#Paramètres généraux
#hideturtle()
#On met la vitesse maximale pour la tortue
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
  assert type(nombre_iteration) == int and nombre_iteration >= 0 and nombre_iteration <= 4
  avant = 200
  epaisseur = 10
  decalage = 100
  angle = 60
  chaine_actuelle = "F++F++F"
  regle = ["F", "F-F++F-F"]
  #Generer la chaine
  for i in range(nombre_iteration):
    avant = avant * 0.37
    epaisseur = epaisseur * 0.6
    decalage = decalage * 1.02
    nouvelle_chaine = ""
    for caractere in chaine_actuelle:
      if caractere == regle[0]:
        nouvelle_chaine = nouvelle_chaine + regle[1]
      else:
        nouvelle_chaine = nouvelle_chaine + caractere
    chaine_actuelle = nouvelle_chaine
  #Initialisation de la tortue
  up()
  goto(-decalage, decalage)
  setheading(0)
  down()
  width(epaisseur)
  #Dessiner
  for caractere in chaine_actuelle:
    if caractere == "F":
      forward(avant)
    elif caractere == "+":
      right(angle)
    elif caractere == "-":
      left(angle)

def arbre_2D (nombre_iteration):
  assert type(nombre_iteration) == int and nombre_iteration >= 0 and nombre_iteration <= 4
  memoire = []
  avant = 200
  epaisseur = 10
  angle = 22.5
  chaine_actuelle = "F"
  regle= ["F", "FF+[+F-F-F]-[-F+F+F]"]
  #Generer la chaine
  for i in range(nombre_iteration):
    avant = avant * 0.4
    epaisseur = epaisseur * 0.7
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
  setheading(90)
  down()
  #Dessiner
  facteur = 1
  for caractere in chaine_actuelle:
    width(epaisseur * facteur)
    if facteur > 0.8:
      color("brown")
    else:
      color("green")
    if caractere == "F":
      forward(avant*facteur)
    elif caractere == "+":
      right(angle)
    elif caractere == "-":
      left(angle)
    elif caractere == "[":
      memoire.append([[xcor(), ycor()], heading()])
      facteur = facteur * 0.9
    elif caractere == "]":
      up()
      etat = memoire.pop()
      goto(etat[0])
      setheading(etat[1])
      down()
      facteur = facteur / 0.9


def courbe_de_koch (nombre_iteration):
  assert type(nombre_iteration) == int and nombre_iteration >= 0 and nombre_iteration <= 5
  avant=200
  epaisseur = 10
  decalage = 100
  angle= 90
  chaine_actuelle="F"
  regle=["F","F+F-F-F+F"]
  #Generer la chaine
  for i in range(nombre_iteration):
    avant = avant * 0.4
    epaisseur = epaisseur * 0.6
    decalage = decalage * 1.2
    nouvelle_chaine = ""
    for caractere in chaine_actuelle:
      if caractere == regle[0]:
        nouvelle_chaine = nouvelle_chaine + regle[1]
      else:
        nouvelle_chaine = nouvelle_chaine + caractere
    chaine_actuelle = nouvelle_chaine
  #Initialisation de la tortue
  up()
  goto(decalage, -decalage)
  setheading(180)
  down()
  width(epaisseur)
  #Dessiner
  for caractere in chaine_actuelle:
    if caractere == "F":
      forward(avant)
    elif caractere == "+":
      right(angle)
    elif caractere == "-":
      left(angle)