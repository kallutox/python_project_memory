import pygame
import random
import time
import sys
import os

''' 
CONSTANTS
'''
WORLD_HEIGHT = 428
WORLD_WIDTH = 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
SEGMENT_HEIGHT = 20
SEGMENT_WIDTH = 20
SEGMENT_GAP = 5



'''
Objects - put Python classes and functions here
'''
class Segment(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([SEGMENT_WIDTH, SEGMENT_HEIGHT])
        self.image.fill(WHITE)

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y



'''
Setup - put run-once  code here
'''
dead = False

pygame.init()
clock = pygame.time.Clock()

world = pygame.display.set_mode([WORLD_WIDTH, WORLD_HEIGHT])
background = pygame.image.load(os.path.join('images', 'snake_background.png'))


pygame.display.set_caption('Kulik & Kreller - Snakes')

allspriteslist = pygame.sprite.Group()

'''
loops
'''
while not dead:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit();
            sys.exit()
            dead = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                print "left"

        if event.type == pygame.KEYUP:
            if event.key == ord('q'):
                pygame.quit()
                sys.exit()
                dead = False

    world.blit(background, [0,0])

    pygame.display.flip()
    clock.tick(15)





