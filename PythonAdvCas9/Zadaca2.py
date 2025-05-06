class Lichnosti:
    data_na_ragjanje = ''
    ime = ''
    prezime = ''

    def __init__ (self,data_na_ragjanje,ime,prezime):
        self.data_na_ragjanje = data_na_ragjanje
        self.ime = ime
        self.prezime = prezime

class Avtor(Lichnosti):
    email = ''

    def __init__ (self,data_na_ragjanje,ime,prezime,email):
        super().__init__(data_na_ragjanje,ime,prezime)
        self.data_na_ragjanje = data_na_ragjanje
        self.ime = ime
        self.prezime = prezime
        self.email = email

class Kniga():
    isbn =''
    avtor=''
    naslov = ''
    cena = ''
    def __init__(self,isbn, avtor,naslov,cena):
        self.isbn=isbn
        self.avtor=avtor
        self.naslov=naslov
        self.cena=cena

    def pecati(self):
        print('ISBN:', self.isbn)
        print('Avtor:', self.avtor.ime, self.avtor.prezime)
        print('Naslov:', self.naslov)
        print('Cena:', self.cena)

igor = Avtor('13.05.2000','Igor','Filipovski','igor@gmail.com')
kniga = Kniga('12345',igor,'Pepelaska','100')
kniga.pecati()

