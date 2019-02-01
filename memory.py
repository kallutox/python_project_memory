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
navy_blue = (0, 0, 128)
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


score_1 = 0
chosen = 0
card_1 = 0
card_2 = 0
opened_card = None


def open_cards():
    counter = 0
    global player_1
    global opened_card
    global fin
    global score_1
    global chosen
    global card_1
    global card_2
    for i in rectangles:
        if i.collidepoint(mouse):
            print "card " + str(counter) + " clicked"
            if chosen == 0:
                chosen += 1
                card_1 = counter
                rectangles[card_1].move_ip(70, 0)
                opened_card = card_1

            elif chosen == 1 and opened_card != counter:
                chosen += 1
                opened_card = None
                card_2 = counter
                rectangles[card_2].move_ip(70, 0)

                #chosen = 0
                print "2 cards chosen!"
                if check_cards(card_1, card_2) is True:
                    print "right pick!"
                    rectangles[card_1].move_ip(0, 2000)
                    rectangles[card_2].move_ip(0, 2000)
                    score_1 += 10
                    player_1 = score_font.render('Player 1: ' + str(score_1), False, navy_blue)
                    chosen = 0

                    if score_1 == 10:
                        fin = fin_font.render('All fruits found!', True, white, black)

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
# how to display text aus: https://sivasantosh.wordpress.com/2012/07/18/displaying-text-in-pygame/
pygame.font.init()
title = 'Fruit Memory!'
headline_font = pygame.font.SysFont('Calibri', 50, bold=True, italic=True)
headline = headline_font.render(title, False, white)


score_font = pygame.font.SysFont('Calibri', 30, bold=True, italic=False)
player_1 = score_font.render('Player 1: ' + str(score_1), False, navy_blue)


fin_font = pygame.font.SysFont('Calibri', 123, bold=True, italic=False)
fin = fin_font.render('', False, (255, 255, 255))




# Menu and choice of options






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
            if chosen == 2:
                close_cards()
                chosen = 0
            else:
                open_cards() #pygame timer event ?



    # Main menu
    # main_menu.mainloop(events)

    screen.fill(background_color)

    draw_fruits_random()
    draw_all_rectangles()

    screen.blit(headline, (screen_width/2 - 150, 0))
    screen.blit(player_1, (10, 10))
    screen.blit(fin, (0, screen_height/2 - 80))






    pygame.display.flip()

    clock.tick(fps)

    if score_1 == 80:
        pygame.quit()
        quit()
