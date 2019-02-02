import pygame
from pygame.locals import *
import random
import pygameMenu
from pygameMenu.locals import *
import os
import sys
import time
from memory_assets import *

# https://github.com/ppizarror/pygame-menu


grey = (190, 190, 190)
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


'''
Objects - put Python classes and functions here
'''


def draw_fruits(fruits, i, (x, y)):
    screen.blit(fruits[i], (x, y))


def draw_fruits_random(fruits, random_pos):
    for i in range(len(fruits)):
        draw_fruits(fruits, i, random_pos[i])


def draw_rectangles(rectangles, i):
    pygame.draw.rect(screen, lightblue, rectangles[i])


def draw_rectangles_random(rectangles):
    for i in range(len(rectangles)):
        draw_rectangles(rectangles, i)


def move_rectangles_random(rectangles, random_pos):
    for i in range(len(rectangles)):
        rectangles[i].x = random_pos[i][0]
        rectangles[i].y = random_pos[i][1]


score_overall = 0
score_1 = 0
score_2 = 0
score_3 = 0
score_4 = 0
chosen = 0
card_1 = 0
card_2 = 0
opened_card = None
player_counter = 1


def open_cards4x4(no_of_player):
    counter = 0
    global player_counter
    global player_1
    global player_2
    global player_3
    global player_4
    global opened_card
    global fin
    global win
    global instructions
    global score_1
    global score_2
    global score_3
    global score_4
    global score_overall
    global chosen
    global card_1
    global card_2

    if no_of_player == 1:
        for i in rectangles4x4:
            if i.collidepoint(mouse):
                print "card " + str(counter) + " clicked"
                if chosen == 0:
                    chosen += 1
                    card_1 = counter
                    rectangles4x4[card_1].move_ip(70, 0)
                    opened_card = card_1

                elif chosen == 1 and opened_card != counter:
                    chosen += 1
                    opened_card = None
                    card_2 = counter
                    rectangles4x4[card_2].move_ip(70, 0)

                    print "2 cards chosen!"
                    if check_cards(card_1, card_2) is True:
                        print "right pick!"
                        rectangles4x4[card_1].move_ip(0, 2000)
                        rectangles4x4[card_2].move_ip(0, 2000)
                        score_1 += 10
                        score_overall += 10
                        player_1 = score_font.render('Player 1: ' + str(score_1), False, navy_blue)
                        chosen = 0

                        if score_overall == 80:
                            fin = fin_font.render('All fruits found!', True, white, grey)
                            instructions = instructions_font.render('Press R to restart | Press Q to quit | Press M to'
                                                                    + ' return to Menu', True, black, grey)

            counter += 1

    if no_of_player == 2:
        for i in rectangles4x4:
            if i.collidepoint(mouse):
                print "card " + str(counter) + " clicked"
                if chosen == 0:
                    chosen += 1
                    card_1 = counter
                    rectangles4x4[card_1].move_ip(70, 0)
                    opened_card = card_1

                elif chosen == 1 and opened_card != counter:
                    chosen += 1
                    opened_card = None
                    card_2 = counter
                    rectangles4x4[card_2].move_ip(70, 0)

                    print "2 cards chosen!"
                    if check_cards(card_1, card_2) is True:
                        print "right pick!"
                        rectangles4x4[card_1].move_ip(0, 2000)
                        rectangles4x4[card_2].move_ip(0, 2000)
                        score_player(player_counter)
                        score_overall += 10
                        repaint_player(player_counter)
                        chosen = 0

                        if score_overall == 80:
                            win = win_font.render('Player ' + who_won() +' won!', True, white, grey)
                            instructions = instructions_font.render('Press R to restart | Press Q to quit | Press M to'
                                                                    + ' return to Menu', True, black, grey)
                    elif check_cards(card_1, card_2) is False:
                        player_counter += 1
                        if player_counter == 3:
                            player_counter = 1
                        repaint_player(player_counter)
            counter += 1

    if no_of_player == 3:
        for i in rectangles4x4:
            if i.collidepoint(mouse):
                print "card " + str(counter) + " clicked"
                if chosen == 0:
                    chosen += 1
                    card_1 = counter
                    rectangles4x4[card_1].move_ip(70, 0)
                    opened_card = card_1

                elif chosen == 1 and opened_card != counter:
                    chosen += 1
                    opened_card = None
                    card_2 = counter
                    rectangles4x4[card_2].move_ip(70, 0)

                    print "2 cards chosen!"
                    if check_cards(card_1, card_2) is True:
                        print "right pick!"
                        rectangles4x4[card_1].move_ip(0, 2000)
                        rectangles4x4[card_2].move_ip(0, 2000)
                        score_player(player_counter)
                        score_overall += 10
                        repaint_player(player_counter)
                        chosen = 0

                        if score_overall == 80:
                            win = win_font.render('Player ' + who_won() +' won!', True, white, grey)
                            instructions = instructions_font.render('Press R to restart | Press Q to quit | Press M to'
                                                                    + ' return to Menu', True, black, grey)
                    elif check_cards(card_1, card_2) is False:
                        player_counter += 1
                        if player_counter == 4:
                            player_counter = 1
                        repaint_player(player_counter)
            counter += 1

    if no_of_player == 4:
        for i in rectangles4x4:
            if i.collidepoint(mouse):
                print "card " + str(counter) + " clicked"
                if chosen == 0:
                    chosen += 1
                    card_1 = counter
                    rectangles4x4[card_1].move_ip(70, 0)
                    opened_card = card_1

                elif chosen == 1 and opened_card != counter:
                    chosen += 1
                    opened_card = None
                    card_2 = counter
                    rectangles4x4[card_2].move_ip(70, 0)

                    print "2 cards chosen!"
                    if check_cards(card_1, card_2) is True:
                        print "right pick!"
                        rectangles4x4[card_1].move_ip(0, 2000)
                        rectangles4x4[card_2].move_ip(0, 2000)
                        score_player(player_counter)
                        score_overall += 10
                        repaint_player(player_counter)
                        chosen = 0

                        if score_overall == 80:
                            win = win_font.render('Player ' + who_won() +' won!', True, white, grey)
                            instructions = instructions_font.render('Press R to restart | Press Q to quit | Press M to'
                                                                    + ' return to Menu', True, black, grey)
                    elif check_cards(card_1, card_2) is False:
                        player_counter += 1
                        if player_counter == 5:
                            player_counter = 1
                        repaint_player(player_counter)
            counter += 1




