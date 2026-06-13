#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.const import WIN_HEIGHT, WIN_WIDTH, MENU_OPTION
from code.level import Level
from code.menu import Menu


class Game:
        def __init__(self):
            pygame.init()
            self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))


        def run(self):

            while True:
                menu = Menu(self.window)
                menu_return = menu.run()

                if menu_return == MENU_OPTION[0]:
                    level = Level(self.window, 'Level1',  menu_return)
                    level.run()
                    pass

                if menu_return == MENU_OPTION[1]:  # Options

                    pass

                if menu_return == MENU_OPTION[2]: # Score

                    pass

                if menu_return == MENU_OPTION[3]: # Credits

                    pass

                elif menu_return == MENU_OPTION[4]: # Exit
                    pygame.quit()
                    quit()
                else:
                    pass






