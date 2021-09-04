import pygame

#import config as c
from game_object import Game_object

class Paddle(Game_object):
    def __init__(self, x, y, w, h, color, offset):
        Game_object.__init__(self, x, y, w, h)
        self.color = color
        self.offset = offset
        self.moving_left = False
        self.moving_right = False

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.bounds)