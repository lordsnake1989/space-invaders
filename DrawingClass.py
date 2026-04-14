import os
import pygame

WIDTH = 800
HEIGHT = 600


def cargar_fondo():
    ruta = os.path.join("img", "background.png")
    if os.path.exists(ruta):
        fondo = pygame.image.load(ruta)
        if pygame.display.get_surface() is not None:
            fondo = fondo.convert()
        return pygame.transform.scale(fondo, (WIDTH, HEIGHT))

    fondo = pygame.Surface((WIDTH, HEIGHT))
    fondo.fill((8, 8, 20))
    return fondo


BACKGROUND = cargar_fondo()


class Drawing:
    def __init__(self, window):
        self.window = window
        self.font = pygame.font.SysFont("comicsans", 30)

    def drawing(self, game, player, enemies, FPS, puntos):
        self.window.fill((0, 0, 0))
        self.window.blit(BACKGROUND, (0, 0))

        player.draw(self.window)

        for enemy in enemies:
            enemy.draw(self.window)

        game.draw_HUD()

        shadow = self.font.render(f"Points: {puntos}", True, (255, 255, 255))
        self.window.blit(shadow, (332, 12))

        points_label = self.font.render(f"Points: {puntos}", True, (0, 0, 0))
        self.window.blit(points_label, (330, 10))

        pygame.display.update()