import pygame

from States.basestate import Base
from classes.pillarClass import Pillar
from constants import *

class Play(Base):

    def __init__(self):
        super().__init__()

        self.pillars = []
        self.current = Pillar()
        self.pillars.append(self.current)

        self.gap = 200

        #setting up background
        self.upper = pygame.image.load("./Images/upper.png")
        self.lower = pygame.image.load("./Images/lower.png")
        self.upper_rect = self.upper.get_rect()
        self.lower_rect = self.lower.get_rect()
        self.upper_rect2 = self.upper.get_rect()
        self.lower_rect2 = self.lower.get_rect()

        self.upper_rect.x = 0
        self.upper_rect.y = 0
        self.lower_rect.x = 0
        self.lower_rect.y = WINDOW_HEIGHT - 40
        self.upper_rect2.x = WINDOW_WIDTH
        self.upper_rect2.y = 0
        self.lower_rect2.x = WINDOW_WIDTH
        self.lower_rect2.y = WINDOW_HEIGHT - 40

        self.lower_speed = 5
        self.upper_speed = 3

    
    def render(self): 

        for pillar in self.pillars:
            pillar.render()

        SCREEN.blit(self.upper, self.upper_rect)
        SCREEN.blit(self.lower, self.lower_rect)
        SCREEN.blit(self.upper, self.upper_rect2)
        SCREEN.blit(self.lower, self.lower_rect2)

    def update(self):

        self.lower_rect.x -= self.lower_speed
        self.lower_rect2.x -= self.lower_speed
        self.upper_rect.x -= self.upper_speed
        self.upper_rect2.x -= self.upper_speed

        self.re_render(self.upper_rect)
        self.re_render(self.upper_rect2)
        self.re_render(self.lower_rect)
        self.re_render(self.lower_rect2)


        if self.current.x <= WINDOW_WIDTH - self.gap - self.current.width:
            self.current = Pillar()
            self.pillars.append(self.current)
        
        for pillar in self.pillars:
            if pillar.x < -pillar.width - self.gap : self.pillars = self.pillars[1:]

        for pillar in self.pillars:
            pillar.update()

        self.render()
    
    def enter(self):
        self.pillars = []
        self.current = Pillar()
        self.pillars.append(self.current)
    
    def re_render(self, img):
        if img.x <= -WINDOW_WIDTH :
            img.x = WINDOW_WIDTH