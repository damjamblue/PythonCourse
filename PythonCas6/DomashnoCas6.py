prashanje1 = input("Koja e tretata planeta od nashiot soncev sistem?")
prashanje2 = input("Kolku strani ima mnoguagolnikot?")
prashanje3 = input("Na kolku stepeni vrie vodata?")

tochniOdgovori= 0

if prashanje1.lower() == "treta" or prashanje1 == 3:
    print("Tocen e odgovorot")
    tochniOdgovori=tochniOdgovori+1
else:
    print("Odgovorot ne e tocen")
if prashanje2.lower() == "mnogu":
    print("Tocen e odgovorot")
    tochniOdgovori=tochniOdgovori+1
else:
    print("Odgovorot ne e tocen")
if prashanje3.lower() == "100":
    print("Odgovorot e tocen")
    tochniOdgovori=tochniOdgovori+1
else:
    print("Odgovorot ne e tocen")

print("Imate tochni odgovori:", tochniOdgovori)