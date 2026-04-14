import pygame

class Ship:
    COOLDOWN = 20

    def __init__(self, x, y, health=100):
        self.x = x
        self.y = y
        self.health = health
        self.max_health = health

        self.ship_img = None
        self.bullet_img = None
        self.bullets = []
        self.cool_down_counter = 0
        self.mask = None

    def draw(self, window):
        if self.ship_img:
            window.blit(self.ship_img, (self.x, self.y))

        for bullet in self.bullets:
            bullet.draw(window)

    def move_bullets(self, velocity, targets):
        self.cooldown()

        for bullet in self.bullets[:]:
            bullet.move(velocity)

            if bullet.off_screen(800):
                self.bullets.remove(bullet)
                continue

            for obj in targets[:]:
                if bullet.collision(obj):
                    if bullet in self.bullets:
                        self.bullets.remove(bullet)

                    if hasattr(obj, "health"):
                        obj.health -= 20
                    break

    def cooldown(self):
        if self.cool_down_counter >= self.COOLDOWN:
            self.cool_down_counter = 0
        elif self.cool_down_counter > 0:
            self.cool_down_counter += 1

    def shoot(self):
        pass

    def get_width(self):
        return self.ship_img.get_width()

    def get_height(self):
        return self.ship_img.get_height()

    def collision(self, obj):
        if self.mask is None or obj.mask is None:
            return False

        offset_x = int(obj.x - self.x)
        offset_y = int(obj.y - self.y)
        return self.mask.overlap(obj.mask, (offset_x, offset_y)) is not None