import pygame, sys
from settings import *
from player import *

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Game")

        self.dt = 0
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

        

            self.screen.fill("black")
            self.player.update()
            self.bullet_group.update()
            self.bullet_group.draw(self.screen)

            pygame.display.update()
            self.dt = self.clock.tick(FPS) / 1000


if __name__ == "__main__":
    game = Game()
    game.run()

