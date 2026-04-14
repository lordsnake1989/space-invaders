import os
import pygame

from ShipClass import Ship
from BulletClass import Bullet


def cargar_imagen_segura(ruta, size, color):
    if os.path.exists(ruta):
        img = pygame.image.load(ruta)

        # Solo convertir si ya existe display
        if pygame.display.get_surface() is not None:
            img = img.convert_alpha()

        return pygame.transform.scale(img, size)

    surf = pygame.Surface(size, pygame.SRCALPHA)
    pygame.draw.polygon(
        surf,
        color,
        [(size[0] // 2, 0), (0, size[1]), (size[0], size[1])]
    )
    return surf


PLAYER_IMAGE = cargar_imagen_segura(
    os.path.join("img", "player_image.png"),
    (50, 40),
    (255, 255, 255)
)

BULLET_IMAGE = cargar_imagen_segura(
    os.path.join("img", "bullet_image.png"),
    (8, 20),
    (255, 255, 0)
)


class Player(Ship):
    def __init__(self, x, y, width_limit, height_limit, health=100):
        super().__init__(x, y, health)
        self.ship_img = PLAYER_IMAGE
        self.bullet_img = BULLET_IMAGE
        self.mask = pygame.mask.from_surface(self.ship_img)

        self.speed = 6
        self.bullet_speed = 6
        self.width_limit = width_limit
        self.height_limit = height_limit
        self.max_health = health

    def move(self, keys):
        if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and self.x - self.speed > 0:
            self.x -= self.speed

        if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and self.x + self.speed + self.get_width() < self.width_limit:
            self.x += self.speed

        if (keys[pygame.K_UP] or keys[pygame.K_w]) and self.y - self.speed > 0:
            self.y -= self.speed

        if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and self.y + self.speed + self.get_height() < self.height_limit:
            self.y += self.speed

    def shoot(self):
        self.cooldown()

        if self.cool_down_counter == 0:
            bullet = Bullet(
                self.x + self.get_width() // 2 - self.bullet_img.get_width() // 2,
                self.y,
                self.bullet_img
            )
            self.bullets.append(bullet)
            self.cool_down_counter = 1