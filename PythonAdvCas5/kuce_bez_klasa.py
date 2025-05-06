def laenje(ime_na_kucheto):
    return ime_na_kucheto + ' vika: Woof! Woof!'

def spienje(ime_na_kucheto):
    return ime_na_kucheto + 'spie: Zzz, Zzz...'

def hranenje(ime_na_kucheto):
    return ime_na_kucheto + ' jade: Om, Nom'

iminja = ['Dziki','Luna','Bela']
godini = [1, 2, 3]

kuce_index = int(input("Vnesi reden broj na kuce: "))

kuce_ime = iminja[kuce_index]
kuce_godini = godini[kuce_index]

print(laenje(kuce_ime))
print(spienje(kuce_ime))
print(hranenje(kuce_ime))