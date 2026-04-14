import pygame
import sys
import os
from pygame import mixer

pygame.init()

class MenuPrincipal:
    BLANCO = (255, 255, 255)
    NEGRO = (0, 0, 0)
    ROJO = (255, 0, 0)

    ANCHO = 800
    ALTO = 600
    DIR_IMAGENES = "img"

    def __init__(self, init_game_mtd, init_score_mtd, init_about_mtd):
        self.init_game_mtd = init_game_mtd
        self.init_score_mtd = init_score_mtd
        self.init_about_mtd = init_about_mtd

        self.ventana = pygame.display.set_mode((self.ANCHO, self.ALTO))
        pygame.display.set_caption("Space Invaders")
        self.base_path = os.path.dirname(os.path.abspath(__file__))

        try:
            ruta_musica = os.path.join(self.base_path, "sounds", "background_song.mp3")
            mixer.music.load(ruta_musica)
            mixer.music.play(-1)
        except Exception:
            pass

    def cargar_imagen(self, nombre_archivo):
        ruta = os.path.join(self.base_path, self.DIR_IMAGENES, nombre_archivo)
        return pygame.image.load(ruta).convert_alpha()

    def mostrar_texto(self, texto, font, color, superficie, x, y):
        texto_objeto = font.render(texto, True, color)
        rectangulo_texto = texto_objeto.get_rect()
        rectangulo_texto.center = (x, y)
        superficie.blit(texto_objeto, rectangulo_texto)
        return rectangulo_texto

    def menu_principal(self):
        opciones = ["Iniciar juego", "Puntajes", "Acerca de"]
        opcion_seleccionada = 0
        selector_rect = pygame.Rect(0, 0, 300, 50)

        try:
            fondo = self.cargar_imagen("menu_fondo.jpg")
            fondo = pygame.transform.scale(fondo, (self.ANCHO, self.ALTO))
        except Exception:
            fondo = None

        try:
            imagen = self.cargar_imagen("hybridge.gif")
            imagen = pygame.transform.scale(imagen, (80, 80))
        except Exception:
            imagen = None

        while True:
            if fondo:
                self.ventana.blit(fondo, (0, 0))
            else:
                self.ventana.fill(self.NEGRO)

            self.mostrar_texto("Space Invaders", pygame.font.Font(None, 64), self.BLANCO, self.ventana, self.ANCHO // 2, self.ALTO // 4)
            self.mostrar_texto("Hybridge", pygame.font.Font(None, 36), self.BLANCO, self.ventana, self.ANCHO // 2, self.ALTO // 4 + 40)

            if imagen:
                self.ventana.blit(imagen, (self.ANCHO // 2 - 40, self.ALTO // 4 + 60))

            rectangulos_texto = []
            for i, opcion in enumerate(opciones):
                rect_texto = self.mostrar_texto(
                    opcion,
                    pygame.font.Font(None, 32),
                    self.BLANCO,
                    self.ventana,
                    self.ANCHO // 2,
                    self.ALTO // 4 + 90 * (i + 1) + 100
                )
                rectangulos_texto.append(rect_texto)

            selector_rect.centerx = self.ANCHO // 2
            selector_rect.centery = rectangulos_texto[opcion_seleccionada].centery - 10

            pygame.draw.rect(self.ventana, self.ROJO, selector_rect, 2)
            pygame.display.update()

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                elif evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_UP:
                        opcion_seleccionada = (opcion_seleccionada - 1) % len(opciones)

                    elif evento.key == pygame.K_DOWN:
                        opcion_seleccionada = (opcion_seleccionada + 1) % len(opciones)

                    elif evento.key == pygame.K_RETURN:
                        opcion_elegida = opciones[opcion_seleccionada].lower()

                        if opcion_elegida == "iniciar juego":
                            print("opción iniciar juego")
                            self.init_game_mtd()
                            return

                        elif opcion_elegida == "puntajes":
                            print("opción puntaje")
                            self.init_score_mtd()
                            return

                        elif opcion_elegida == "acerca de":
                            print("opción acerca de")
                            self.init_about_mtd()
                            return