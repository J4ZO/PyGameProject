import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, player_position,bullet_img):
        super().__init__()
        self.image = bullet_img
        self.rect = self.image.get_rect()
        self.rect.center = player_position

        print("Player position bullet: " , pygame.Vector2(player_position))
        self.direction = pygame.Vector2(pygame.mouse.get_pos())
        self.speed_bullet = 10
    