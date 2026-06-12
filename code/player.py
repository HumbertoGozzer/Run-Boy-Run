#!/usr/bin/python
# -*- coding: utf-8 -*-
from typing import Self
from unittest.mock import ANY

import pygame.key
from pygame import Rect, rect

from code.const import PLAYER_SPEED, WIN_WIDTH, WIN_HEIGHT
from code.entity import Entity


class Player(Entity):
    def __init__(self, name: str, position):
        super().__init__(name, position)

        self.animacoes = {
            'Idle': pygame.image.load('./asset/Soldier/Idle.png').convert_alpha(),
            'Walk': pygame.image.load('./asset/Soldier/Walk.png').convert_alpha(),
            'Run': pygame.image.load('./asset/Soldier/Run.png').convert_alpha(),
            'MeleAttack': pygame.image.load('./asset/Soldier/MeleAttack.png').convert_alpha(),
            'Shot': pygame.image.load('./asset/Soldier/Shot_2.png').convert_alpha(),
            'Dead': pygame.image.load('./asset/Soldier/Dead.png').convert_alpha()


        }

        self.acao_atual = 'Idle'
        self.indice_frame = 0.0
        self.velocidade_animacao = 0.15


        #total_frame = 7
        self.largura_frame = 128
        self.altura_frame = 128

        # Tamanho personagem
        self.largura_render = 200
        self.altura_render = 200

        # Config de dano (Piscar vermelho)
        self.esta_piscando = False
        self.duracao_piscar = 0
        self.frames_piscando = 10

        self.virado_esquerda = False


        soldier_idle = self.surf
        corte = Rect(0,0, self.largura_frame, self.altura_frame)
        self.surf = soldier_idle.subsurface(corte)

        self.rect = Rect(position[0], position[1], self.largura_render, self.altura_render)

        self.animar()


    def move(self):
        if self.acao_atual == 'Dead':
            self.animar()
            return

        pressed_keys = pygame.key.get_pressed()

        mouse_buttons = pygame.mouse.get_pressed()

        nova_acao = 'Idle'

        velocidade = PLAYER_SPEED
        if pressed_keys[pygame.K_LSHIFT] or pressed_keys[pygame.K_RSHIFT]:
            velocidade = PLAYER_SPEED * 1.5
            if any([pressed_keys[pygame.K_w], pressed_keys[pygame.K_s], pressed_keys[pygame.K_a], pressed_keys[pygame.K_d]]):
                nova_acao = 'Run'
        elif any([pressed_keys[pygame.K_w], pressed_keys[pygame.K_s], pressed_keys[pygame.K_a], pressed_keys[pygame.K_d]]):
                nova_acao = 'Walk'

        if mouse_buttons[0]:
            nova_acao = 'Shot'
        elif mouse_buttons[2]:
            nova_acao = 'MeleAttack'

        # Movimentação Utilizando W, A, S, D
        if pressed_keys[pygame.K_w]:
            self.rect.y -= velocidade

        if pressed_keys[pygame.K_s]:
            self.rect.y += velocidade

        if pressed_keys[pygame.K_a]:
            self.rect.x -= velocidade
            self.virado_esquerda = True

        if pressed_keys[pygame.K_d]:
            self.rect.x += velocidade
            self.virado_esquerda = False


        if nova_acao != self.acao_atual:
            self.acao_atual = nova_acao
            self.indice_frame = 0.0

        #Correção de Limites
        if self.rect.left < -60:
            self.rect.left = -60

        if self.rect.right > (WIN_WIDTH + 40):
            self.rect.right = WIN_WIDTH + 40

        if self.rect.top < 560:
            self.rect.top = 560

        if self.rect.bottom > WIN_HEIGHT:
            self.rect.bottom = WIN_HEIGHT

        self.animar()

    def animar(self):
        folha_atual = self.animacoes[self.acao_atual]

        total_frames = folha_atual.get_width() // self.largura_frame

        if self.acao_atual == 'Dead' and int(self.indice_frame) == total_frames - 1:
            self.indice_frame = total_frames - 1

        else:
            self.indice_frame += self.velocidade_animacao
            if self.indice_frame >= total_frames:
                self.indice_frame = 0.0

        posicao_x_corte = int(self.indice_frame) * self.largura_frame

        corte = Rect(posicao_x_corte, 0, self.largura_frame, self.altura_frame)

        frame_original = folha_atual.subsurface(corte)

        self.surf = pygame.transform.scale(frame_original, (self.largura_render, self.altura_render))

        if self.virado_esquerda:
            self.surf = pygame.transform.flip(self.surf, True, False)

        if self.esta_piscando:

            mascara = pygame.mask.from_surface(self.surf)

            silhueta_vermelha = mascara.to_surface(setcolor=(255, 0, 0, 255), unsetcolor =(0, 0, 0, 0))
            silhueta_vermelha.set_alpha(180)

            self.surf.blit(silhueta_vermelha, (0, 0))

            self.duracao_piscar -= 1
            if self.duracao_piscar <= 0:
                self.esta_piscando = False

    def tomar_dano(self):
        if not self.esta_piscando and self.acao_atual != 'Dead':
            self.esta_piscando = True
            self.duracao_piscar = self.frames_piscando



