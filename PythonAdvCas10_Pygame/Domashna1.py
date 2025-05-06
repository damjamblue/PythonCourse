import pygame
from pygame.locals import *

pygame.init()

pozicija_na_krug_Y = 266
pozicija_na_krug_X = 275
ekran_pozicija_golemina_X=650
ekran_pozicija_golemina_Y=650
radius = 100

screen = pygame.display.set_mode([ekran_pozicija_golemina_X,ekran_pozicija_golemina_Y])

running = True
while running:
    for event in pygame.event.get():

        if event.type == QUIT:
            running = False

        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False

    screen.fill([19, 252, 3])
    #RGB=R,G,B
    pygame.draw.circle(screen,(255, 0, 0),(pozicija_na_krug_X,pozicija_na_krug_Y), radius)

    pygame.display.flip()

pygame.quit