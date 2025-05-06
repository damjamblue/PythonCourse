# from turtle import *
#
# def kvadrat(x,y,agol):
#     penup()
#     goto(x, y)
#     pendown()
#     for x in range(0,4):
#         forward(100)
#         left(agol)
#     # penup()
#     # goto(200, 100)
#     # pendown()
#     # for x in range(0,4):
#     #     forward(100)
#     #     left(90)
#     # goto(100, 100)
#     # pendown()
#     # for x in range(0,4):
#     #     forward(100)
#     #     left(90)
#     # goto(100, 200)
#     # pendown()
#     # for x in range(0,4):
#     #     forward(100)
#     #     left(90)
#
#
# kvadrat(200,200,90)
# kvadrat(200,100,90)
# kvadrat(100,100,90)
# kvadrat(100,200,90)
# kvadrat(200,200,45)
#
#
# done()



from turtle import *
def kvadrat(dolzina):
    for x in range(4):
        forward(dolzina)
        right(90)
def podelen_kvadrat():
    for x in range(4):
        kvadrat(100)
        right(90)

podelen_kvadrat()


done()


