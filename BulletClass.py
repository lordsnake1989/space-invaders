import pygame

class Bullet:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img

    def draw(self, window):
        window.blit(self.img, (self.x, self.y))

    def move(self, speed):
        self.y += speed

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.img.get_width(), self.img.get_height())

    def collision(self, obj):
        return self.get_rect().colliderect(obj.get_rect())