import pygame

class Bullet:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img
        self.mask = pygame.mask.from_surface(self.img)

    def draw(self, window):
        window.blit(self.img, (self.x, self.y))

    def move(self, velocity):
        self.y += velocity

    def off_screen(self, height):
        return not (0 <= self.y <= height)

    def collision(self, obj):
        offset_x = int(obj.x - self.x)
        offset_y = int(obj.y - self.y)
        return self.mask.overlap(obj.mask, (offset_x, offset_y)) is not None