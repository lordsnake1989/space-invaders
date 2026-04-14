import os
import random
import pygame

from PlayerClass import Player
from EnemyClass import Enemy

class Game:
    def __init__(self, FPS, level, lives, window, screen_width, screen_height):
        self.FPS = FPS
        self.level = level
        self.lives = lives
        self.window = window
        self.screen_width = screen_width
        self.screen_height = screen_height

        self.score = 0
        self.max_pun = self.cargar_max_puntaje()

        self.player = Player(
            x=screen_width // 2 - 25,
            y=screen_height - 90,
            width_limit=screen_width,
            height_limit=screen_height
        )

        self.enemies = []
        self.wave_length = 5
        self.enemy_velocity = 0.8

        self.spawn_wave()

    def ruta_scores(self):
        base_path = os.path.dirname(os.path.abspath(__file__))
        carpeta = os.path.join(base_path, "puntajes")
        os.makedirs(carpeta, exist_ok=True)
        return os.path.join(carpeta, "scores.txt")

    def cargar_max_puntaje(self):
        ruta = self.ruta_scores()
        max_score = 0

        if not os.path.exists(ruta):
            return 0

        try:
            with open(ruta, "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    linea = linea.strip()
                    if not linea:
                        continue

                    partes = linea.split(",")
                    if len(partes) >= 2:
                        try:
                            score = int(partes[-1].strip())
                            max_score = max(max_score, score)
                        except ValueError:
                            pass
        except Exception:
            pass

        return max_score

    def spawn_wave(self):
        self.enemies = []
        colores = ["red", "blue", "green"]

        filas = min(2 + self.level // 2, 5)
        columnas = min(self.wave_length, 8)

        margen_x = 70
        margen_y = 60
        separacion_x = 110
        separacion_y = 85

        for fila in range(filas):
            for col in range(columnas):
                jitter_x = random.randint(-10, 10)
                jitter_y = random.randint(-6, 6)

                x = margen_x + col * separacion_x + jitter_x
                y = margen_y + fila * separacion_y + jitter_y

                x = max(20, min(x, self.screen_width - 60))

                enemigo = Enemy(x, y, random.choice(colores), health=20)
                self.enemies.append(enemigo)

    def move_player(self):
        keys = pygame.key.get_pressed()
        self.player.move(keys)

        if keys[pygame.K_SPACE]:
            self.player.shoot()

        self.player.move_bullets(-self.player.bullet_speed, self.enemies)

    def move_enemies(self):
        if len(self.enemies) == 0:
            self.level += 1
            self.wave_length = min(self.wave_length + 1, 8)

            # Extra: balas del jugador más rápidas por nivel
            self.player.bullet_speed += 1

            # Dificultad gradual
            self.player.speed = min(self.player.speed + 0.2, 9)
            self.enemy_velocity = min(self.enemy_velocity + 0.1, 2.2)

            self.spawn_wave()
            return

        for enemy in self.enemies[:]:
            enemy.move(self.enemy_velocity)

            frecuencia_disparo = max(70, 180 - self.level * 10)
            if random.randrange(0, frecuencia_disparo) == 1:
                enemy.shoot()

            velocidad_bala_enemiga = min(2.8 + self.level * 0.12, 4.2)
            enemy.move_bullets(velocidad_bala_enemiga, [self.player])

            if enemy.y + enemy.get_height() >= self.screen_height:
                self.lives -= 1
                if enemy in self.enemies:
                    self.enemies.remove(enemy)

    def handle_collisions(self):
        for enemy in self.enemies[:]:
            if enemy.health <= 0:
                self.enemies.remove(enemy)
                self.score += 10
                continue

            if enemy.collision(self.player):
                self.player.health -= 20
                self.lives -= 1
                if enemy in self.enemies:
                    self.enemies.remove(enemy)

        if self.player.health < 0:
            self.player.health = 0

    def draw_HUD(self):
        font = pygame.font.SysFont("comicsans", 28)

        texto_vidas = font.render(f"Lives: {self.lives}", True, (255, 255, 255))
        texto_nivel = font.render(f"Level: {self.level}", True, (255, 255, 255))
        texto_bala = font.render(f"Bullet Speed: {self.player.bullet_speed}", True, (255, 255, 255))

        self.window.blit(texto_vidas, (10, 10))
        self.window.blit(texto_nivel, (10, 40))
        self.window.blit(texto_bala, (10, 70))

        pygame.draw.rect(self.window, (255, 0, 0), (10, self.screen_height - 20, 200, 12))
        vida_ancho = int((self.player.health / self.player.max_health) * 200)
        pygame.draw.rect(self.window, (0, 255, 0), (10, self.screen_height - 20, max(0, vida_ancho), 12))

    def over(self):
        return self.lives <= 0 or self.player.health <= 0