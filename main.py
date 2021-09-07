import pygame

from contants import *

pygame.init()

GAME_OVER = False

while not GAME_OVER:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GAME_OVER = True
        
    

pygame.exit()
exit()