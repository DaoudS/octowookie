import pygame

class Player:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.skin = pygame.image.load("res/graphics/mfalcon.png").convert_alpha()
    def move(self):
        pass
    
    def draw(self):
        screen.blit(skin, [0,0])
