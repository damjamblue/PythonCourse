obidi = 0
while obidi < 100:
    obidi += 1
    zbor = input()
    if zbor == 'kraj':
        break

if obidi == 100:
    print('Vnesovte 100 zborovi')
else:
    print('Vnesovte kraj i ciklusot zavrshi')