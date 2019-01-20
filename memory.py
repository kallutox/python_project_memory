import pygame
import random
import sys


# Spieleranzahl: 2-8
# Kartenanzahl: 64 (32 Bildpaare)



'''
Objects - put Python classes and functions here
'''





'''
Setup - put run-once  code here
'''
background_color = (255, 255, 255)
screen_width = 800
screen_height = 640

clock = pygame.time.Clock()
fps = 30

screen = pygame.display.set_mode([screen_width, screen_height])
pygame.display.set_caption("Memory")

mouse_x = 0
mouse_y = 0

'''
Main loop - put game loop here
'''
pairs_left = True
while pairs_left:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    screen.fill(background_color)

    pygame.display.flip()

    clock.tick(fps)


# Rectangle = https://stackoverflow.com/questions/53660333/pygame-drawing-multiple-rectangles
