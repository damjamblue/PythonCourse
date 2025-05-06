def tekst_proveri(tekst,broj_na_karakteri):
       if len(tekst) > int(broj_na_karakteri):
           tekstot = tekst[:int(broj_na_karakteri)]+'...'
           print(tekstot)
       else:
           print(tekst)
vnesen_tekst = input("Vnesete tekst:")
broj_na_karakteri = input("Vnesete kolku sakate da se skrati teksot:")
tekst_proveri(vnesen_tekst,broj_na_karakteri)