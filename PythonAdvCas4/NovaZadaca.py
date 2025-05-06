from turtle import *
def kvadrat(dolzina):
    for x in range(0,4):
        forward(dolzina)
        left(90)
def podelen_kvadrat():
    for x in range(0,4):
        kvadrat(100)
        right(90)

podelen_kvadrat()
right(45)
podelen_kvadrat()

done()