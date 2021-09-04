import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
background_image = pygame.image.load('.\images\kosmos.jpg')

while True:
    #screen.fill((192, 192, 192))
    screen.blit(background_image, (0, 0))
    pygame.display.update()
    clock.tick(60)
    

