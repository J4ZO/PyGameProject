from random import randint

import pygame
from enemy import *
from settings import *

class Spawn():
    def __init__(self, enemy_group,b_group):
        self.image_enemy = pygame.image.load("Images/enemy_ship.png")
        self.speed_enemy = 3

        self.bullet_group = b_group
        self.enemy_group = enemy_group

        self.positions = [(WIDTH / 2, - 100) , (WIDTH / 2, HEIGHT + 100) , (-100, HEIGHT / 2) , (WIDTH + 100, HEIGHT / 2)]
    

    def spawn(self,target_player):
        index = randint(0, len(self.positions) - 1)

        enemy = Enemy(target_player, self.image_enemy, self.bullet_group, self.speed_enemy, self.positions[index])
        self.enemy_group.add(enemy)
        
