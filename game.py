#!/ usr/bin/python
import pygame
from pygame.locals import *

class Game(object):
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((1024, 728)) 

        self.clock = pygame.time.Clock()
        
        pygame.display.set_caption('The Game, fps = %d ' % self.clock.get_fps())

    def main(self):
        running = True
        control = Game()

        while running:
            self.clock.tick()
            running = self.events()
            control.main_scene

            pygame.display.update()

    def events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                return False

            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    return False
        return True
    
    def main_menu(self):
        menubg = pygame.image.load("res/graphics/menubg.png")
        screen.blit(background, [0,0])

    def main_scene(self):
        background = pygame.image.load("res/graphics/backdrop.jpg")
        screen.blit(background, [0,0])

class Player:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.skin = pygame.image.load("res/graphics/mfalcon.png").convert_alpha()
    def move(self):
        pass
    
    def draw(self):
        screen.blit(skin, [0,0])

if __name__ == '__main__':
    game = Game()
    game.main()
