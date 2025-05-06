
tekst = input("Vnesete tekst:")
def obraten_tekst(tekst):
    for x in reversed(tekst):
        print(x, end="")
#end="" gi redi karakterite vo eden red
obraten_tekst(tekst)


#bunus
def obraten_tekst_bonus(text):
    obraten_text = ""  # Pochni so prazen text
    i = 0  # brojach
    while i < len(text):  # odi po sekoja bukva
        obraten_text = text[i] + obraten_text  # dodavaj ja sekoja bukva na pocheotkot
        i += 1  # odi kon slednata bukva
    return obraten_text

print("\nObraten text:", obraten_tekst_bonus(tekst))