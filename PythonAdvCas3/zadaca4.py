samoglaski ='aeiouAEIOU'

def proverka(recenica):
    for bukva in recenica:
        if bukva in samoglaski:
            print(bukva)

vnesete_recenica=input('Vnesete recenica:')
proverka(vnesete_recenica)
