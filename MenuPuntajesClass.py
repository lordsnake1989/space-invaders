import pygame
import sys
import os

class MenuPuntajes:
    BLANCO = (255, 255, 255)
    NEGRO = (0, 0, 0)
    GRIS = (200, 200, 200)
    ROJO = (255, 0, 0)

    ANCHO = 800
    ALTO = 600

    def __init__(self, back_mtd):
        self.back_mtd = back_mtd
        self.ventana = pygame.display.set_mode((self.ANCHO, self.ALTO))
        pygame.display.set_caption("Mejores Puntajes")
        self.base_path = os.path.dirname(os.path.abspath(__file__))

    def cargar_puntajes(self, archivo):
        puntajes = []
        ruta_archivo = os.path.join(self.base_path, archivo)

        try:
            with open(ruta_archivo, "r", encoding="utf-8") as file:
                for line in file:
                    line = line.strip()
                    if line:
                        partes = line.split(",")
                        if len(partes) >= 2:
                            nombre = ",".join(partes[:-1]).strip()
                            puntaje = partes[-1].strip()
                            puntajes.append((nombre, int(puntaje)))
        except FileNotFoundError:
            pass
        except Exception as e:
            print(f"Error al leer puntajes: {e}")

        return sorted(puntajes, key=lambda x: x[1], reverse=True)[:5]

    def cargar_imagen(self, nombre_archivo):
        ruta = os.path.join(self.base_path, "img", nombre_archivo)
        return pygame.image.load(ruta).convert_alpha()

    def mostrar_texto(self, texto, font, color, superficie, x, y):
        texto_objeto = font.render(texto, True, color)
        rectangulo_texto = texto_objeto.get_rect()
        rectangulo_texto.center = (x, y)
        superficie.blit(texto_objeto, rectangulo_texto)

    def dibujar_boton(self, texto, font, color, superficie, x, y, ancho, alto):
        pygame.draw.rect(superficie, color, (x, y, ancho, alto))
        self.mostrar_texto(texto, font, self.NEGRO, superficie, x + ancho / 2, y + alto / 2)

    def mostrar_puntajes(self, puntajes):
        self.ventana.fill(self.NEGRO)

        try:
            fondo = self.cargar_imagen("menu_fondo.jpg")
            fondo = pygame.transform.scale(fondo, (self.ANCHO, self.ALTO))
            self.ventana.blit(fondo, (0, 0))
        except Exception:
            pass

        self.mostrar_texto("Mejores Puntajes", pygame.font.Font(None, 48), self.BLANCO, self.ventana, self.ANCHO // 2, 50)
        self.mostrar_texto("Space Invaders Hybridge", pygame.font.Font(None, 36), self.BLANCO, self.ventana, self.ANCHO // 2, 120)

        if not puntajes:
            self.mostrar_texto("Aún no hay registros", pygame.font.Font(None, 36), self.ROJO, self.ventana, self.ANCHO // 2, self.ALTO // 2)
        else:
            y_offset = 250
            for i, (nombre, puntaje) in enumerate(puntajes, 1):
                color_texto = self.BLANCO if i == 1 else self.ROJO
                font_size = 42 if i == 1 else 36
                self.mostrar_texto(f"{i}. {nombre}: {puntaje}", pygame.font.Font(None, font_size), color_texto, self.ventana, self.ANCHO // 2, y_offset)
                y_offset += 60

        self.dibujar_boton("<", pygame.font.Font(None, 36), self.GRIS, self.ventana, 20, 20, 50, 50)
        pygame.display.update()

    def ejecutar(self):
        puntajes = self.cargar_puntajes(os.path.join("puntajes", "scores.txt"))
        self.mostrar_puntajes(puntajes)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        x, y = event.pos
                        if 20 <= x <= 70 and 20 <= y <= 70:
                            self.back_mtd()
                            return