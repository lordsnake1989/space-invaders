import pygame
from PlayerClass import Player
from EnemyClass import Enemy
from DrawingClass import Drawing
from GameClass import Game

pygame.init()

WIDTH = 800
HEIGHT = 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders")

FONT = pygame.font.SysFont("comicsans", 30)

def main():
    run = True

    game = Game(FONT, 60, 5, WIN, WIDTH, HEIGHT, bullets=15)
    drawing = Drawing(WIN)

    player = Player(WIDTH // 2 - 20, HEIGHT - 80, 5, 5, 200)
    enemies = Enemy(2).create(5)

    while run:
        game.clock.tick(game.FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        player.move()
        player.cooldown()
        player.create_bullets()
        player.fire()

        game.bullets = len(player.bullets)

        for enemy in enemies[:]:
            enemy.move()

            # si el enemigo sale por abajo, pierde una vida
            if enemy.y > HEIGHT:
                enemies.remove(enemy)
                game.lives -= 1
                continue

            # si toca al jugador, pierde una vida
            if enemy.get_rect().colliderect(player.get_rect()):
                enemies.remove(enemy)
                game.lives -= 1
                continue

            # si el jugador le pega, se elimina el enemigo
            if player.hit(enemy):
                enemies.remove(enemy)
                continue

        while len(enemies) < 5:
            enemies.extend(Enemy(2).create(1))

        drawing.drawing(game, player, enemies, game.FPS)

        if game.lives <= 0:
            # mostrar Game Over antes de cerrar
            WIN.fill((0, 0, 0))
            game_over_label = FONT.render("GAME OVER", True, (255, 255, 255))
            WIN.blit(game_over_label, (WIDTH // 2 - game_over_label.get_width() // 2, HEIGHT // 2))
            pygame.display.update()
            pygame.time.delay(2000)
            run = False

    pygame.quit()

main()