class Pravoagolnik:
    a = ''
    b = ''
    def __init__(self,a,b):
      self.a = a
      self.b = b

    def plostina(self):
        plostina=self.a*self.b
        return  plostina
    def perimetar(self):
        perimetar=2*self.a+2*self.b
        return perimetar



pravoagolnik1=Pravoagolnik(5,4)
pravoagolnik2=Pravoagolnik(6,5)
print(pravoagolnik1.plostina())
print(pravoagolnik1.perimetar())
print(pravoagolnik2.plostina())
print(pravoagolnik2.perimetar())

#
#
#
# class Vozilo:
#     godina_na_proizvodstvo = ''
#     boja = ''
#
#     def __init__ (self,godina_na_proizvodstvo,boja):
#         self.godina_na_proizvodstvo = godina_na_proizvodstvo
#         self.boja = boja
#
# class Avtomobil(Vozilo):
#     proizvoditel = []
#
#     def __init__ (self,godina_na_proizvodstvo,boja,proizvoditel):
#         super().__init__(godina_na_proizvodstvo,boja)
#         self.proizvoditel = proizvoditel
#     def __str__(self):
#         return 'Avtomobil, Godina na proizvodstvo: '+ self.godina_na_proizvodstvo + '\n Boja: ' +self.boja + '\n Proizvoditel: ' + self.proizvoditel
#
# class Avtobus(Vozilo):
#     broj_na_sedishta = ''
#
#     def __init__(self,godina_na_proizvodstvo,boja,broj_na_sedishta):
#         super().__init__(godina_na_proizvodstvo,boja)
#         self.broj_na_sedishta = broj_na_sedishta
#     def __str__(self):
#         return 'Avtobus, Godina na proizvodstvo: '+ self.godina_na_proizvodstvo + '\n Boja: ' +self.boja + '\n Broj na Sedista: '+self.broj_na_sedishta
#
# Corolla = Avtomobil('2016','crvena','Toyota')
# Punto = Avtomobil('2020','zolta','Fiat')
# Man = Avtobus('2020','crvena','50')
# Fas = Avtobus('2017','bela','45')
#
# print(Corolla)
# print(Man)