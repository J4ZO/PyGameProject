import pygame

class Player:
    def __init__(self, screen):
        self.screen = screen
        self.player_pos = pygame.Vector2(self.screen.get_width() / 2, self.screen.get_height() / 2)
        self.direction = pygame.Vector2(0, 0)

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

        # Shoot


    def move(self, speed, dtime):
        self.player_pos += self.direction * speed * dtime
    
    def draw(self):
        pygame.draw.circle(self.screen, "red", self.player_pos, 20 )

    def move_player(self,speed,dt):
        self.draw()
        self.input()
        self.move(speed,dt)
    
    # Shoot
    
