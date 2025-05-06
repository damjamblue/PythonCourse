class Mache():

    ime = ''
    godini = 0
    boja_na_krzno = ''
    sopstvenik = ''


    def __init__(self, ime, godini, boja_na_krzno, sopstvenik):
        self.ime = ime
        self.godini = godini
        self.boja_na_krzno = boja_na_krzno
        self.sopstvenik = sopstvenik

    def meow(self):
        for x in range(self.godini):
            print("Meow", x)

    def __str__(self):
        return f'Ime:{self.ime}, godini: {self.godini}, boja na krzno: {self.boja_na_krzno}, sopstvenik {self.sopstvenik}'

    def pedigre(self):
        print("Pedigre za maceto", self.ime, "e slednoto:")
        print("Godini:", self.godini)
        print("Boja na krzno:",self.boja_na_krzno)



moe_mache = Mache("Maza",4,"belo so sivo","Angelka")
print(moe_mache.ime)
moe_mache.meow()

moe_mache2 = Mache(ime="Meda",godini=5, boja_na_krzno="kafeno", sopstvenik="Matej")
print(moe_mache2.ime)
moe_mache2.meow()

moe_mache3 = Mache(ime="Belko",godini=2, boja_na_krzno="belo", sopstvenik="Ana")
print(moe_mache2.ime)
moe_mache3.meow()

print(moe_mache)

moe_mache2.pedigre()

moe_mache4 = Mache(ime="Crnko", godini=1, boja_na_krzno="crno", sopstvenik="Filip")
print(moe_mache4)