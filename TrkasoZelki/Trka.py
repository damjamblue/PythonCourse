import turtle
from turtle import *

import random

# Prva zelka
prv_igrach = Turtle()
prv_igrach.shape('turtle')
prv_igrach.color('green')
prv_igrach.penup()
prv_igrach.goto(-200,100)
# Prva cel

prv_igrach.goto(300,60)
prv_igrach.pendown()
prv_igrach.circle(40)
prv_igrach.penup()
prv_igrach.goto(-200,100)

# Vtora zelka
vtor_igrach = Turtle()
vtor_igrach.shape('turtle')
vtor_igrach.color('blue')
vtor_igrach.penup()
vtor_igrach.goto(-200, -100)

# Vtora cel
vtor_igrach.goto(300, -140)
vtor_igrach.pendown()
vtor_igrach.circle(40)
vtor_igrach.penup()
vtor_igrach.goto(-200,-100)


kocka = [1,2,3,4,5,6]

#Nedopishano

while True:
    frlena_kocka = random.randint(kocka[0], kocka[len(kocka) - 1])
    prv_igrach.forward(frlena_kocka)

    frlena_kocka2 = random.randint(kocka[0], kocka[len(kocka) - 1])
    vtor_igrach.forward(frlena_kocka2)

    if (prv_igrach.xcor() >= 240):
        turtle.write('Igrata zavrshi')
        break
    if (vtor_igrach.xcor() >= 240):
        turtle.write('Igrata zavrshi')
        break



done()