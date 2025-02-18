from turtle import *
import random

dolzina_na_chekor = 20
lista_na_prepreki = [-100, -50, 50]

# Prva zhelka
prv_igrach = Turtle()
prv_igrach.shape('turtle')
prv_igrach.color('green')
prv_igrach.penup()
prv_igrach.goto(-200, 100)
# Prva cel
prv_igrach.goto(300, 60)
prv_igrach.pendown()
prv_igrach.circle(40)
# Prechka
for i in lista_na_prepreki:
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
# Vrakanje na zelkata na startnata linija
prv_igrach.penup()
prv_igrach.goto(-200, 100)
prv_igrach.pendown()

# Vtora zhelka
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
vtor_igrach.goto(-200, -100)
vtor_igrach.pendown()

# vtora Prechka
vtor_igrach.penup()
vtor_igrach.goto(-100, -130)
vtor_igrach.pendown()
vtor_igrach.forward(10)
vtor_igrach.left(90)
vtor_igrach.forward(60)
vtor_igrach.left(90)
vtor_igrach.forward(10)
vtor_igrach.left(90)
vtor_igrach.forward(60)
vtor_igrach.left(90)

# Vrakanje na zelkata na startnata linija
vtor_igrach.penup()
vtor_igrach.goto(-200, -100)
vtor_igrach.pendown()

# Kockata da ja pretstavime so site vrednosti koi moze da gi ima
kocka = [1,2,3,4,5,6]
prv_igrach_vrednost = 0
vtor_igrach_vrednost = 0

#Usporuvanje
prv_igrach_usporuvanja = 0

# Nacin 1 - so goto, treba da gi pamtime site prethodni vrednosti
# for i in range(0,20):
#     input("Prv igrach mozhe da pritisne ENTER za da ja svrti kockata")
#     prv_igrach_vrednost += random.choice(kocka)
#     print(prv_igrach_vrednost)
#     prv_igrach.goto(prv_igrach_vrednost - 200, 100)
#     input("Vtor igrach mozhe da pritisne ENTER za da ja svrti kockata")
#     vtor_igrach_vrednost += random.choice(kocka)
#     print(vtor_igrach_vrednost)
#     vtor_igrach.goto(vtor_igrach_vrednost - 200, -100)

# Nacin 2 - so forward, treba samo da se dvizi napred kolku sto e kockata frlena
for i in range(0,20):

    input("Prv igrach mozhe da pritisne ENTER za da ja svrti kockata")
    prv_igrach_vrednost = random.choice(kocka)
    print(prv_igrach_vrednost)

    prv_igrach_pridvizuvanje = prv_igrach_vrednost * dolzina_na_chekor
    print(prv_igrach_pridvizuvanje)

brojach_usporuvanja = 0

for j in range(len(lista_na_prepreki)):
    if prv_igrach.xcor() >= lista_na_prepreki[j] and brojach_usporuvanja[j]  == 0:
            prv_igrach_usporuvanja += 1
            print("Prviot igrach e usporen", prv_igrach_usporuvanja, "pati")
            print("Prv igrach pridvizuvanje so usporuvanje", prv_igrach_pridvizuvanje / prv_igrach_usporuvanja)
            prv_igrach.forward(prv_igrach_pridvizuvanje / prv_igrach_usporuvanja)
            brojach_usporuvanja[j] = 1
            break
    else:
        print("Prv igrach pridvizuvanje ")
    if prv_igrach.xcor() >= -100:
        print("Prviot igrach e usporen")
        prv_igrach.forward(prv_igrach_pridvizuvanje / 2)
    else:
        prv_igrach.forward(prv_igrach_pridvizuvanje)

    if prv_igrach.pos() > (300, 100):
        prv_igrach.penup()
        prv_igrach.goto(-200, 200)
        prv_igrach.pendown()
        prv_igrach.write("PRV IGRACH POBEDI!", font=("Arial", 20, "bold"))
        break

    input("Vtor igrach mozhe da pritisne ENTER za da ja svrti kockata")
    vtor_igrach_vrednost = random.choice(kocka)

    print(vtor_igrach_vrednost)
    vtor_igrach.forward(vtor_igrach_vrednost * dolzina_na_chekor)

    vtor_igrach_pridvizuvanje = vtor_igrach_vrednost * dolzina_na_chekor
    print(vtor_igrach_pridvizuvanje)

    if vtor_igrach.xcor() >= -100:
        print("Prviot igrach e usporen")
        vtor_igrach.forward(vtor_igrach_pridvizuvanje / 2)
    else:
        vtor_igrach.forward(vtor_igrach_pridvizuvanje)

    if vtor_igrach.pos() > (300, -100):
        vtor_igrach.penup()
        vtor_igrach.goto(-200, 200)
        vtor_igrach.pendown()
        vtor_igrach.write("VTOR IGRACH POBEDI!", font=("Arial", 20, "bold"))
        break

done()