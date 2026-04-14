import os
import pygame
from pygame import mixer

pygame.init()
mixer.init()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
audio_path = os.path.join(BASE_DIR, "sounds", "explosion.wav")

print("Probando audio desde:", audio_path)

sonido = mixer.Sound(audio_path)
sonido.set_volume(1.0)
sonido.play()

pygame.time.delay(3000)

pygame.quit()