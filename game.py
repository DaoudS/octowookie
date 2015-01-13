#!/usr/bin/python

import pygame

def main():
    pygame.init()
    #Colors
    red   = 255,0,0
    green = 0,255,0
    blue  = 0,0,255
    white = 255,255,255

    screen = pygame.display.set_mode((640, 480))
    screen.fill(white)

    player_image = pygame.image.load("sprites/mfalcon.png")
    screen.blit(player_image, (300, 240))
    pygame.display.update()

    while True:
        pass

if __name__ == '__main__':
    main()
