import pygame

from States.basestate import Base
from constants import *

class Start(Base):

    def __init__(self):

        super().__init__()

    
    def render(self) : 
        font = pygame.font.SysFont("Comic sans MS", 72)
        text = font.render("Flappy Bird", True, (255, 255, 255), (0, 0, 0))
        textRect = text.get_rect()

        textRect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)

        SCREEN.blit(text, textRect)

    def update(self):

        self.render()