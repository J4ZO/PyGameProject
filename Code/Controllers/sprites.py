import pygame

class Sprites:
    def __init__(self, n_image, width, height, count):
        self.sheet = pygame.image.load(n_image)
        self.frames = []

        for i in range(count):
            rect = pygame.Rect(i * width, 0, width, height)
            self.frames.append(self.sheet.subsurface(rect))
        
    
    def get_frames(self):
        return self.frames
