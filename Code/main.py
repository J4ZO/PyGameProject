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
        self.player = Player(self.screen)
    

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

        

            self.screen.fill("black")
            self.player.move_player(1, self.dt)
            pygame.display.flip()
            self.dt = self.clock.tick(FPS)


if __name__ == "__main__":
    game = Game()
    game.run()

