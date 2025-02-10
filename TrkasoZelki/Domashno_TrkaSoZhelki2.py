import turtle
from turtle import *

import random

dolzina_na_chekor = 30

# Prva zhelka
prv_igrach = Turtle()
prv_igrach.shape('turtle')
prv_igrach.color('green')
prv_igrach.penup()
prv_igrach.goto(-150, 200) #startna pozicija
# Prva cel
prv_igrach.goto(300, 160) #y=200-40(r)=160, pozicija na krugot/celta
prv_igrach.pendown()
prv_igrach.circle(40)
prv_igrach.penup()
prv_igrach.goto(-200, 200) #start

# Vtora zhelka
vtor_igrach = Turtle()
vtor_igrach.shape('turtle')
vtor_igrach.color('blue')
vtor_igrach.penup()
vtor_igrach.goto(-150, 200)
# Vtora cel
vtor_igrach.goto(300, -40)
vtor_igrach.pendown()
vtor_igrach.circle(40)
vtor_igrach.penup()
vtor_igrach.goto(-200, 0)

# Treta zhelka
tret_igrach = Turtle()
tret_igrach.shape('turtle')
tret_igrach.color('red')
tret_igrach.penup()
tret_igrach.goto(-150, 200)
# Treta cel
tret_igrach.goto(300, -200)
tret_igrach.pendown()
tret_igrach.circle(40)
tret_igrach.penup()
tret_igrach.goto(-200, -160)

#Kockata da ja pretstavime so site vrednosti koi moze da gi ima
kocka = [1,2,3,4,5,6]
prv_igrach_vrednost = 0
vtor_igrach_vrednost = 0
tret_igrach_vrednost = 0

for i in range(0, 30):
    # input("Prv igrach moze da pritisne ENTER za da ja svrti kockata")
    turtle.textinput("Prv IGRAC", "Prv igrach moze da pritisne ENTER za da ja svrti kockata")
    prv_igrach_vrednost = random.choice(kocka)
    print(prv_igrach_vrednost)
    prv_igrach.forward(prv_igrach_vrednost * dolzina_na_chekor)

    if prv_igrach.pos() > (260, 160):
        prv_igrach.penup()
        prv_igrach.goto(-200, 200)
        prv_igrach.pendown()
        prv_igrach.write("PRV IGRACH POBEDI!", font="Ariel")
        break

    # input("Vtor igrach moze da pritisne ENTER za da ja svrti kockata")
    turtle.textinput("Vtor IGRAC", "Vtor igrach moze da pritisne ENTER za da ja svrti kockata")
    vtor_igrach_vrednost = random.choice(kocka)
    print(vtor_igrach_vrednost)
    vtor_igrach.forward(vtor_igrach_vrednost * dolzina_na_chekor)

    if vtor_igrach.pos() > (260, 0):
        vtor_igrach.penup()
        vtor_igrach.goto(-200, 200)
        vtor_igrach.pendown()
        vtor_igrach.write("VTOR IGRACH POBEDI!", font="Ariel")
        break

    # input("Tret igrach moze da pritisne ENTER za da ja svrti kockata")
    turtle.textinput("Tret IGRAC", "Tret igrach moze da pritisne ENTER za da ja svrti kockata")
    tret_igrach_vrednost = random.choice(kocka)
    print(tret_igrach_vrednost)
    tret_igrach.forward(tret_igrach_vrednost * dolzina_na_chekor)

    if tret_igrach.pos() > (260, -160):
        tret_igrach.penup()
        tret_igrach.goto(-200, 200)
        tret_igrach.pendown()
        tret_igrach.write("TRET IGRACH POBEDI!", font="Ariel")
        break

done()