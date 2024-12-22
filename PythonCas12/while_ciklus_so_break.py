obidi = 0
sitezborovi =''
while obidi < 10:
    obidi += 1
    zbor = input()
    if(len(sitezborovi)>0): #Iva, sitezborovi=0
       sitezborovi += ', '+zbor
    else:
        sitezborovi += zbor
    if zbor == 'kraj':
        print(sitezborovi)
        break

if obidi == 10:
    print('Gi vnesovte site 10 potrebni zborovi')
else:
    print('Vnesovte kraj I ciklusot zavrshi')



