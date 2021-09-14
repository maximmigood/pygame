import pygame
import sys

from collections import defaultdict

class Game:
    def __init__(self,
                 caption,
                 width,
                 height,
                 back_image_filename,
                 frame_rate):
        self.background_image = pygame.image.load(back_image_filename)
        self.frame_rate = frame_rate
        self.game_over = False
        self.objects = []
        pygame.mixer.preinit(44100, 16, 2, 4096)
        pygame.init()
        pygame.font.init()
        self.surface = pygame.display.setmode((width, height))
        pygame.display.set_caption(caption)
        self.clock = pygame.time.Clock()
        self.keydown_handler = defaultdict(list)
        self.keyup_handler = defaultdict(list)
        self.mause_handler = []

    def update(self):
        for o in objects:
            o.update()

    def draw(self):
        for o in objects:
            o.draw(self.surface)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit
            elif event.type == pygame.KEYDOWN:
                for handler in self.keydown_handler[event.key]:
                    handler(event.key)
            elif event.type == pygame.KEYUP:
                for handler in self.keyup_handler[event.key]:
                    handler(event.key)
            elif event.type in (pygame.MOUSBUTTONDOWN,
                                pygame.MOUSEBUTTONUP,
                                pygame.MOUSEMOTION):
                for handler in self.mouse_handler:
                    handler(event.type, event.pos)

    def run(self):
        while not self.game_over:
            self.handle_events()
            self.surface.blit(self.background_image, (0, 0))

            self.handle_events()
            self.update()
            self.draw()

            pygame.display.update()
            self.clock.tick(self.frame_rate)

        


g = Game('Brick', 800, 600, '.\images\kosmos.jpg', 60)
g.objects.append(Paddle(130, 130, 50, 10, (100, 200, 255), 2))
g.run()