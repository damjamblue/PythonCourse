class Nastavnik():

    ime = ''
    prezime = ''
    lista_na_predmeti = []
    ucenici = []


    def __init__(self, ime, prezime, lista_na_predmeti, ucenici):
        self.ime = ime
        self.prezime = prezime
        self.lista_na_predmeti = lista_na_predmeti
        self.ucenici = ucenici


    def povekje_predmeti(self, nastavnik1, nastavnik2):
            if len(nastavnik1.lista_na_predmeti) > len(nastavnik2.lista_na_predmeti):
                print(nastavnik1.ime, "predava povekje predmeti.")
            elif len(nastavnik1.lista_na_predmeti) < len(nastavnik2.lista_na_predmeti):
                print(nastavnik2.ime, "predava povekje predmeti.")
            else:
                print("Nastavnicite predavaat ist broj na predmeti.")
    def lista_ucenici(self):
            for ucenik in self.ucenici:
                print(ucenik.ime, ucenik.prezime, ucenik.lista_na_ocenki)

    def podatoci_ucenik(self, ime_na_ucenik):
        for ucenik in self.ucenici:
            if ucenik.ime == ime_na_ucenik:
                print('Podatoci za ucenikot')
                print(ucenik.ime, ucenik.prezime, ucenik.lista_na_ocenki, ucenik.prosek())
class Uchenik():

    ime = ''
    prezime = ''
    oddelenie = 0
    lista_na_ocenki = []

    def __init__(self, ime, prezime, oddelenie, lista_na_ocenki):
        self.ime = ime
        self.prezime = prezime
        self.oddelenie = oddelenie
        self.lista_na_ocenki = lista_na_ocenki

    def prosek(self):
        prosekot=0

        for x in range(len(self.lista_na_ocenki)):
            prosekot = (prosekot + self.lista_na_ocenki[x])/len(self.lista_na_ocenki)
            print('lista prosek check:',len(self.lista_na_ocenki))
        if (len(self.lista_na_ocenki) != 0):
            print(prosekot)
        else:
            print('Ucenikot nema oceni')



nikola=Uchenik("Nikola","",4,[4, 5, 3, 4])
nikola.prosek()

stefan=Uchenik("Stefan","Vladimirov",7,[4, 3, 5, 3])
stefan.prosek()

damjan = Uchenik("Damjan","Topalov",5,[5, 5, 5, 5])

damjan.prosek()

boris = Nastavnik(ime='Boris', prezime='Nikolovski',
                  lista_na_predmeti=["python", 'htmlcss'], ucenici=[damjan,stefan,nikola])

ana = Nastavnik(ime='Ana', prezime='Angelova',
                lista_na_predmeti=['graficki dizajn','javascript'], ucenici=[stefan, damjan])

boris.lista_ucenici()
ana.lista_ucenici()

boris.podatoci_ucenik('Nikola')
