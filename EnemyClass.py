import pygame
import random
from ShipClass import Ship

WIDTH = 800

class Enemy(Ship):
    COLOR = {
        'blue': (0, 0, 255),
        'green': (0, 255, 0),
        'purple': (128, 0, 128)
    }

    def __init__(self, speed, x=50, y=50, color='blue', health=100):
        super().__init__(x, y, health)
        self.speed = speed
        self.width = 50
        self.height = 50

        self.ship_img = pygame.Surface((self.width, self.height))
        self.ship_img.fill(self.COLOR[color])
        self.mask = pygame.mask.from_surface(self.ship_img)

    def draw(self, window):
        window.blit(self.ship_img, (self.x, self.y))

    def move(self):
        self.y += self.speed

    def create(self, amount):
        enemies = []
        for _ in range(amount):
            enemies.append(
                Enemy(
                    self.speed,
                    random.randrange(20, WIDTH - 60),
                    random.randrange(-300, -100),
                    random.choice(['blue', 'green', 'purple'])
                )
            )
        return enemies

    def increase_speed(self):
        self.speed *= 1.02