class Uchenik():

    ime = ''
    prezime = ''
    oddelenie = 1
    lista_na_ocenki = []


    def __init__(self, ime, prezime, oddelenie, lista_na_ocenki):
        self.ime = ime
        self.prezime = prezime
        self.oddelenie = oddelenie
        self.lista_na_ocenki = lista_na_ocenki

    def prosek(self):
        prosekot=0

        for x in range(len(self.lista_na_ocenki)):
            prosekot = prosekot + self.lista_na_ocenki[x]/len(self.lista_na_ocenki)
        if (len(self.lista_na_ocenki) != 0):
            print(prosekot)
        else:
            print('Ucenikot nema oceni')

ucenik_1=Uchenik("Petko","Stankovski",1,[5, 4, 3, 2])
ucenik_1.prosek()


ucenik_2=Uchenik("Darin","Nikolovski",1,[4, 3, 5, 1])
ucenik_2.prosek()


# def povekje_predmeti_self(self, nastavnik1):
#     if len(self.lista_na_predmeti) > len(nastavnik1.lista_na_predmeti):
#         print(self.ime, " predava povekje predmeti.")
#     elif len(self.lista_na_predmeti) < len(nastavnik1.lista_na_predmeti):
#         print(nastavnik1.ime, " predava povekje predmeti.")
#     else:
#         print("Nastavnicite predavaat ist broj na predmeti.")

# biljanaNastavnik.povekje_predmeti_self(janaNastavnik)