import pygame, sys
from settings import *
from player import *

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Game")

        self.bullet_group = pygame.sprite.Group()


        self.player = Player(self.screen, 5 ,self.bullet_group)

        
    

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.player.shoot()


            posicion_mouse = pygame.mouse.get_pos()
    
            mouse_x = posicion_mouse[0]
            mouse_y = posicion_mouse[1]

            self.screen.fill("black")
            self.player.update(mouse_x,mouse_y)
            self.bullet_group.update()
            self.bullet_group.draw(self.screen)

            pygame.display.update()
            self.clock.tick(FPS) / 1000


if __name__ == "__main__":
    game = Game()
    game.run()

