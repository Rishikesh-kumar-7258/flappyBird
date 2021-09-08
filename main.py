import pygame

from contants import *
from classes.pillarClass import Pillar

pygame.init()

GAME_OVER = False

demo = Pillar()
demo.render()

while not GAME_OVER:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GAME_OVER = True
        
    SCREEN.fill(BLACK)
    demo.update()
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
quit()