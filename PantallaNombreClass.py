import pygame
import sys
import os

class PantallaNombre:
    BLANCO = (255, 255, 255)
    NEGRO = (0, 0, 0)
    ROJO = (255, 0, 0)
    GRIS = (200, 200, 200)

    ANCHO = 800
    ALTO = 600

    def __init__(self, puntaje, back_mtd):
        self.puntaje = puntaje
        self.back_mtd = back_mtd
        self.nombre = ""
        self.ventana = pygame.display.set_mode((self.ANCHO, self.ALTO))
        pygame.display.set_caption("Nuevo Récord")
        self.base_path = os.path.dirname(os.path.abspath(__file__))

    def guardar_puntaje(self):
        carpeta = os.path.join(self.base_path, "puntajes")
        os.makedirs(carpeta, exist_ok=True)

        ruta_archivo = os.path.join(carpeta, "scores.txt")

        nombre_final = self.nombre.strip()
        if not nombre_final:
            nombre_final = "Jugador"

        with open(ruta_archivo, "a", encoding="utf-8") as archivo:
            archivo.write(f"{nombre_final},{self.puntaje}\n")

    def mostrar_texto(self, texto, font, color, x, y):
        superficie = font.render(texto, True, color)
        rect = superficie.get_rect(center=(x, y))
        self.ventana.blit(superficie, rect)

    def dibujar(self):
        self.ventana.fill(self.NEGRO)

        self.mostrar_texto("¡Nuevo Récord!", pygame.font.Font(None, 60), self.ROJO, self.ANCHO // 2, 120)
        self.mostrar_texto(f"Puntaje: {self.puntaje}", pygame.font.Font(None, 42), self.BLANCO, self.ANCHO // 2, 200)
        self.mostrar_texto("Ingresa tu nombre:", pygame.font.Font(None, 40), self.BLANCO, self.ANCHO // 2, 280)

        caja_rect = pygame.Rect(self.ANCHO // 2 - 200, 330, 400, 60)
        pygame.draw.rect(self.ventana, self.GRIS, caja_rect, 2)

        texto_nombre = pygame.font.Font(None, 42).render(self.nombre, True, self.BLANCO)
        self.ventana.blit(texto_nombre, (caja_rect.x + 10, caja_rect.y + 15))

        self.mostrar_texto("Presiona ENTER para guardar", pygame.font.Font(None, 30), self.BLANCO, self.ANCHO // 2, 450)

        pygame.display.update()

    def ejecutar(self):
        while True:
            self.dibujar()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        self.guardar_puntaje()
                        self.back_mtd()
                        return

                    elif event.key == pygame.K_BACKSPACE:
                        self.nombre = self.nombre[:-1]

                    else:
                        if len(self.nombre) < 15 and event.unicode.isprintable():
                            self.nombre += event.unicode