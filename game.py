#!/ usr/bin/python
import pygame
from pygame.locals import *

class Game(object):
    def __init__(self):
        pygame.init()

        self.window = pygame.display.set_mode((1024, 728)) 

        self.clock = pygame.time.Clock()
        
        pygame.key.set_repeat(50,50)
        
        pygame.display.set_caption('The Game %d fps' % self.clock.get_fps())

    def run(self):
        running = True

        while running:
            self.clock.tick()
            running = self.events()
            pygame.display.update()

    def events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                return False

            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    return False
        return True

class Player:
    def __init__(self):
        self.image_load = pygame.image.load("res/graphics/mfalcon.png").convert_alpha()
        self.x = 0
        self.y = 0
        self.angle = 0
    def move(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            self.y = self.y - 5
        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            self.y = self.y + 5
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            self.x = self.x - 5
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            self.x = self.x + 5
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            pass
    def draw(self, screen):
        self.image = pygame.transform.rotate(self.image_load, self.angle)
        self.screen.blit(image, (self.x, self.y))

if __name__ == '__main__':
    game = Game()
    game.run()
