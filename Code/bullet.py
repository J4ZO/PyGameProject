import pygame
from settings import *
class Bullet(pygame.sprite.Sprite):
    def __init__(self, player_position,bullet_img, mouse_x, mouse_y):
        super().__init__()
        self.image = bullet_img
        self.rect = self.image.get_rect()
        self.rect.center = player_position
        self.position = pygame.math.Vector2(player_position)

        target = pygame.math.Vector2(mouse_x, mouse_y) 
        self.direction = (target - self.position).normalize()
        self.speed_bullet = 30
    
    def update(self):
        self.position += self.direction * self.speed_bullet
        self.rect.center = self.position

        if self.rect.right < 0 or self.rect.left > WIDTH or self.rect.top > HEIGHT or self.rect.bottom < -HEIGHT: 
            print("killed")
            self.kill()

