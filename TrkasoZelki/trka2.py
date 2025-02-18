import turtle
from turtle import *

import random

dolzina_na_chekor = 30

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

# for i in range(0,20):
#     input("Prv igrach moze da pritisne ENTER za da ja svrti kockata")
#     prv_igrach_vrednost = random.choice(kocka)
#     print(prv_igrach_vrednost)
#     input("Vtor igrach moze da pritisne ENTER za da ja svrti kockata")
#     vtor_igrach_vrednost = random.choice(kocka)
#     print(vtor_igrach_vrednost)
#     vtor_igrach.goto(vtor_igrach_vrednost - 200, 100)

#Nacin 2 - so forward, treba samo da se dvizi napred kolku sto e kockata frlena
for i in range(0,30):
    turtle.textinput("Prv IGRAC", "Prv igrach moze da pritisne ENTER za da ja svrti kockata")
    prv_igrach_vrednost = random.choice(kocka)
    print(prv_igrach_vrednost)
    prv_igrach.forward(prv_igrach_vrednost * dolzina_na_chekor)

    turtle.textinput("Votr IGRAC", "Vroe igrach moze da pritisne ENTER za da ja svrti kockata")
    vtor_igrach_vrednost = random.choice(kocka)
    print(vtor_igrach_vrednost)
    vtor_igrach.forward(vtor_igrach_vrednost * dolzina_na_chekor)

    input("Tret igrach moze da pritisne ENTER za da ja svrti kockata")
    tret_igrach_vrednost = random.choice(kocka)
    print(tret_igrach_vrednost)
    tret_igrach.forward(tret_igrach_vrednost * dolzina_na_chekor)

    if prv_igrach.pos() > (300, 100):
        vtor_igrach.forward(vtor_igrach_vrednost * dolzina_na_chekor)

    if prv_igrach.pos() > (300, 100):
        print("Prviot igrach pobedi")
        prv_igrach.goto(-200, 200)
        prv_igrach.pendown()
        prv_igrach.write("VTOR IGRACH POBEDI!", font= "Ariel")
        break
    if vtor_igrach.pos() > (300, 100):
        print("Vtoriot igrach pobedi")
        break


done()