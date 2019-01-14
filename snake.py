# -*- coding: utf-8 -*-
import pygame
import sys
import os

'''
Tutorial Code from here: https://opensource.com/article/17/12/game-framework-python
'''



'''
Objects - put Python classes and functions here
'''




'''
Setup - put run-once  code here
'''
main = True

worldx = 600
worldy = 428

fps = 40    # frame rate
ani = 4     # animation cycles
clock = pygame.time.Clock()
pygame.init()

world = pygame.display.set_mode([worldx, worldy])
backdrop = pygame.image.load(os.path.join('images', 'snake_background.png'))   # + .convert() ??
backdropbox = world.get_rect()



'''
Main loop - put game loop here
'''
while main == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            main = False

        if event.type == pygame.KEYDOWN:
            if event.key == ord('q'):
                pygame.quit()
                sys.exit()
                main = False

    world.blit(backdrop, backdropbox)
    pygame.display.flip()
    clock.tick(fps)


