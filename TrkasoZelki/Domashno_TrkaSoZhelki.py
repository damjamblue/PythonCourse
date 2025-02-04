from turtle import *
import random

# Prva zhelka
prv_igrach = Turtle()
prv_igrach.shape('turtle')
prv_igrach.color('green')
prv_igrach.penup()
prv_igrach.goto(-100, 200)
# Prva cel
prv_igrach.goto(300, 160)
prv_igrach.pendown()
prv_igrach.circle(40)
prv_igrach.penup()
prv_igrach.goto(-100, 200)

# Vtora zhelka
vtor_igrach = Turtle()
vtor_igrach.shape('turtle')
vtor_igrach.color('blue')
vtor_igrach.penup()
vtor_igrach.goto(-200, -200)
# Vtora cel
vtor_igrach.goto(300, -240)
vtor_igrach.pendown()
vtor_igrach.circle(40)
vtor_igrach.penup()
vtor_igrach.goto(-200, -200)

kocka = [1,2,3,4,5,6]

while True:
    frlena_kocka = random.randint(kocka[0], kocka[len(kocka) - 1])
    prv_igrach.forward(frlena_kocka)

    frlena_kocka = random.randint(kocka[0], kocka[len(kocka) - 1])
    vtor_igrach.forward(frlena_kocka)

    if (prv_igrach.xcor() >= 260):
        print("Prviot igrach e pobednik")
        break
    if (vtor_igrach.xcor() >= 260):
        print("Vtoriot igrach e pobednik")
        break

done()