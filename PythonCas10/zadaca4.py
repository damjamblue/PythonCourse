import random

sluchaenBingo = random.randint(1,10)

pogodiBroj = int(input("Vnesi broj"))

if sluchaenBingo == pogodiBroj:
    print("Go pogodivte brojot")
else:
    print("Provajte povtorno")