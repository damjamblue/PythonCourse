class Machka():
    def __init__(self, ime, godini, boja_na_krzno, brzina):
        self.ime = ime
        self.godini = godini
        self.boja_na_krzno = boja_na_krzno
        self.brzina = brzina

    def mjaukanje(self):
        return self.ime + ' vika: Mjau! Mjau!'

    def proveri_brzina(self):
        return self.ime + ' ima brzina ' + str(self.brzina)

    def broj_na_mjaukanje(self):
        broj = int(self.godini)
        for x in range(0, broj):
            print("mjau")

    def pobrza_macka(self, macka2):
        if self.brzina > macka2.brzina:
            print(self.ime, " e pobrza macka.")
        elif self.brzina < macka2.brzina:
            print(macka2.ime, " e pobrza macka.")
        else:
            print("Mackite se so ista brzina")



keti_objekt = Machka("Keti", 2, "bela", 30)
maca_objekt = Machka("Maca", 4,"crna", 20)

print(keti_objekt.proveri_brzina())
print(keti_objekt.mjaukanje())
keti_objekt.broj_na_mjaukanje()

print(maca_objekt.proveri_brzina())
print(maca_objekt.mjaukanje())
maca_objekt.broj_na_mjaukanje()


keti_objekt.pobrza_macka(maca_objekt)
maca_objekt.pobrza_macka(keti_objekt)