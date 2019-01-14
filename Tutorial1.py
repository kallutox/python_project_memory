# -*- coding: utf-8 -*-
import pygame
import sys
import os
import random

'''
Tutorial Code from here: https://opensource.com/article/17/12/game-framework-python
'''



'''
Objects - put Python classes and functions here
'''
class Snake(pygame.sprite.Sprite):
    '''
    Spawn a player
    '''

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images = []

        img = pygame.image.load(os.path.join('images', 'hero.png')).convert()
        self.images.append(img)
        self.image = self.images[0]
        self.rect = self.image.get_rect()

        self.movex = 0  # move along X
        self.movey = 0  # move along Y
        self.frame = 0  # count frames

    def control(self, x, y):
        self.movex += x
        self.movey += y

    def update(self):
        self.rect.x = self.rect.x + self.movex
        self.rect.y = self.rect.y + self.movey




'''
Setup - put run-once  code here
'''
dead = True

worldx = 600
worldy = 428

fps = 40    # frame rate
ani = 4     # animation cycles
clock = pygame.time.Clock()
pygame.init()

world = pygame.display.set_mode([worldx, worldy])
backdrop = pygame.image.load(os.path.join('images', 'snake_background.png'))
backdropbox = world.get_rect()

snake = Snake()
snake.rect.x = 0
snake.rect.y = 0
player_list = pygame.sprite.Group()
player_list.add(snake)
steps = 10

'''
Main loop - put game loop here
'''
while dead == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit();
            sys.exit()
            dead = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                snake.control(-steps, 0)
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                snake.control(steps, 0)


        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                snake.control(steps, 0)
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                snake.control(-steps, 0)
            if event.key == ord('q'):
                pygame.quit()
                sys.exit()
                dead = False

    snake.update()  # update player position
    world.blit(backdrop, backdropbox)
    player_list.draw(world)
    pygame.display.flip()
    clock.tick(fps)


