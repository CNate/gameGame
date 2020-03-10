import pygame
from pygame.constants import *


def handleEvents():
    event = pygame.event.poll()
    if event.type != pygame.NOEVENT:
        print(event)

    if event.type == pygame.QUIT:
        pygame.quit()


def main():
    AppIsRunning = True
    pygame.init()

    if not pygame.display.get_init():
        print("display not initialized...")
    screen = pygame.display.set_mode([600, 480])
    while (AppIsRunning):
        handleEvents()


if __name__ == "__main__":
    main()
