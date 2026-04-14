import pygame

class Game:
    def __init__(self, font, FPS, lives, window, screen_width, screen_height, bullets=0):
        self.font = font
        self.HEIGHT = screen_height
        self.WIDTH = screen_width
        self.FPS = FPS
        self.lives = lives
        self.level = 1
        self.window = window
        self.clock = pygame.time.Clock()
        self.bullets = bullets

    def draw_HUD(self):
        lives_label = self.font.render(f"Lives: {self.lives}", True, (0, 0, 0))
        bullets_label = self.font.render(f"Bullets: {self.bullets}", True, (0, 0, 0))
        level_label = self.font.render(f"Level: {self.level}", True, (0, 0, 0))

        self.window.blit(lives_label, (10, 10))
        self.window.blit(bullets_label, (10, 50))
        self.window.blit(level_label, (10, 90))