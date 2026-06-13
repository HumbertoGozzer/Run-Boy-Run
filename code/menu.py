
import pygame.image
from pygame.font import Font
from code.const import WIN_WIDTH, COLOR_ORANGE, MENU_OPTION, COLOR_WHITE, COLOR_GREEN


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/Menu/Menubg.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

        # Fonts preloaded
        self.font_title = pygame.font.SysFont("Lucida Sans Typewriter", 70)
        self.font_option = pygame.font.SysFont("Lucida Sans Typewriter", 50)

    def run(self, ):
        menu_option = 0
        pygame.mixer_music.load('./asset/Songs/Musicmenu.mp3')
        pygame.mixer_music.play(-1)
        while True:

            self.window.blit(self.surf, self.rect)


            # Draw Title
            pos_y = 70
            for char in ["THE", "FALL","OF", "CITY"]:
                self.menu_text(self.font_title, char, COLOR_ORANGE, (WIN_WIDTH / 2, pos_y))
                pos_y += 80

            # Options
            for i in range(len(MENU_OPTION)):
                color = COLOR_GREEN if i == menu_option else COLOR_WHITE
                self.menu_text(self.font_option, MENU_OPTION[i], color, (WIN_WIDTH / 2, 550 + 60 * i))
            pygame.display.flip()

            # Check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit() # Close Window
                    quit() # End pygame

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN: # DOWN KY
                        if menu_option < len(MENU_OPTION) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0

                    if event.key == pygame.K_UP: # UP KEY
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) - 1

                    if event.key == pygame.K_RETURN: # ENTER
                        return MENU_OPTION[menu_option]




    def menu_text(self, font:Font, text: str, text_color: tuple, text_center_pos: tuple):
        text_surf = font.render(text, True, text_color).convert_alpha()
        text_rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
