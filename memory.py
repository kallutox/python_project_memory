import pygame
from pygame.locals import *
import random
import pygameMenu
from pygameMenu.locals import *
import sys

#https://github.com/ppizarror/pygame-menu


black = (0, 0, 0)
white = (255, 255, 255)
orange = (255, 165, 0)
lightblue = (173, 216, 230)
background_color = orange
fps = 30.0
menu_colour = (200, 200, 200)
screen_width = 800
screen_height = 640
screen_size = (screen_width, screen_height)

# Create screen and objects
surface = pygame.display.set_mode(screen_size)

# Spieleranzahl: 2-8
# Kartenanzahl: 16


'''
Objects - put Python classes and functions here
'''


def draw_fruit(i, (x, y)):
    screen.blit(fruits[i], (x, y))

def draw_fruits_random():
    for i in range(16):
        draw_fruit(i, random_pos[i])


'''
Setup - put run-once  code here
'''
background_color = orange
screen_width = 800
screen_height = 640

clock = pygame.time.Clock()
fps = 30

screen = pygame.display.set_mode([screen_width, screen_height])
pygame.display.set_caption("Fruit Memory!")

mouse_x = 0
mouse_y = 0

# Game Title and Menu
pygame.font.init()
title = 'Fruit Memory!'
font = pygame.font.SysFont('Calibri', 50, bold=True, italic=True)
headline = font.render(title, False, white)

#Menu doesn't work yet
main_menu = pygameMenu.Menu(screen, screen_width, screen, font, title)
game_size_menu = pygameMenu.Menu(screen, screen_width, screen, font, "Choose a size for the game's field:")

main_menu.add_option('Start Game', )
main_menu.add_option('Choose Size of Field', game_size_menu)
main_menu.add_option('Exit', PYGAME_MENU_EXIT)


# Images ---> gameDisplay.blit(Img, (x,y))
apfelImg = pygame.image.load('images/apfel.jpg')
bananeImg = pygame.image.load('images/banane.jpg')
erdbeereImg = pygame.image.load('images/erdbeere.jpg')
weintraubeImg = pygame.image.load('images/weintraube.jpg')
kirscheImg = pygame.image.load('images/kirsche.jpg')
kiwiImg = pygame.image.load('images/kiwi.jpg')
orangeImg = pygame.image.load('images/orange.jpg')
wassermeloneImg = pygame.image.load('images/wassermelone.jpg')

fruits = [apfelImg, bananeImg, erdbeereImg, weintraubeImg, kirscheImg, kiwiImg, orangeImg, wassermeloneImg,
          apfelImg, bananeImg, erdbeereImg, weintraubeImg, kirscheImg, kiwiImg, orangeImg, wassermeloneImg]


# Positions
pos = []
pos.append((120, 100))
pos.append((280, 100))
pos.append((440, 100))
pos.append((600, 100))

pos.append((120, 240))
pos.append((280, 240))
pos.append((440, 240))
pos.append((600, 240))

pos.append((120, 380))
pos.append((280, 380))
pos.append((440, 380))
pos.append((600, 380))

pos.append((120, 520))
pos.append((280, 520))
pos.append((440, 520))
pos.append((600, 520))



# Rectangles
properties = (80, 80)

rect0 = pygame.Rect(pos[0], properties)
rect1 = pygame.Rect(pos[1], properties)
rect2 = pygame.Rect(pos[2], properties)
rect3 = pygame.Rect(pos[3], properties)

rect4 = pygame.Rect(pos[4], properties)
rect5 = pygame.Rect(pos[5], properties)
rect6 = pygame.Rect(pos[6], properties)
rect7 = pygame.Rect(pos[7], properties)


rect8 = pygame.Rect(pos[8], properties)
rect9 = pygame.Rect(pos[9], properties)
rect10 = pygame.Rect(pos[10], properties)
rect11 = pygame.Rect(pos[11], properties)

rect12 = pygame.Rect(pos[12], properties)
rect13 = pygame.Rect(pos[13], properties)
rect14 = pygame.Rect(pos[14], properties)
rect15 = pygame.Rect(pos[15], properties)



random_pos = list(pos)
random.shuffle(random_pos)



'''
Main loop - put game loop here
'''
pairs_left = True
while pairs_left:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()


    '''
    # Main menu
    game_menu.mainloop(events)
    '''


    screen.fill(background_color)

    screen.blit(headline, (screen_width/2 - 150, 0))

    pygame.draw.rect(screen, lightblue, rect0)
    pygame.draw.rect(screen, lightblue, rect1)
    pygame.draw.rect(screen, lightblue, rect2)
    pygame.draw.rect(screen, lightblue, rect3)
    pygame.draw.rect(screen, lightblue, rect4)
    pygame.draw.rect(screen, lightblue, rect5)
    pygame.draw.rect(screen, lightblue, rect6)
    pygame.draw.rect(screen, lightblue, rect7)
    pygame.draw.rect(screen, lightblue, rect8)
    pygame.draw.rect(screen, lightblue, rect9)
    pygame.draw.rect(screen, lightblue, rect10)
    pygame.draw.rect(screen, lightblue, rect11)
    pygame.draw.rect(screen, lightblue, rect12)
    pygame.draw.rect(screen, lightblue, rect13)
    pygame.draw.rect(screen, lightblue, rect14)
    pygame.draw.rect(screen, lightblue, rect15)

    draw_fruits_random()

    pygame.display.flip()

    clock.tick(fps)

