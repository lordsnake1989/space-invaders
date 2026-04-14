import pygame
import sys
import os

from GameClass import Game
from DrawingClass import Drawing
from PantallaNombreClass import PantallaNombre
from MenuPrincipalClass import MenuPrincipal
from MenuPuntajesClass import MenuPuntajes
from MenuAcercaDeClass import MenuAcercaDe

ANCHO = 800
ALTO = 600

pygame.init()
VENTANA = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Space Invaders Hybridge")


def initGame():
    main()


def initPuntaje():
    menu_puntajes = MenuPuntajes(menu_principal)
    menu_puntajes.ejecutar()


def initAbout():
    menu_acerca = MenuAcercaDe(menu_principal)
    menu_acerca.ejecutar()


def menu_principal():
    menu = MenuPrincipal(initGame, initPuntaje, initAbout)
    menu.menu_principal()


def main():
    clock = pygame.time.Clock()
    run = True

    game = Game(60, 1, 3, VENTANA, ANCHO, ALTO)
    drawing = Drawing(VENTANA)

    while run:
        clock.tick(game.FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        game.move_player()
        game.move_enemies()
        game.handle_collisions()

        drawing.drawing(
            game,
            game.player,
            game.enemies,
            game.FPS,
            game.score
        )

        if game.over():
            puntaje = game.score

            if puntaje > game.max_pun:
                try:
                    sound = pygame.mixer.Sound(os.path.join("sounds", "ganar.mp3"))
                    sound.play()
                except Exception:
                    pass

                pantalla = PantallaNombre(puntaje, menu_principal)
                pantalla.ejecutar()
                return
            else:
                menu_principal()
                return


if __name__ == "__main__":
    menu_principal()