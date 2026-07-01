import pygame, sys
from .button import *
from settings import *


class GameOver():
    def __init__(self, screen, font, on_play):
        self.screen = screen
        self.font = font
        self.on_play = on_play
    
    def game_over(self):
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
            
            position_mouse = pygame.mouse.get_pos()
            menu_text = self.get_font(self.font,100).render("GAME OVER", True, "#ffffff")
            menu_rect = menu_text.get_rect(center =(640,250))

            play_button = Button(pygame.image.load(resource_path("Images/bg_button_large.png")), (640, 400), "RESTART", self.get_font(self.font, 75), "#ffffff", "#e80000")
            quit_button = Button(pygame.image.load(resource_path("Images/bg_button.png")), (640, 550), "QUIT", self.get_font(self.font, 75), "#ffffff", "#e80000")

            self.screen.blit(menu_text, menu_rect)

            for button in [play_button, quit_button]:
                button.changeColor(position_mouse)
                button.update(self.screen)

            pygame.display.update()

    def get_font(self,font,size): 
        return pygame.font.Font(font, size)

