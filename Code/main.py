import pygame, sys
from settings import *
from Controllers.player import *
from Controllers.spawn import *
from UI.menu import *
from UI.game_over import * 

class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Game")

        self.bullet_group = pygame.sprite.Group()

        self.enemy_group = pygame.sprite.Group()


        self.player = Player(self.screen, 5 ,self.bullet_group)
        self.spawn = Spawn(self.enemy_group, self.bullet_group)
        

        self.spawn_enemy = pygame.USEREVENT + 1
        pygame.time.set_timer(self.spawn_enemy, 500)

        self.font = resource_path("Assets/Pixel Space.ttf")

        self.background = pygame.image.load(resource_path("Images/background.png")).convert()
        self.background = pygame.transform.scale(self.background, (WIDTH, HEIGHT))

        

        self.shoot_sound = pygame.mixer.Sound(resource_path("Audio/LaserShoot.wav"))

        self.menu = Menu(self.screen, self.font, self.run, self.background)
        self.game_over = GameOver(self.screen, self.font, self.restart_values)
    

    def run(self):
        self.battle = pygame.mixer.music.load(resource_path("Audio/battle.wav"))
        pygame.mixer.music.set_volume(0.2)
        pygame.mixer.music.play(-1)

        while True:
            posicion_mouse = pygame.mouse.get_pos()
    
            mouse_x = posicion_mouse[0]
            mouse_y = posicion_mouse[1]


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                if not self.player.get_player_dead():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:
                            self.player.shoot(mouse_x,mouse_y)
                            self.shoot_sound.play()
                    if event.type == self.spawn_enemy:
                        self.spawn.spawn(self.player.get_player_position())

                

            self.screen.blit(self.background, (0, 0)) 
            self.player.update(mouse_x,mouse_y)

            self.bullet_group.update()

            enemy_deaths = pygame.sprite.groupcollide(self.enemy_group,self.bullet_group,False,True)

            for enemy in enemy_deaths:
                enemy.start_death()
            
            self.bullet_group.draw(self.screen)

            if(pygame.sprite.spritecollide(self.player, self.enemy_group, True)):
                self.player.take_damage(20)

            self.enemy_group.update(self.player.get_player_position())
        
            self.enemy_group.draw(self.screen)
            if self.player.get_player_dead():
                self.player.animated_death(self.game_over.game_over)
    
            pygame.display.update()
            self.clock.tick(FPS) / 1000

    def main_menu(self):
        self.menu.main_menu()

    def restart_values(self):
        self.player.reset()

        self.bullet_group.empty()
        self.enemy_group.empty()

        self.run()

if __name__ == "__main__":
    game = Game()
    game.main_menu()

