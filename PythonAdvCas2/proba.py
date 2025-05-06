def funkcja(lista1):
    for x in range(0, len(lista1)):
        print(abs(lista1[x]))
        if(x==789):
            break
lista = []
for x in range(1, 1000):
    broj = int(input('vnesi broj'))
    if broj != 789:
        lista.append(broj)
    else:
        funkcja(lista)
print(lista)