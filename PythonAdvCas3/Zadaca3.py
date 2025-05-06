vkupno = 0
broevi = []
dolzina_na_lista =0
def lista(lista_na_broevi):
    zbir = 0
    for x in lista_na_broevi:
        zbir = x + zbir
        dolzina(lista_na_broevi)
    vkupno=zbir/dolzina_na_lista
    print(vkupno)
def vnesuvanje():
    while True:
        broj=int(input('Vnesete broevi,za kraj vneste 0'))
        broevi.append(broj)
        if(broj ==0):
            break
def dolzina(lista):
    dolzina=0
    for i in lista:
        dolzina+=1
dolzina_na_lista=dolzina

vnesuvanje()
lista(broevi)
