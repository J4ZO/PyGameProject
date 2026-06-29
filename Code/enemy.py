import pygame
import math
from bullet import *

class Enemy(pygame.sprite.Sprite):
    def __init__(self, target_player, image_enemy, b_group, speed_enemy, enemy_start_position):
        super().__init__()
        self.target = target_player
        self.speed_enemy = speed_enemy
        self.original_image_enemy = image_enemy

        self.image = self.original_image_enemy

        self.rect = self.image.get_rect()
        self.rect.center = enemy_start_position

        self.direction = pygame.Vector2(0, 0)
        
        self.bullet_group = b_group

        self.bullet_image = pygame.image.load("Images/shot.png")
    


    def move(self):
        direction = pygame.Vector2(self.target) - pygame.Vector2(self.rect.center)

        if direction.length() > 0:
            direction = direction.normalize()

        self.rect.center += direction * self.speed_enemy

    def rotate(self):
        x = self.target[0] 
        y = self.target[1] 
        distancex = self.rect.centerx - x
        distancey = self.rect.centery - y

        
        angle = math.degrees(math.atan2(distancex, distancey))

        self.image = pygame.transform.rotate(self.original_image_enemy, angle)

        self.rect = self.image.get_rect(center = self.rect.center)

    def shoot(self):
        bullet = Bullet(self.rect.center , self.bullet_image, self.target.x, self.target.y_y)
        self.bullet_group.add(bullet)

    def kill_enemy(self):
        self.kill()

    def update(self, target_updated):
        self.target = target_updated
        self.move()
        self.rotate()
