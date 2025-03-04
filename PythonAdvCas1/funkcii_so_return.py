import turtle
from turtle import *

# def pozdrav(ime):
#     zdravo ="Zdravo " + ime
#     return zdravo
#
# pozdrav_nino = pozdrav("nino")
# pozdrav_martina = pozdrav("martina")
#
# print(pozdrav_nino)
# print(pozdrav_martina)



# def vnesi_broj():
#     broj=input("vnesi broj")
#     print(broj)
# vnesi_broj()

# def proveri_broj(broj):
#     if(broj>100):
#         print("brojot e pogolem od 100")
#     else:
#         print("brojot e pomal od 100")
# proveri_broj(int(input("Vnesete broj")))

# def proveri_broj2():
#     broj=int(input("Vnesete broj"))
#     if(broj>100):
#         print("brojot e pogolem od 100")
#     else:
#         print("brojot e pomal od 100")
# proveri_broj2()

# def zbir_na_broevi(pocetok, kraj):
#     zbir=0
#     for x in range(pocetok,kraj):
#         zbir=x+zbir
#         print("Vo momentov zbirot e",zbir, "koga pochetok",pocetok,"kraj",kraj)
#     return print(zbir)
# pochetok=int(input("Vnesete broj za pochetok"))
# kraj=int(input("Vnesete broj za kraj"))
# zbir_na_broevi(pochetok,kraj)

from turtle import *


def funkcija(boja, kordinata1,kordinata2):
    color(boja)
    penup()
    goto(kordinata1, kordinata2)
    pendown()
    for x in range(0,4):
        forward(100)
        right(90)


begin_fill()

funkcija('red',200, 100)
end_fill()
begin_fill()
funkcija('blue',450, 100)
end_fill()
begin_fill()
funkcija('green',650, 100)
end_fill()
done()