def who_won():
    global score_1
    global score_2
    global score_3
    global score_4
    scores = [score_1, score_2, score_3, score_4]

    if score_1 > score_2 and score_1 > score_3 and score_1 > score_4:
        return '1'
    elif score_2 > score_1 and score_2 > score_3 and score_2 > score_4:
        return '2'
    elif score_3 > score_1 and score_3 > score_2 and score_3 > score_4:
        return '2'
    elif score_4 > score_1 and score_4 > score_2 and score_4 > score_3:
        return '2'



def score_player(player):
    global score_1
    global score_2
    global score_3
    global score_4

    if player == 1:
        score_1 += 10

    if player == 2:
        score_2 += 10

    if player == 3:
        score_3 += 10

    if player == 4:
        score_4 += 10


def repaint_player(player):
    global player_1
    global player_2
    global player_3
    global player_4

    if player == 1:
        player_1 = score_font.render('Player 1: ' + str(score_1), False, navy_blue)
        player_2 = score_font.render('Player 2: ' + str(score_2), False, grey)
        player_3 = score_font.render('Player 3: ' + str(score_3), False, grey)
        player_4 = score_font.render('Player 4: ' + str(score_4), False, grey)

    elif player == 2:
        player_1 = score_font.render('Player 1: ' + str(score_1), False, grey)
        player_2 = score_font.render('Player 2: ' + str(score_2), False, navy_blue)
        player_3 = score_font.render('Player 3: ' + str(score_3), False, grey)
        player_4 = score_font.render('Player 4: ' + str(score_4), False, grey)
    elif player == 3:
        player_1 = score_font.render('Player 1: ' + str(score_1), False, grey)
        player_2 = score_font.render('Player 2: ' + str(score_2), False, grey)
        player_3 = score_font.render('Player 3: ' + str(score_3), False, navy_blue)
        player_4 = score_font.render('Player 4: ' + str(score_4), False, grey)
    elif player == 4:
        player_1 = score_font.render('Player 1: ' + str(score_1), False, grey)
        player_2 = score_font.render('Player 2: ' + str(score_2), False, grey)
        player_3 = score_font.render('Player 3: ' + str(score_3), False, grey)
        player_4 = score_font.render('Player 4: ' + str(score_4), False, navy_blue)


