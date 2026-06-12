#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.background import Background
from code.const import WIN_HEIGHT
from code.player import Player


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0,0)):
        list_bg = []
        match entity_name:
            case 'onda1':
                list_bg = [Background('Background/onda1', position)]

                return list_bg

            case 'onda2':
                list_bg = [Background('Background/onda2', position)]

                return list_bg

            case 'onda3':
                list_bg = [Background('Background/onda3', position)]

                return list_bg

            case 'bossfight':
                list_bg  = [Background('Background/bossfight', position)]

                return list_bg

            case 'Player':
                return [Player('Soldier/idle', position=(10, WIN_HEIGHT / 2 ))]
            case _:
                
                return []
