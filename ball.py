import pygame
from game_object import Game_object
import config as c
import random

class Ball(Game_object):
    def __init__(self, x, y, r, color, speed):
        Game_object.__init__(self,
                              x - r, 
                              y - r,
                              r * 2,
                              r * 2,
                              speed )
        self.radius = r
        self.diametr = r * 2
        self.color = color

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, self.center, self.radius)

    def create_ball(self):
        speed = (random.randint(-2, 2), c.ball_speed)