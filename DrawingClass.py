import pygame
import os

BACKGROUND = pygame.image.load(os.path.join('img', 'background.png'))

class Drawing:
    def __init__(self, window):
        self.window = window

    def drawing(self, game, player, enemies, FPS):
        bg = pygame.transform.scale(BACKGROUND, (800, 600))
        self.window.blit(bg, (0, 0))

        for enemy in enemies[:]:
            enemy.draw(self.window)

        player.draw(self.window)
        game.draw_HUD()

        pygame.display.update()