def close_cards():
    global card_1
    global card_2
    rectangles4x4[card_1].move_ip(-70, 0)
    rectangles4x4[card_2].move_ip(-70, 0)


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


def restart_game4x4():

    global score_1
    global score_2
    global score_3
    global score_4
    global score_overall
    global chosen
    global card_1
    global card_2
    global opened_card
    global fin
    global player_1
    global player_2
    global player_3
    global player_4
    global instructions
    global win

    score_1 = 0
    score_2 = 0
    score_3 = 0
    score_4 = 0
    score_overall = 0

    chosen = 0
    card_1 = 0
    card_2 = 0
    opened_card = None
    fin = fin_font.render('', False, (255, 255, 255))
    win = fin_font.render('', False, (255, 255, 255))
    instructions = instructions_font.render('', False, (255, 255, 255))
    repaint_player(1)
    random.shuffle(random_pos4x4)





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
player_2 = score_font.render('Player 2: ' + str(score_2), False, grey)
player_3 = score_font.render('Player 3: ' + str(score_3), False, grey)
player_4 = score_font.render('Player 4: ' + str(score_4), False, grey)

fin_font = pygame.font.SysFont('Calibri', 123, bold=True, italic=False)
fin = fin_font.render('', False, (255, 255, 255))

win_font = pygame.font.SysFont('Calibri', 100, bold=True, italic=False)
win = win_font.render('', False, (255, 255, 255))


instructions_font = pygame.font.SysFont('Calibri', 30, bold=True, italic=False)
instructions = instructions_font.render('', False, (255, 255, 255))














'''
Main loop - put game loop here
'''


def memory4x4(number_of_players):
    global chosen
    global score_1
    global player_1
    global headline
    global fin
    global instructions
    global clock
    global screen_height
    global screen_width
    global background_color
    global mouse
    global mouse_x
    global mouse_y

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
                    open_cards4x4(number_of_players) #pygame timer event ?

            if score_overall == 80:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        restart_game4x4()
                        draw_fruits_random(fruits4x4, random_pos4x4)
                        move_rectangles_random(rectangles4x4, random_pos4x4)

                    if event.key == pygame.K_q:
                        pygame.quit()
                        quit()

        screen.fill(background_color)

        draw_fruits_random(fruits4x4, random_pos4x4)
        draw_rectangles_random(rectangles4x4)

        screen.blit(headline, (screen_width/2 - 150, 0))
        screen.blit(player_1, (10, 10))
        screen.blit(player_2, (10, 50))
        screen.blit(player_3, (640, 10))
        screen.blit(player_4, (640, 50))
        screen.blit(fin, (0, 200))
        screen.blit(win, (50, 100))
        screen.blit(instructions, (10, 400))

        pygame.display.flip()

        clock.tick(fps)

def memory6x6():
    global chosen
    global score_1
    global player_1
    global headline
    global fin
    global instructions
    global clock
    global screen_height
    global screen_width
    global background_color
    global mouse
    global mouse_x
    global mouse_y

    pairs_left = True
    while pairs_left:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.fill(background_color)

        draw_rectangles_random(rectangles6x6)

        pygame.display.flip()

        clock.tick(fps)


memory4x4(4)
#memory6x6()
