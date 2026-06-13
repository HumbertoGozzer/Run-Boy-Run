#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

import pygame


from code.const import COLOR_WHITE, WIN_HEIGHT
from code.entityFactory import EntityFactory


class Level:
    def __init__(self, window, name, game_mode):

        self.time_elapsed = 0
        self.window = window
        self.name = name
        self.game_mode = game_mode

        self.font = pygame.font.SysFont("Lucida Sans Typewriter", 14)

        self.bg_list = EntityFactory.get_entity('onda1')
        self.entity_list = EntityFactory.get_entity('Player')
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
            # Lógica
            for ent in self.entity_list:
                ent.move()

            # Renderização
            self.window.fill((0, 0, 0))
            for bg in self.bg_list:
                self.window.blit(bg.surf, bg.rect)

            for ent in self.entity_list:
                self.window.blit(ent.surf, (ent.rect.x, ent.rect.y - ent.render_offset_Y))
                # Degub hitbox
                pygame.draw.rect(self.window, (255, 0, 0), ent.rect, 2)


            self.level_text(f'{self.name} - Tempo: {self.time_elapsed / 1000:.1f}s', COLOR_WHITE, (10, 5))
            self.level_text(f'fps: {clock.get_fps():.0f}', COLOR_WHITE, (10, WIN_HEIGHT - 35))
            self.level_text(f'entidades: {len(self.entity_list)}', COLOR_WHITE, (10, WIN_HEIGHT - 20))

            pygame.display.flip()



    def level_text(self, text: str, text_color: tuple, text_pos: tuple):
        text_surf = self.font.render(text, True, text_color).convert_alpha()
        self.window.blit(text_surf, text_surf.get_rect(left=text_pos[0], top=text_pos[1]))