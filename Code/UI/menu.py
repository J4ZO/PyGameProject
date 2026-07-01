import pygame, sys
from .button import *
from .image import *
from settings import *

class Menu:
    def __init__(self, screen, font, on_play, menu_bg):
        self.screen = screen
        self.font = font
        self.on_play = on_play
        self.bg = menu_bg
        self.music_menu = pygame.mixer.music.load(resource_path("Audio/main_menu.wav"))
        pygame.mixer.music.set_volume(1)
        pygame.mixer.music.play(-1)

        self.image_movement = pygame.image.load(resource_path("Images/movement.png"))
        self.image_movement = pygame.transform.scale(self.image_movement, (349, 180))

        self.image_shoot = pygame.image.load(resource_path("Images/shoot.png"))
        self.image_shoot = pygame.transform.scale(self.image_shoot, (217, 180))

    def main_menu(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if play_button.checkForInput(position_mouse):
                        self.on_play()
                    if quit_button.checkForInput(position_mouse):
                        pygame.quit()
                        sys.exit()

            self.screen.blit(self.bg, (0, 0)) 

            position_mouse = pygame.mouse.get_pos()
            menu_text = self.get_font(self.font,100).render("MAIN MENU", True, "#ffffff")
            menu_rect = menu_text.get_rect(center =(640,100))

            play_button = Button(pygame.image.load(resource_path("Images/bg_button.png")), (640, 250), "PLAY", self.get_font(self.font, 75), "#ffffff", "#CDECFF")
            quit_button = Button(pygame.image.load(resource_path("Images/bg_button.png")), (640, 400), "QUIT", self.get_font(self.font, 75), "#ffffff", "#CDECFF")
        
            ImageMenu(self.image_movement, (300, 500), self.screen)
            ImageMenu(self.image_shoot, (1000, 500), self.screen)

            self.screen.blit(menu_text, menu_rect)

            for button in [play_button, quit_button]:
                button.changeColor(position_mouse)
                button.update(self.screen)

            pygame.display.update()

    def get_font(self,font,size): 
        return pygame.font.Font(font, size)



