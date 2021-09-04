import pygame

from game_object import Game_object

class Brick(Game_object):
    def __init__ (self, x, y, w, h, color, special_effect = None):
        Game_object.__init__(self, x, y, w, h)
        self.color = color
        self.special_effect = special_effect
    
    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.bounds)
