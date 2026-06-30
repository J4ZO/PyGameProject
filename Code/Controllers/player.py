import pygame
import math
from .bullet import *
from .sprites import *

class Player(pygame.sprite.Sprite):
    def __init__(self, screen, speed, b_group):
        super().__init__()
        self.screen = screen
        self.speed = speed
        self.original_image = pygame.image.load("Images/ship_1.png")

        self.image = self.original_image

        self.rect = self.image.get_rect()
        self.rect.center = pygame.Vector2(self.screen.get_width() / 2, self.screen.get_height() / 2)
        self.direction = pygame.Vector2(0, 0)

        self.health = 100
        self.is_dead = False


        self.bullet_group = b_group

        self.bullet_image = pygame.image.load("Images/shot.png")

        path = "Images/dead.png"
        self.sheet_dead = Sprites(path,48,48,7)

        self.sprite_dead = self.sheet_dead.get_frames()

        self.current_sprite = 0

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
    
    def rotate(self, x_value,y_value):
        x = x_value
        y = y_value
        distancex = self.rect.centerx- x
        distancey = self.rect.centery - y
        angle = math.degrees(math.atan2(distancex, distancey))

        self.image = pygame.transform.rotate(self.original_image, angle)

        self.rect = self.image.get_rect(center = self.rect.center)

    def update(self, x_value,y_value):
        if not self.is_dead:
            self.input()
            self.move()
            self.rotate(x_value,y_value)

        self.draw()



    def draw(self):
        self.screen.blit(self.image, self.rect )
    
    # Shoot
    def shoot(self, mouse_x,mouse_y):
        bullet = Bullet(self.rect.center , self.bullet_image, mouse_x,mouse_y)
        self.bullet_group.add(bullet)

    def get_player_position(self):
        return self.rect.center

    def take_damage(self,damage):
        self.health -= damage
        print(self.health)
        if self.health <= 0:
            self.is_dead  = True

    def get_player_dead(self):
        return self.is_dead
    

    def animated_death(self):
        if self.current_sprite < len(self.sprite_dead):
            self.image = self.sprite_dead[int(self.current_sprite)]
            self.current_sprite += 0.2
        else:
            self.kill()    
