#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.key
from pygame import Rect

from code.const import PLAYER_SPEED, WIN_WIDTH, WIN_HEIGHT
from code.entity import Entity


class Player(Entity):
    def __init__(self, name: str, position):
        super().__init__(name, position)

        self.name= 'Player'

        # Loading of the animations
        self.animations = {
            'Idle': pygame.image.load('./asset/Soldier/Idle.png').convert_alpha(),
            'Walk': pygame.image.load('./asset/Soldier/Walk.png').convert_alpha(),
            'Run': pygame.image.load('./asset/Soldier/Run.png').convert_alpha(),
            'MeleAttack': pygame.image.load('./asset/Soldier/MeleAttack.png').convert_alpha(),
            'Shot': pygame.image.load('./asset/Soldier/Shot_2.png').convert_alpha(),
            'Dead': pygame.image.load('./asset/Soldier/Dead.png').convert_alpha()


        }
        # Animation settings and sizes
        self.current_action = 'Idle'
        self.index_frame = 0.0
        self.speed_animation = 0.15
        self.width_frame = 128
        self.height_frame = 128

        self.height_render = 200
        self.hitbox_width = 80
        self.hitbox_height = 120
        self.render_offset_Y = 80

        # Settings (flash red)
        self.is_flashing = False
        self.flash_duration = 0
        self.flash_frames = 10
        self.turned_left = False


        self.rect = Rect(position[0], position[1], self.hitbox_width, self.hitbox_height)
        self.animating()


    def move(self):
        # Logic of death interrupts the movement
        if self.current_action == 'Dead':
            self.animating()
            return

        pressed = pygame.key.get_pressed()
        mouse = pygame.mouse.get_pressed()

        in_moviment = any([pressed[pygame.K_w], pressed[pygame.K_s], pressed[pygame.K_a], pressed[pygame.K_d]])
        speed = PLAYER_SPEED * (1.5 if pressed[pygame.K_LSHIFT] else 1.0)

        # Actions
        if mouse[0]: new_action = 'Shot'
        elif mouse[2]: new_action = 'MeleAttack'
        elif in_moviment: new_action = 'Run' if pressed[pygame.K_LSHIFT] else 'Walk'
        else: new_action = 'Idle'

        # Movements
        if pressed[pygame.K_w]: self.rect.y -= speed
        if pressed[pygame.K_s]: self.rect.y += speed
        if pressed[pygame.K_a]:
            self.rect.x -= speed
            self.turned_left = True
        if pressed[pygame.K_d]:
            self.rect.x += speed
            self.turned_left = False

        # Restart animation when switching actions.
        if new_action != self.current_action:
            self.current_action = new_action
            self.index_frame = 0.0


        # Screen limits
        self.rect.clamp_ip(pygame.Rect(0, 580, WIN_WIDTH, WIN_HEIGHT - 700))
        self.animating()

    def animating(self):

        current_sheet = self.animations[self.current_action]
        total_frames = current_sheet.get_width() // self.width_frame

        if self.current_action == 'Dead' and int(self.index_frame) == total_frames - 1:
            self.index_frame = total_frames - 1

        else:
            self.index_frame += self.speed_animation
            if self.index_frame >= total_frames:
                self.index_frame = 0.0

        position_x_cut = int(self.index_frame) * self.width_frame

        cut = Rect(position_x_cut + 40, 0, 60, self.height_frame)

        original_frame = current_sheet.subsurface(cut)


        self.surf = pygame.transform.scale(original_frame, (self.hitbox_width, self.height_render))

        if self.turned_left:
            self.surf = pygame.transform.flip(self.surf, True, False)

        if self.is_flashing:

            mask = pygame.mask.from_surface(self.surf)
            red_silhouette = mask.to_surface(setcolor=(255, 0, 0, 255), unsetcolor =(0, 0, 0, 0))
            red_silhouette.set_alpha(180)
            self.surf.blit(red_silhouette, (0, 0))
            self.flash_duration -= 1
            if self.flash_duration <= 0: self.is_flashing = False

    def take_damage(self):
        if not self.is_flashing and self.current_action != 'Dead':
            self.is_flashing = True
            self.flash_duration = self.flash_frames



