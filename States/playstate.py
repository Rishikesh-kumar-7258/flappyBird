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

    
    def render(self): 

        self.current.render()
        for pillar in self.pillars:
            pillar.render()

    def update(self):

        if self.current.x <= WINDOW_WIDTH - self.gap - self.current.width:
            self.current = Pillar()
            self.pillars.append(self.current)
        
        for pillar in self.pillars:
            if pillar.x < -pillar.width : self.pillars = self.pillars[1:]

        for pillar in self.pillars:
            pillar.update()

        self.render()
    
    def enter(self):
        self.pillars = []
        self.current = Pillar()
        self.pillars.append(self.current)