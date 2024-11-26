import random

food1 = input("hrana 1")
food2 = input("hrana 2")
food3 = input("hrana 3")

# 1 nacin
foods = [food1, food2, food3]
print(foods)


rndbr1= random.randint(0, len(foods)-1)

game1 = input("game 1")
game2 = input("game 2")
game3 = input("game 3")
games = []
games.append(game1)
games.append(game1)
games.append(game1)
rndbr2= random.randint(0, len(games)-1)
print(foods[rndbr1])
print(games[rndbr2])


