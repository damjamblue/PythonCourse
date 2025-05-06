import turtle
from turtle import * #site nejzini pod biblioteki

import random

dolzina_na_chekor = 30
prv_lista_na_prepreki = [-100, -50, 0, 50]
prv_brojach_prepreki = [0, 0, 0, 0]

vtor_lista_na_ubrzuvanja = [-100, -50, 0, 50]
vtor_brojach_ubrzuvanja = [0,0,0,0]

# Prva zhelka
prv_igrach = Turtle() #turtle object e kreiran na prviot igrach
prv_igrach.shape('turtle')
prv_igrach.color('green')
prv_igrach.penup()
prv_igrach.goto(-200, 100)
# Prva cel
prv_igrach.goto(300, 60) # pozicija na krugot/celta
prv_igrach.pendown()
prv_igrach.circle(40)
# Prechka
for i in prv_lista_na_prepreki:
    prv_igrach.penup()
    prv_igrach.goto(i, 70)
    prv_igrach.pendown()
    prv_igrach.forward(10)
    prv_igrach.left(90)
    prv_igrach.forward(60)
    prv_igrach.left(90)
    prv_igrach.forward(10)
    prv_igrach.left(90)
    prv_igrach.forward(60)
    prv_igrach.left(90)
prv_igrach.penup()
prv_igrach.goto(-200, 100) #start/pochetna pozicija na zhelka
prv_igrach.pendown()

# Vtora zhelka
vtor_igrach = Turtle()
vtor_igrach.shape('turtle')
vtor_igrach.color('blue')
vtor_igrach.penup()
vtor_igrach.goto(-200, 100)
# Vtora cel
vtor_igrach.goto(300, -140)
vtor_igrach.pendown()
vtor_igrach.circle(40)
for i in vtor_lista_na_ubrzuvanja:
    vtor_igrach.penup()
    vtor_igrach.goto(i, -120)
    vtor_igrach.pendown()
    vtor_igrach.circle(20)
vtor_igrach.penup()
vtor_igrach.goto(-200, -100)
vtor_igrach.pendown()


# Treta zhelka
tret_igrach = Turtle()
tret_igrach.shape('turtle')
tret_igrach.color('red')
tret_igrach.penup()
tret_igrach.goto(-200, 100)
# Treta cel
tret_igrach.goto(300, -340)
tret_igrach.pendown()
tret_igrach.circle(40)
for i in prv_lista_na_prepreki:
    tret_igrach.penup()
    tret_igrach.goto(i, -330)
    tret_igrach.pendown()
    tret_igrach.forward(10)
    tret_igrach.left(90)
    tret_igrach.forward(60)
    tret_igrach.left(90)
    tret_igrach.forward(10)
    tret_igrach.left(90)
    tret_igrach.forward(60)
    tret_igrach.left(90)
tret_igrach.penup()
tret_igrach.goto(-200, -300)
tret_igrach.pendown()

#Kockata da ja pretstavime so site vrednosti koi moze da gi ima
kocka = [1,2,3]
prv_igrach_vrednost = 0
vtor_igrach_vrednost = 0
tret_igrach_vrednost = 0

for i in range(0, 30):
    # input("Prv igrach moze da pritisne ENTER za da ja svrti kockata")
    turtle.textinput("Prv IGRAC", "Prv igrach moze da pritisne ENTER za da ja svrti kockata")#Go smenivme od konzola vo turtle window
    prv_igrach_vrednost = random.choice(kocka)
    print(prv_igrach_vrednost)

    prv_igrach_pridvizuvanje = prv_igrach_vrednost * dolzina_na_chekor

    # listata od prechki
    for j in range(len(prv_lista_na_prepreki)):
        if prv_igrach.xcor() >= prv_lista_na_prepreki[j] and prv_brojach_prepreki[j] == 0:
            print("Prv igrach pridvizuvanje so usporuvanje", prv_igrach_pridvizuvanje / 2)
            prv_igrach_pridvizuvanje = prv_igrach_pridvizuvanje / 2
            prv_brojach_prepreki[j] = 1
            break

    prv_igrach.forward(prv_igrach_pridvizuvanje)

    if prv_igrach.xcor() > 260:
        prv_igrach.penup()
        prv_igrach.goto(-200, 200)
        prv_igrach.pendown()
        prv_igrach.write("PRV IGRACH POBEDI!", font="Ariel")
        break

    # input("Vtor igrach moze da pritisne ENTER za da ja svrti kockata")
    turtle.textinput("Vtor IGRAC", "Vtor igrach moze da pritisne ENTER za da ja svrti kockata")
    vtor_igrach_vrednost = random.choice(kocka)
    print(vtor_igrach_vrednost)

    vtor_igrach_pridvizuvanje = vtor_igrach_vrednost * dolzina_na_chekor

    # listata od ubrzuvanja
    for j in range(len(vtor_lista_na_ubrzuvanja)):
        if prv_igrach.xcor() >= vtor_lista_na_ubrzuvanja[j] and vtor_brojach_ubrzuvanja[j] == 0:
            print("Vtor igrach pridvizuvanje so ubrzuvanje", prv_igrach_pridvizuvanje * 2)
            prv_igrach_pridvizuvanje = prv_igrach_pridvizuvanje * 2
            vtor_brojach_ubrzuvanja[j] = 1
            break

    vtor_igrach.forward(vtor_igrach_pridvizuvanje)


    if vtor_igrach.xcor() > 260:  #x sekogash e isto, visinata y e razlichna
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

    if tret_igrach.xcor() > 260:
        tret_igrach.penup()
        tret_igrach.goto(-200, 200)
        tret_igrach.pendown()
        tret_igrach.write("TRET IGRACH POBEDI!", font="Ariel")
        break

done()