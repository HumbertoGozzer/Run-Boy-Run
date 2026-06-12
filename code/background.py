#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.transform

from code.const import WIN_WIDTH, WIN_HEIGHT
from code.entity import Entity

class Background(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

        self.surf = pygame.transform.scale(self.surf, (WIN_WIDTH, WIN_HEIGHT))

        self.rect = self.surf.get_rect(left=position[0], top=position[1])

    def move(self, ):
        pass
