import pygame
import time
import random

WIDTH, HEIGHT = 1333, 900
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

def main():
    is_running = True;

    while is_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
                break

    pygame.quit()
      
if __name__ == "__main__":
    main()


