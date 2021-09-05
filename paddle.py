import pygame

import config as c
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

    def update(self):
        if self.moving_left:
            dx = -(min(self.offset, self.left))
        elif self.moving_right:
             dx = min(self.offset, c.screen_width - self.right)
        else:
            return
        self.move(dx, 0)

    def handle(self, key):
        if key == pygame.K_LEFT:
            self.moving_left = not self.moving_left
        else:
            self.moving_right = not self.moving_right
                