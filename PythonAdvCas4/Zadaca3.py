from turtle import *
def shestoagolnik():
    for x in range(0,6):
        forward(100)
        left(60)

shestoagolnik()

def kvadrat(direction):
    for x in range(0,4):
        forward(100)
        direction(90)

kvadrat(left)
forward(100)

kvadrat(right)

def triagolnik():
    for x in range(0,3):
        forward(100)
        right(120)

triagolnik()

done()