import pygame
from pygame.locals import *
import random
import pygameMenu
from pygameMenu.locals import *
import os
import sys
import time


# https://github.com/ppizarror/pygame-menu


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
pygame.display.set_caption('Fruit Memory')
clock = pygame.time.Clock()
dt = 1 / fps

# Create screen and objects
surface = pygame.display.set_mode(screen_size)

# Spieleranzahl: 1 - 4
# Kartenanzahl: 16 - 36


'''
Objects - put Python classes and functions here
'''


def draw_fruit(i, (x, y)):
    screen.blit(fruits[i], (x, y))


def draw_fruits_random():
    for i in range(16):
        draw_fruit(i, random_pos[i])


def draw_rectangle(i):
    pygame.draw.rect(screen, lightblue, rectangles[i])


def draw_all_rectangles():
    for i in range(16):
        draw_rectangle(i)


score = 0
chosen = 0
card_1 = 0
card_2 = 0

def open_cards():
    counter = 0
    global score
    global chosen
    global card_1
    global card_2
    for i in rectangles:
        if i.collidepoint(mouse):
            print "card " + str(counter) + " clicked"

            chosen += 1
            if chosen == 1:
                card_1 = counter
                rectangles[card_1].move_ip(70, 0)

            if chosen == 2:
                card_2 = counter
                rectangles[card_2].move_ip(70, 0)
                chosen = 0
                print "2 cards chosen!"
                if check_cards(card_1, card_2) is True:
                    print "right pick!"
                    rectangles[card_1].move_ip(0, 2000)
                    rectangles[card_2].move_ip(0, 2000)
                    score += 1
                else:
                    close_cards()

        counter += 1


def close_cards():
    global card_1
    global card_2
    rectangles[card_1].move_ip(-70, 0)
    rectangles[card_2].move_ip(-70, 0)


def check_cards(c1, c2):
    if c1 == 0 and c2 == 1 or c1 == 1 and c2 == 0:
        return True
    elif c1 == 2 and c2 == 3 or c1 == 3 and c2 == 2:
        return True
    elif c1 == 4 and c2 == 5 or c1 == 5 and c2 == 4:
        return True
    elif c1 == 6 and c2 == 7 or c1 == 7 and c2 == 6:
        return True
    elif c1 == 8 and c2 == 9 or c1 == 9 and c2 == 8:
        return True
    elif c1 == 10 and c2 == 11 or c1 == 11 and c2 == 10:
        return True
    elif c1 == 12 and c2 == 13 or c1 == 13 and c2 == 12:
        return True
    elif c1 == 14 and c2 == 15 or c1 == 15 and c2 == 14:
        return True
    else:
        return False





'''
Setup - put run-once  code here
'''
screen_width = 800
screen_height = 640

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


# Menu and choice of options

'''
def main_background():
    surface.fill(orange)

size_menu = pygameMenu.Menu(surface,
                            bgfun=main_background,
                            color_selected=white,
                            font=pygameMenu.fonts.FONT_BEBAS,
                            font_color=black,
                            font_size=30,
                            menu_alpha=100,
                            menu_color=white,
                            menu_height=int(screen_height * 0.6),
                            menu_width=int(screen_width * 0.6),
                            onclose=PYGAME_MENU_DISABLE_CLOSE,
                            option_shadow=False,
                            title='Choose Size of Field',
                            window_height=screen_height,
                            window_width=screen_width
                            )

player_menu = pygameMenu.Menu(surface,
                              bgfun=main_background,
                              color_selected=white,
                              font=pygameMenu.fonts.FONT_BEBAS,
                              font_color=black,
                              font_size=30,
                              menu_alpha=100,
                              menu_color=white,
                              menu_height=int(screen_height * 0.6),
                              menu_width=int(screen_width * 0.6),
                              onclose=PYGAME_MENU_DISABLE_CLOSE,
                              option_shadow=False,
                              title='Choose Number of Players',
                              window_height=screen_height,
                              window_width=screen_width
                              )

main_menu = pygameMenu.Menu(surface,
                            bgfun=main_background,
                            color_selected=white,
                            font=pygameMenu.fonts.FONT_BEBAS,
                            font_color=white,
                            font_size=30,
                            menu_alpha=100,
                            menu_color=white,
                            menu_height=int(screen_height * 0.6),
                            menu_width=int(screen_width * 0.6),
                            onclose=PYGAME_MENU_DISABLE_CLOSE,
                            option_shadow=False,
                            title='Fruit Memory',
                            window_height=screen_height,
                            window_width=screen_width
                            )



#main_menu.add_option('Start Game', )
main_menu.add_option('Choose Number of Players', player_menu)
main_menu.add_option('Choose Size of Field', size_menu)
main_menu.add_option('Quit Game', PYGAME_MENU_EXIT)
'''






