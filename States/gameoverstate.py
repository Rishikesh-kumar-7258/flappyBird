import pygame

from States.basestate import Base
from classes.buttonClass import Button
from constants import *

class GameOver(Base):

    def __init__(self):
        super().__init__()

        self.biggerFont = pygame.font.SysFont("Comis sans MS", 72)
        self.smallerFont = pygame.font.SysFont("Comis sans MS", 36)
        self.startbtn = Button(text="Start Again", color2=BLUE)
        self.startbtn.x = WINDOW_WIDTH // 2 - self.startbtn.width // 2
        self.startbtn.y = WINDOW_HEIGHT // 2 + 200

    def render(self):
        message = self.biggerFont.render("Game Over!", True, RED, BGC)
        mRect = message.get_rect()
        mRect.center = (WINDOW_WIDTH //2 , WINDOW_HEIGHT // 2)
        SCREEN.blit(message, mRect)
        self.startbtn.render()

    def update(self, params):

        if self.startbtn.clicked() :
            gStateMachine.change("countdown")

        self.render()