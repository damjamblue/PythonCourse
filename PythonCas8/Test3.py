import random

films = ['Spiderman','Deadpool','Godzilla','Batman']
games = ['Fortnite','Minecraft','Roblox','Tetris']

films_random = random.randint(0,1)
games_random = random.randint(0,2)

print('Film za gledanje:',films[films_random])
print('Igra za igranje:',games[games_random])