# Images ---> gameDisplay.blit(Img, (x,y))
apfelImg = pygame.image.load('images/apfel.png')
bananeImg = pygame.image.load('images/banane.png')
erdbeereImg = pygame.image.load('images/erdbeere.png')
weintraubeImg = pygame.image.load('images/weintraube.png')
kirscheImg = pygame.image.load('images/kirsche.png')
kiwiImg = pygame.image.load('images/kiwi.png')
orangeImg = pygame.image.load('images/orange.png')
wassermeloneImg = pygame.image.load('images/wassermelone.png')

fruits = [apfelImg, apfelImg, bananeImg, bananeImg, erdbeereImg, erdbeereImg, weintraubeImg, weintraubeImg,
          kirscheImg, kirscheImg, kiwiImg, kiwiImg, orangeImg, orangeImg, wassermeloneImg, wassermeloneImg]


# Positions
pos0 = (120, 100)
pos1 = (280, 100)
pos2 = (440, 100)
pos3 = (600, 100)

pos4 = (120, 240)
pos5 = (280, 240)
pos6 = (440, 240)
pos7 = (600, 240)

pos8 = (120, 380)
pos9 = (280, 380)
pos10 = (440, 380)
pos11 = (600, 380)

pos12 = (120, 520)
pos13 = (280, 520)
pos14 = (440, 520)
pos15 = (600, 520)

pos = [pos0, pos1, pos2, pos3, pos4, pos5, pos6, pos7,
       pos8, pos9, pos10, pos11, pos12, pos13, pos14, pos15]

random_pos = list(pos)
random.shuffle(random_pos)

# Rectangles
properties = (80, 80)

rect0 = pygame.Rect(random_pos[0], properties)
rect1 = pygame.Rect(random_pos[1], properties)
rect2 = pygame.Rect(random_pos[2], properties)
rect3 = pygame.Rect(random_pos[3], properties)

rect4 = pygame.Rect(random_pos[4], properties)
rect5 = pygame.Rect(random_pos[5], properties)
rect6 = pygame.Rect(random_pos[6], properties)
rect7 = pygame.Rect(random_pos[7], properties)


rect8 = pygame.Rect(random_pos[8], properties)
rect9 = pygame.Rect(random_pos[9], properties)
rect10 = pygame.Rect(random_pos[10], properties)
rect11 = pygame.Rect(random_pos[11], properties)

rect12 = pygame.Rect(random_pos[12], properties)
rect13 = pygame.Rect(random_pos[13], properties)
rect14 = pygame.Rect(random_pos[14], properties)
rect15 = pygame.Rect(random_pos[15], properties)

rectangles = [rect0, rect1, rect2, rect3, rect4, rect5, rect6, rect7,
              rect8, rect9, rect10, rect11, rect12, rect13, rect14, rect15]





'''
Main loop - put game loop here
'''
pairs_left = True
while pairs_left:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Application events
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            mouse = (mouse_x, mouse_y)
            open_cards()



    # Main menu
    # main_menu.mainloop(events)

    screen.fill(background_color)

    screen.blit(headline, (screen_width/2 - 150, 0))

    draw_fruits_random()
    draw_all_rectangles()




    pygame.display.flip()

    clock.tick(fps)

    if score == 8:
        pygame.quit()
        quit()
