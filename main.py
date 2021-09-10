import pygame

from constants import *
from classes.pillarClass import Pillar
from States.playstate import Play
from States.startstate import Start

pygame.init()

STATES = {
    "play" : Play(),
    "start" : Start()
}

gStateMachine.states = STATES
gStateMachine.change("play")

GAME_OVER = False

while not GAME_OVER:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GAME_OVER = True
        
    SCREEN.fill(BGC)
    gStateMachine.update()
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
quit()