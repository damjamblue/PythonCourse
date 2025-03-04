moiGodini = 0
def moiGodini(godina_na_ragjanje, segashna_godina):
    moiGodini=segashna_godina-godina_na_ragjanje
    print("Ti imash", moiGodini, "godini")

godina_na_ragjanje=int(input("Vnesete ja godinata na ragjanje"))
segashna_godina=int(input("Vnesete ja segashnata godina"))

moiGodini(godina_na_ragjanje, segashna_godina)
