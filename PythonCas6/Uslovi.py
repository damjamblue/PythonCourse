# odgovor = input("Napisha li domashna zadaca")
#
# if odgovor == "da":
#     print("Mozesh da igrash na kompjuter.")


# broj = int(input("Vnesi broj"))
# if broj <= 756:
#     print("Brojot e pomal ili ednakov na 756")
#
# prosek = float(input("Vnesi prosek"))
# if prosek == 5.00:
#     print("Prosekot e ednakov na 5.00")
#
# boja = input("Vnesi boja")
# if boja == "zelena":
#     print("Bojata e zelena")


# godini = int(input("Vnesi godini"))
# if godini >= 18:
#     print("Ti si polnoleten")
# else:
#     print("Ti ne si polnoleten")
#
# broj = int(input("Vnesi broj"))
#
# if broj > 5:
#     broj = broj - 2
# elif broj < 1:


#budget - promenliva nie ja i davame ime
#int -Integer - Cel Broj
#float-decimalen
#Input - Vnes od tastatura
budget = int(input("Vnesi budget"))
iznos = int(input("Vnesi iznos"))

if budget >iznos:
    print("Mozete da pazarite")
else:
    nedostasuvaat =iznos-budget
    print("Nemate dovolno pari da pazarite vi falat:", nedostasuvaat)
