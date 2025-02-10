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
prv_igrach.goto(-100,100)

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

#Kockata da ja pretstavime so site vrednosti koi moze da gi ima
kocka = [1,2,3,4,5,6]

#Nedopishano

while True:
    #frlena_kocka = random.randint(kocka[0], kocka[len(kocka) - 1])
    #Naredbata random.choice kon koja predavame nekoja lista ni naogja sluchaen element
    #od vrednostite na listata. Bidejki listata gi sodrzhi elementite 1,2,3,4,5,6
    #random.choice sekogas ke ni dade vrednost od 1 do 6
    frlena_kocka = random.choice(kocka)
    prv_igrach.forward(frlena_kocka)

    # frlena_kocka2 = random.randint(kocka[0], kocka[len(kocka) - 1])
    frlena_kocka = random.choice(kocka)
    vtor_igrach.forward(frlena_kocka)

    if (prv_igrach.xcor() >= 260):
        turtle.write('Prviot igrach e pobednik')
        break
    if (vtor_igrach.xcor() >= 260):
        turtle.write('Vtoriot igrach e pobednik')
        break

done()