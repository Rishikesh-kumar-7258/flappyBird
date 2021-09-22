import pygame

from pygame.transform import scale

from States.basestate import Base

from constants import *

class Countdown(Base):

    def __init__(self):
        super().__init__()

        self.largeFont = pygame.font.SysFont("Comic sans MS", 100)
        self.MediumFont = pygame.font.SysFont("Comic sans MS", 36)
        self.count = 4
    
    def render(self): 

        count = self.largeFont.render(str(int(self.count)), True, WHITE, BGC)
        countRect = count.get_rect()
        countRect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT // 2)

        txt = self.MediumFont.render("Press space to play", True, BLUE, BGC)
        textRect = txt.get_rect()
        textRect.center = (WINDOW_WIDTH //2 , WINDOW_HEIGHT // 2 + 200)
        SCREEN.blit(count, countRect)
        SCREEN.blit(txt, textRect)

        if self.count <= 1 : gStateMachine.change("play")

    def update(self, params):

        self.count -= 0.1
        pygame.time.wait(100)
        self.render()
    
    def enter(self, **params):
        self.count = 4