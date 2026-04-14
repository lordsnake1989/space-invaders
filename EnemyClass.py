import os
import pygame
import random
import math

from ShipClass import Ship
from BulletClass import Bullet


def cargar_imagen_segura(ruta, size, color):
    if os.path.exists(ruta):
        img = pygame.image.load(ruta)
        if pygame.display.get_surface() is not None:
            img = img.convert_alpha()
        return pygame.transform.scale(img, size)

    surf = pygame.Surface(size, pygame.SRCALPHA)
    pygame.draw.rect(surf, color, (0, 0, size[0], size[1]), border_radius=6)
    return surf


RED_SHIP = cargar_imagen_segura(
    os.path.join("img", "red_enemy.png"),
    (40, 30),
    (255, 0, 0)
)

BLUE_SHIP = cargar_imagen_segura(
    os.path.join("img", "blue_enemy.png"),
    (40, 30),
    (0, 100, 255)
)

GREEN_SHIP = cargar_imagen_segura(
    os.path.join("img", "green_enemy.png"),
    (40, 30),
    (0, 255, 0)
)

YELLOW_BULLET = cargar_imagen_segura(
    os.path.join("img", "bullet_image.png"),
    (8, 20),
    (255, 255, 0)
)


class Enemy(Ship):
    COLOR_MAP = {
        "red": RED_SHIP,
        "blue": BLUE_SHIP,
        "green": GREEN_SHIP
    }

    def __init__(self, x, y, color, health=20):
        super().__init__(x, y, health)
        self.ship_img = self.COLOR_MAP[color]
        self.bullet_img = YELLOW_BULLET
        self.mask = pygame.mask.from_surface(self.ship_img)

        # Movimiento independiente
        self.base_x = x
        self.vertical_speed = random.uniform(0.6, 1.3)
        self.horizontal_speed = random.uniform(0.02, 0.06)
        self.horizontal_amplitude = random.randint(20, 55)
        self.wave_offset = random.uniform(0, math.pi * 2)

    def move(self, global_velocity=0):
        # Movimiento vertical
        self.y += self.vertical_speed + global_velocity * 0.15

        # Movimiento lateral independiente
        self.x = self.base_x + math.sin(
            self.y * self.horizontal_speed + self.wave_offset
        ) * self.horizontal_amplitude

    def shoot(self):
        self.cooldown()

        if self.cool_down_counter == 0:
            bullet = Bullet(
                self.x + self.get_width() // 2 - self.bullet_img.get_width() // 2,
                self.y + self.get_height() - 5,
                self.bullet_img
            )
            self.bullets.append(bullet)
            self.cool_down_counter = 1