maxVisina = 122
print("Dobredojdovte vo mojot luna park")
aktivnosti = ["rolerkoster","trambolina","vrteleshka","panoramsko trkalo"]

vnesiVisina = int(input("Vnesi visina"))

if vnesiVisina <= maxVisina:
    aktivnosti.remove("rolerkoster")
    print(aktivnosti)
else:
    print(aktivnosti)
