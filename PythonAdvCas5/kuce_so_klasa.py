class Kuche():

    def __init__(self, ime, godini):
        self.ime = ime
        self.godini = godini

    def laenje(self):
        return self.ime + ' vika: Woof! Woof!'
    def spienje(self):
        return self.ime + 'spie: Zzz, Zzz...'

    def hranenje(self):
        return self.ime + ' jade: Om, Nom'

    def godini(self):
        return self.ime + ' ima' + self.godini + 'godini'

    def postaro_kuche(self, kuche_2):
        if self.godini > kuche_2.godini:
            print(self.ime, " e postaro kuche.")
        elif self.godini < kuche_2.godini:
            print(kuche_2.ime, " e postaro kuche.")
        else:
            print("Kuchinjata imaat ist broj na godini")


coco_object = Kuche("coco","4")
luna_object = Kuche("luna", 5)
bela_object = Kuche("bela", 6)
dzeki_object = Kuche("dzeki", 7)
loki = Kuche("loki", 8)
dogi = Kuche("dogi", 9)
pero = Kuche("pero", 10)

print(coco_object.ime)
print(coco_object.laenje())
print(dzeki_object.ime)
print(bela_object.hranenje())
print(luna_object.spienje())
print(loki.ime, loki.godini)
print(pero.ime, pero.godini)
print(dogi.hranenje())

dzeki_object.postaro_kuche(bela_object)
dzeki_object.postaro_kuche(luna_object)
loki.postaro_kuche(dogi)

print(loki.godini)