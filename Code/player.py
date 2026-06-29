import pygame
from bullet import *

class Player(pygame.sprite.Sprite):
    def __init__(self, screen, speed, b_group):
        super().__init__()
        self.screen = screen
        self.speed = speed

        self.image = pygame.image.load("Images/ship_1.png")
        self.rect = self.image.get_rect()
        self.rect.center = pygame.Vector2(self.screen.get_width() / 2, self.screen.get_height() / 2)


        self.player_pos = pygame.Vector2(self.screen.get_width() / 2, self.screen.get_height() / 2)
        self.direction = pygame.Vector2(0, 0)

        self.bullet_group = b_group

        self.bullet_image = pygame.image.load("Images/shot.png")

    # Move
    def input(self):
        key = pygame.key.get_pressed()

        # Move
        self.direction.x = 0
        self.direction.y = 0

        if key[pygame.K_w]:
            self.direction.y = -1 
        if key[pygame.K_s]:
            self.direction.y = 1 
        if key[pygame.K_a]:
            self.direction.x = -1 
        if key[pygame.K_d]:
            self.direction.x = 1
        
        if self.direction.magnitude() > 0:
            self.direction = self.direction.normalize()


    def move(self):
        self.rect.move_ip(self.direction.x * self.speed, self.direction.y * self.speed)


    def update(self):
        self.input()
        self.move()
        self.draw()


    def draw(self):
        self.screen.blit(self.image, self.rect )
    
    # Shoot
    def shoot(self):
        bullet = Bullet(self.rect.center , self.bullet_image )
        self.bullet_group.add(bullet)
        print("Bullet group: ")

