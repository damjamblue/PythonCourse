import pygame
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode([500,500])

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()