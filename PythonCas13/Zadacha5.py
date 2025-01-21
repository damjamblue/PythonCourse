from turtle import *

# Naredbi koi kje gi koristime
# penup() - podignuvanje na zhelkata(strelkata) od platnoto za iscrtuvanje
# pendown() - spushtanje na strelkata na platnoto za iscrtuvanje
# goto(x,y) - pridvizhuvanje kon pozicija (x,y) na ekranot
# circle(r) - iscrtuvanje na kruzhnica so radius r
# pensize(width) - postavuvanje na debelinata na linijata koja se iscrtuva
# write(text, font) - ispishuvanje na tekst na ekranot so dadeni informacii za font

speed(0)

# Iscrtuvanje sin krug kako pozadina

penup()
goto(0, -250)
pendown()
color('red')
begin_fill()
circle(250) # kruznica so radius od 250 merni edinici
end_fill()
# postavuvanje na boja na snegulkata

color('white')
pensize(7)

# ciklus za iscrtuvanje na 6 kraka

for i in range(0, 6):
    # postavuvanje na strelkata na pocetna pozicija
    penup()
    goto(0,20)
    pendown()

    # iscrtuvanje na eden krak od snegulkata

    forward(100)
    left(45)
    forward(40)
    forward(-40)
    right(90)
    forward(40)
    forward(-40)
    left(45)
    forward(40)
    right(60)

# Poraka

penup()
hideturtle()
goto(-120, -180)
color("yellow")
write("Среќна нова 2025!", font=("Arial", 20, "bold"))

done()

