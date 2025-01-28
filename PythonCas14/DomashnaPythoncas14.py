a = int(input("Vnesete go prviot broj"))
b = int(input("Vnesete go vtoriot broj"))

for x in range(a,b):
        if(x == a):
                print(a)
        elif(a < b):
                a = a * 3
                if(a<=b):
                        print(a)