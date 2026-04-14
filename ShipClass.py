import pygame

class Ship:
    def __init__(self, x, y, health=100):
        self.x = x
        self.y = y
        self.health = health
        self.ship_img = None
        self.bullet_img = None
        self.bullets = []
        self.fired_bullets = []
        self.cool_down = 20

    def draw(self, window):
        if self.ship_img is not None:
            window.blit(self.ship_img, (self.x, self.y))

    def get_width(self):
        if self.ship_img is not None:
            return self.ship_img.get_width()
        return 0

    def get_height(self):
        if self.ship_img is not None:
            return self.ship_img.get_height()
        return 0

    # 🔥 ESTE ES EL QUE FALTABA
    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.get_width(), self.get_height())