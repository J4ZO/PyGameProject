class ImageMenu():
    def __init__(self, image, pos,screen):
        self.image = image
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))

        screen.blit(self.image, self.rect)