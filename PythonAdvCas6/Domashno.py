class Nastavnik():

    ime = ''
    prezime = ''
    lista_na_predmeti = []


    def __init__(self, ime, prezime, lista_na_predmeti):
        self.ime = ime
        self.prezime = prezime
        self.lista_na_predmeti = lista_na_predmeti


    def povekje_predmeti(self, nastavnik1, nastavnik2):
            if len(nastavnik1.lista_na_predmeti) > len(nastavnik2.lista_na_predmeti):
                print(nastavnik1.ime, "predava povekje predmeti.")
            elif len(nastavnik1.lista_na_predmeti) < len(nastavnik2.lista_na_predmeti):
                print(nastavnik2.ime, "predava povekje predmeti.")
            else:
                print("Nastavnicite predavaat ist broj na predmeti.")



biljanaNastavnik = Nastavnik("Biljana","Denkova",["makedonski", "likovno", "istorija"])
janaNastavnik = Nastavnik("Jana","Stefanovska",["hemija", "biologija", "fizika", "matematika"])
anetaNastavnik = Nastavnik("Aneta","Kostevska",["gimnastika", "origami", "velosipedizam", "shah", "literatura", "matematika"])


print (biljanaNastavnik.ime, biljanaNastavnik.prezime)
print (janaNastavnik.ime, janaNastavnik.prezime)
print (anetaNastavnik.ime, anetaNastavnik.prezime)

janaNastavnik.povekje_predmeti(biljanaNastavnik, anetaNastavnik)




