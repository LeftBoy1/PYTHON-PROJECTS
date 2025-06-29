import pygame
import time

pygame.mixer.init()
pygame.mixer.music.load("F:\\Devansh Gupta\\Python Basic\\PYTHON PROJECTS\\Michael.mp3")
pygame.mixer.music.play()

# wait while the music plays
while pygame.mixer.music.get_busy():
    time.sleep(1)



