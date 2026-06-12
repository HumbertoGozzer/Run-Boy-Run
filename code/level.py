#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.const import COLOR_WHITE, WIN_HEIGHT
from code.entity import Entity
from code.entityFactory import EntityFactory


class Level:
    def __init__(self, window, name, game_mode):

        self.time_elapsed = 0
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('onda1'))
        self.entity_list.extend(EntityFactory.get_entity('Player'))
    def run(self):

        pygame.mixer_music.load('./asset/Songs/Levelsong.mp3')
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()
        while True:
            tick = clock.tick(60)
            self.time_elapsed += tick

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            for ent in self.entity_list:
                ent.move()

            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)


            # Printed text

            # Linha 1: Mostra o nome da orda e o tempo subindo em tempo real
            self.level_text(14, f'{self.name} - Tempo: {self.time_elapsed / 1000:.1f}s', COLOR_WHITE, (10, 5))

            # Linha 2: Mostra o FPS atual embaixo na tela
            self.level_text(14, f'fps: {clock.get_fps():.0f}', COLOR_WHITE,
                            (10, WIN_HEIGHT - 35))

            # Linha 3: Mostra a contagem de entidades ativas
            self.level_text(14, f'entidades: {len(self.entity_list)}', COLOR_WHITE, (10, WIN_HEIGHT - 20))

            pygame.display.flip()

        pass

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)