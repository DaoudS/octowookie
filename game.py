#!/usr/bin/python

import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))

    pacman_image = pygame.image.load("sprites/pacman-small.png")
    screen.blit(pacman_image, (10, 10))

    pygame.display.update()

    while True:
        pass

if __name__ == '__main__':
    main()
