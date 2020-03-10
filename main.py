import pygame
from pygame.constants import *


def handleEvents(state):
    event = pygame.event.poll()
    if event.type != pygame.NOEVENT:
        print(event)

    if event.type == pygame.QUIT:
        state['AppIsRunning'] = False


def main():
    state = {'AppIsRunning': True}
    pygame.init()
    arrr = 5
    print(f'{arrr} is a number')

    if not pygame.display.get_init():
        print("display not initialized...")
    screen = pygame.display.set_mode([640, 480])
    while (state['AppIsRunning']):
        handleEvents(state)


if __name__ == "__main__":
    main()
