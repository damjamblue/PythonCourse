niza = []

def niza1():
    while True:
        broj = int(input("Vnesete broj"))
        niza.append(broj)
        if broj==789:
            for x in niza:
                if(x!=789):
                    print(abs(x))
            break


niza1()
