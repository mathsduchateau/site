from turtle import *

speed(10) #vitesse du tracé: rapide
penup() #lever le crayon
goto(-50,-50) #aller en bas à gauche
pendown() #baisser le crayon
length = 200
for i in range(10): #répéter 10 fois
  color('blue')
  forward(length) #avancer de length pixels
  left(90) #tourner à gauche de 90 degrés
  forward(length)
  left(90)
  length = length - 10
  color('green')
  forward(length)
  left(90)
  forward(length)
  left(90)
  length = length - 10
done() #fini!