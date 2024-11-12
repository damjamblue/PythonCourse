emagodini = int(input("Vnesi gi godinite na Ema"))
nikolagodini = int(input("Vnesi gi godinite na Nikola"))
andrejgodini = int(input("Vnesi gi godinite na Andrej"))

if(emagodini>nikolagodini and emagodini>andrejgodini):
    print("Ema e najstara")
elif(nikolagodini>emagodini and nikolagodini>andrejgodini):
    print("Nikola e najstar")
elif(andrejgodini>emagodini and andrejgodini>nikolagodini):
    print("Andrej e najstar")
elif(andrejgodini==emagodini and andrejgodini==nikolagodini):
    print("Site se vrsnici")

