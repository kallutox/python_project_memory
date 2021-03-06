import pygame
from pygame.locals import *
import random
import pygameMenu
from pygameMenu.locals import *
import pygameMenu.config_menu as cfg
from memory_assets import *


# code structure from https://pythonprogramming.net/adding-sounds-music-pygame/

# code to play sound from https://nerdparadise.com/programming/pygame/part3
# and https://pythonprogramming.net/adding-sounds-music-pygame/

# ----- variables

# colors
black = (0, 0, 0)
white = (255, 255, 255)
grey = (200, 200, 200)
light_grey = (220, 220, 220)
orange = (255, 190, 50)

background_color = orange
menu_background = grey


# game properties
screen_width = 800
screen_height = 640
screen_size = (screen_width, screen_height)

fps = 30.0

screen = pygame.display.set_mode([screen_width, screen_height])
font = pygameMenu.fonts.FONT_BEBAS

mouse_x = mouse_y = 0

pygame.display.set_caption('FRUIT MEMORY')
clock = pygame.time.Clock()
dt = 1 / fps

score_1 = score_2 = score_3 = score_4 = score_overall = 0
chosen = card_1 = card_2 = 0

opened_card = None
player_counter = 1


# ----- functions

def draw_fruits(fruits, i, (x, y)):
    screen.blit(fruits[i], (x, y))


def draw_fruits_random(fruits, random_pos):
    for i in range(len(fruits)):
        draw_fruits(fruits, i, random_pos[i])


def draw_rectangles(rectangles, i):
    pygame.draw.rect(screen, light_grey, rectangles[i])


def draw_rectangles_random(rectangles):
    for i in range(len(rectangles)):
        draw_rectangles(rectangles, i)


def move_rectangles_random(rectangles, random_pos):
    for i in range(len(rectangles)):
        rectangles[i].x = random_pos[i][0]
        rectangles[i].y = random_pos[i][1]


# open a card in a 4x4 game
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

                    if check_cards(card_1, card_2) is True:

                        rectangles4x4[card_1].move_ip(0, 2000)
                        rectangles4x4[card_2].move_ip(0, 2000)
                        score_1 += 10
                        score_overall += 10
                        player_1 = score_font.render('PLAYER 1: ' + str(score_1), False, black)
                        chosen = 0

                        if score_overall == 80:
                            pygame.mixer.music.load('audio/good.wav')
                            pygame.mixer.music.play(0)
                            fin = fin_font.render('ALL FRUITS FOUND!', True, black, grey)
                            instructions = instructions_font.render('   Press R to restart | Press Q to quit  ',
                                                                    True, black, grey)

            counter += 1

    if no_of_player == 2:
        for i in rectangles4x4:
            if i.collidepoint(mouse):
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

                    if check_cards(card_1, card_2) is True:
                        rectangles4x4[card_1].move_ip(0, 2000)
                        rectangles4x4[card_2].move_ip(0, 2000)
                        score_player(player_counter)
                        score_overall += 10
                        repaint_player(player_counter)
                        chosen = 0

                        if score_overall == 80:
                            pygame.mixer.music.load('audio/good.wav')
                            pygame.mixer.music.play(0)
                            win = win_font.render(who_won(), True, black, grey)
                            instructions = instructions_font.render('   Press R to restart | Press Q to quit  ',
                                                                    True, black, grey)
                    elif check_cards(card_1, card_2) is False:
                        player_counter += 1
                        if player_counter == 3:
                            player_counter = 1
                        repaint_player(player_counter)
            counter += 1

    if no_of_player == 3:
        for i in rectangles4x4:
            if i.collidepoint(mouse):
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

                    if check_cards(card_1, card_2) is True:
                        rectangles4x4[card_1].move_ip(0, 2000)
                        rectangles4x4[card_2].move_ip(0, 2000)
                        score_player(player_counter)
                        score_overall += 10
                        repaint_player(player_counter)
                        chosen = 0

                        if score_overall == 80:
                            pygame.mixer.music.load('audio/good.wav')
                            pygame.mixer.music.play(0)
                            win = win_font.render(who_won(), True, black, grey)
                            instructions = instructions_font.render('   Press R to restart | Press Q to quit  ',
                                                                    True, black, grey)
                    elif check_cards(card_1, card_2) is False:
                        player_counter += 1
                        if player_counter == 4:
                            player_counter = 1
                        repaint_player(player_counter)
            counter += 1

    if no_of_player == 4:
        for i in rectangles4x4:
            if i.collidepoint(mouse):
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

                    if check_cards(card_1, card_2) is True:
                        rectangles4x4[card_1].move_ip(0, 2000)
                        rectangles4x4[card_2].move_ip(0, 2000)
                        score_player(player_counter)
                        score_overall += 10
                        repaint_player(player_counter)
                        chosen = 0

                        if score_overall == 80:
                            pygame.mixer.music.load('audio/good.wav')
                            pygame.mixer.music.play(0)
                            win = win_font.render(who_won(), True, black, grey)
                            instructions = instructions_font.render('   Press R to restart | Press Q to quit  ',
                                                                    True, black, grey)
                    elif check_cards(card_1, card_2) is False:
                        player_counter += 1
                        if player_counter == 5:
                            player_counter = 1
                        repaint_player(player_counter)
            counter += 1


# open a card in a 6x6 game
def open_cards6x6(no_of_player):
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
        for i in rectangles6x6:
            if i.collidepoint(mouse):
                if chosen == 0:
                    chosen += 1
                    card_1 = counter
                    rectangles6x6[card_1].move_ip(2000, 0)
                    opened_card = card_1

                elif chosen == 1 and opened_card != counter:
                    chosen += 1
                    opened_card = None
                    card_2 = counter
                    rectangles6x6[card_2].move_ip(2000, 0)

                    if check_cards(card_1, card_2) is True:
                        rectangles6x6[card_1].move_ip(0, 2000)
                        rectangles6x6[card_2].move_ip(0, 2000)
                        score_1 += 10
                        score_overall += 10
                        player_1 = score_font.render('PLAYER 1: ' + str(score_1), False, black)
                        chosen = 0

                        if score_overall == 180:
                            pygame.mixer.music.load('audio/good.wav')
                            pygame.mixer.music.play(0)
                            fin = fin_font.render('ALL FRUITS FOUND!', True, black, grey)
                            instructions = instructions_font.render('   Press R to restart | Press Q to quit  ',
                                                                    True, black, grey)

            counter += 1

    if no_of_player == 2:
        for i in rectangles6x6:
            if i.collidepoint(mouse):
                if chosen == 0:
                    chosen += 1
                    card_1 = counter
                    rectangles6x6[card_1].move_ip(2000, 0)
                    opened_card = card_1

                elif chosen == 1 and opened_card != counter:
                    chosen += 1
                    opened_card = None
                    card_2 = counter
                    rectangles6x6[card_2].move_ip(2000, 0)

                    if check_cards(card_1, card_2) is True:
                        rectangles6x6[card_1].move_ip(0, 2000)
                        rectangles6x6[card_2].move_ip(0, 2000)
                        score_player(player_counter)
                        score_overall += 10
                        repaint_player(player_counter)
                        chosen = 0

                        if score_overall == 180:
                            pygame.mixer.music.load('audio/good.wav')
                            pygame.mixer.music.play(0)
                            win = win_font.render(who_won(), True, black, grey)
                            instructions = instructions_font.render('   Press R to restart | Press Q to quit  ',
                                                                    True, black, grey)
                    elif check_cards(card_1, card_2) is False:
                        player_counter += 1
                        if player_counter == 3:
                            player_counter = 1
                        repaint_player(player_counter)
            counter += 1

    if no_of_player == 3:
        for i in rectangles6x6:
            if i.collidepoint(mouse):
                if chosen == 0:
                    chosen += 1
                    card_1 = counter
                    rectangles6x6[card_1].move_ip(2000, 0)
                    opened_card = card_1

                elif chosen == 1 and opened_card != counter:
                    chosen += 1
                    opened_card = None
                    card_2 = counter
                    rectangles6x6[card_2].move_ip(2000, 0)

                    if check_cards(card_1, card_2) is True:
                        rectangles6x6[card_1].move_ip(0, 2000)
                        rectangles6x6[card_2].move_ip(0, 2000)
                        score_player(player_counter)
                        score_overall += 10
                        repaint_player(player_counter)
                        chosen = 0

                        if score_overall == 180:
                            pygame.mixer.music.load('audio/good.wav')
                            pygame.mixer.music.play(0)
                            win = win_font.render(who_won(), True, black, grey)
                            instructions = instructions_font.render('   Press R to restart | Press Q to quit  ',
                                                                    True, black, grey)
                    elif check_cards(card_1, card_2) is False:
                        player_counter += 1
                        if player_counter == 4:
                            player_counter = 1
                        repaint_player(player_counter)
            counter += 1

    if no_of_player == 4:
        for i in rectangles6x6:
            if i.collidepoint(mouse):
                if chosen == 0:
                    chosen += 1
                    card_1 = counter
                    rectangles6x6[card_1].move_ip(2000, 0)
                    opened_card = card_1

                elif chosen == 1 and opened_card != counter:
                    chosen += 1
                    opened_card = None
                    card_2 = counter
                    rectangles6x6[card_2].move_ip(2000, 0)

                    if check_cards(card_1, card_2) is True:
                        rectangles6x6[card_1].move_ip(0, 2000)
                        rectangles6x6[card_2].move_ip(0, 2000)
                        score_player(player_counter)
                        score_overall += 10
                        repaint_player(player_counter)
                        chosen = 0

                        if score_overall == 180:
                            pygame.mixer.music.load('audio/good.wav')
                            pygame.mixer.music.play(0)
                            win = win_font.render(who_won(), True, black, grey)
                            instructions = instructions_font.render('   Press R to restart | Press Q to quit  ',
                                                                    True, black, grey)
                    elif check_cards(card_1, card_2) is False:
                        player_counter += 1
                        if player_counter == 5:
                            player_counter = 1
                        repaint_player(player_counter)
            counter += 1


# return the winner of a game
def who_won():
    global score_1
    global score_2
    global score_3
    global score_4

    if score_1 > score_2 and score_1 > score_3 and score_1 > score_4:
        return 'Player 1 won!'
    elif score_2 > score_1 and score_2 > score_3 and score_2 > score_4:
        return 'Player 2 won!'
    elif score_3 > score_1 and score_3 > score_2 and score_3 > score_4:
        return 'Player 3 won!'
    elif score_4 > score_1 and score_4 > score_2 and score_4 > score_3:
        return 'Player 4 won!'
    else:
        return 'No one won!'


# adds to the player's score
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


# renders score of current player in different color
def repaint_player(player):
    global player_1
    global player_2
    global player_3
    global player_4

    if player == 1:
        player_1 = score_font.render('PLAYER 1: ' + str(score_1), False, black)
        player_2 = score_font.render('PLAYER 2: ' + str(score_2), False, white)
        player_3 = score_font.render('PLAYER 3: ' + str(score_3), False, white)
        player_4 = score_font.render('PLAYER 4: ' + str(score_4), False, white)

    elif player == 2:
        player_1 = score_font.render('PLAYER 1: ' + str(score_1), False, white)
        player_2 = score_font.render('PLAYER 2: ' + str(score_2), False, black)
        player_3 = score_font.render('PLAYER 3: ' + str(score_3), False, white)
        player_4 = score_font.render('PLAYER 4: ' + str(score_4), False, white)

    elif player == 3:
        player_1 = score_font.render('PLAYER 1: ' + str(score_1), False, white)
        player_2 = score_font.render('PLAYER 2: ' + str(score_2), False, white)
        player_3 = score_font.render('PLAYER 3: ' + str(score_3), False, black)
        player_4 = score_font.render('PLAYER 4: ' + str(score_4), False, white)
    elif player == 4:
        player_1 = score_font.render('PLAYER 1: ' + str(score_1), False, white)
        player_2 = score_font.render('PLAYER 2: ' + str(score_2), False, white)
        player_3 = score_font.render('PLAYER 3: ' + str(score_3), False, white)
        player_4 = score_font.render('PLAYER 4: ' + str(score_4), False, black)


# hides a pair of cards in a 4x4 game
def close_cards4x4():
    global card_1
    global card_2
    rectangles4x4[card_1].move_ip(-70, 0)
    rectangles4x4[card_2].move_ip(-70, 0)


# hides a pair of cards in a 6x6 game
def close_cards6x6():
    global card_1
    global card_2
    rectangles6x6[card_1].move_ip(-2000, 0)
    rectangles6x6[card_2].move_ip(-2000, 0)


# checks whether two cards are the same
def check_cards(c1, c2):
    if c1 == 0 and c2 == 1 or c1 == 1 and c2 == 0:
        pygame.mixer.music.load('audio/coin.wav')
        pygame.mixer.music.play(0)
        return True
    elif c1 == 2 and c2 == 3 or c1 == 3 and c2 == 2:
        pygame.mixer.music.load('audio/coin.wav')
        pygame.mixer.music.play(0)
        return True
    elif c1 == 4 and c2 == 5 or c1 == 5 and c2 == 4:
        pygame.mixer.music.load('audio/coin.wav')
        pygame.mixer.music.play(0)
        return True
    elif c1 == 6 and c2 == 7 or c1 == 7 and c2 == 6:
        pygame.mixer.music.load('audio/coin.wav')
        pygame.mixer.music.play(0)
        return True
    elif c1 == 8 and c2 == 9 or c1 == 9 and c2 == 8:
        pygame.mixer.music.load('audio/coin.wav')
        pygame.mixer.music.play(0)
        return True
    elif c1 == 10 and c2 == 11 or c1 == 11 and c2 == 10:
        pygame.mixer.music.load('audio/coin.wav')
        pygame.mixer.music.play(0)
        return True
    elif c1 == 12 and c2 == 13 or c1 == 13 and c2 == 12:
        pygame.mixer.music.load('audio/coin.wav')
        pygame.mixer.music.play(0)
        return True
    elif c1 == 14 and c2 == 15 or c1 == 15 and c2 == 14:
        pygame.mixer.music.load('audio/coin.wav')
        pygame.mixer.music.play(0)
        return True
    elif c1 == 16 and c2 == 17 or c1 == 17 and c2 == 16:
        pygame.mixer.music.load('audio/coin.wav')
        pygame.mixer.music.play(0)
        return True
    elif c1 == 18 and c2 == 19 or c1 == 19 and c2 == 18:
        pygame.mixer.music.load('audio/coin.wav')
        pygame.mixer.music.play(0)
        return True
    elif c1 == 20 and c2 == 21 or c1 == 21 and c2 == 20:
        pygame.mixer.music.load('audio/coin.wav')
        pygame.mixer.music.play(0)
        return True
    elif c1 == 22 and c2 == 23 or c1 == 23 and c2 == 22:
        pygame.mixer.music.load('audio/coin.wav')
        pygame.mixer.music.play(0)
        return True
    elif c1 == 24 and c2 == 25 or c1 == 25 and c2 == 24:
        pygame.mixer.music.load('audio/coin.wav')
        pygame.mixer.music.play(0)
        return True
    elif c1 == 26 and c2 == 27 or c1 == 27 and c2 == 26:
        pygame.mixer.music.load('audio/coin.wav')
        pygame.mixer.music.play(0)
        return True
    elif c1 == 28 and c2 == 29 or c1 == 29 and c2 == 28:
        pygame.mixer.music.load('audio/coin.wav')
        pygame.mixer.music.play(0)
        return True
    elif c1 == 30 and c2 == 31 or c1 == 31 and c2 == 30:
        pygame.mixer.music.load('audio/coin.wav')
        pygame.mixer.music.play(0)
        return True
    elif c1 == 32 and c2 == 33 or c1 == 33 and c2 == 32:
        pygame.mixer.music.load('audio/coin.wav')
        pygame.mixer.music.play(0)
        return True
    elif c1 == 34 and c2 == 35 or c1 == 35 and c2 == 34:
        pygame.mixer.music.load('audio/coin.wav')
        pygame.mixer.music.play(0)
        return True
    else:
        pygame.mixer.music.load('audio/wrong.wav')
        pygame.mixer.music.play(0)
        return False


# start game new with new card position
def restart_game(random_positions):
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

    score_1 = score_2 = score_3 = score_4 = score_overall = 0
    chosen = card_1 = card_2 = 0

    opened_card = None
    fin = fin_font.render('', False, white)
    win = win_font.render('', False, white)
    instructions = instructions_font.render('', False, white)
    repaint_player(1)
    random.shuffle(random_positions)


# texts
# how to display text taken from: https://sivasantosh.wordpress.com/2012/07/18/displaying-text-in-pygame/

pygame.font.init()
title = 'FRUIT MEMORY'
headline_font = pygame.font.SysFont(None, cfg.MENU_FONT_SIZE_TITLE)
headline = headline_font.render(title, True, white, cfg.MENU_TITLE_BG_COLOR)

score_font = pygame.font.SysFont(font, 35, bold=False, italic=False)
player_1 = score_font.render('PLAYER 1: ' + str(score_1), False, black)
player_2 = score_font.render('PLAYER 2: ' + str(score_2), False, white)
player_3 = score_font.render('PLAYER 3: ' + str(score_3), False, white)
player_4 = score_font.render('PLAYER 4: ' + str(score_4), False, white)

fin_font = pygame.font.SysFont('Calibri', 101)
fin = fin_font.render('', False, white)

win_font = pygame.font.SysFont('Calibri', 100)
win = win_font.render('', False, white)

instructions_font = pygame.font.SysFont('Calibri', 30)
instructions = instructions_font.render('', False, white)


# main loops
def memory4x4(number_of_players):
    global chosen
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
                    close_cards4x4()
                    chosen = 0
                else:
                    open_cards4x4(number_of_players)

            if score_overall == 80:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        pygame.mixer.music.load('audio/start.wav')
                        pygame.mixer.music.play(0)
                        restart_game(random_pos4x4)
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
        screen.blit(win, (124, 200))
        screen.blit(instructions, (180, 400))

        pygame.display.flip()

        clock.tick(fps)


def memory6x6(number_of_players):
    global chosen
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
                    close_cards6x6()
                    chosen = 0
                else:
                    open_cards6x6(number_of_players)

            if score_overall == 180:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        pygame.mixer.music.load('audio/start.wav')
                        pygame.mixer.music.play(0)
                        restart_game(random_pos6x6)
                        draw_fruits_random(fruits6x6, random_pos6x6)
                        move_rectangles_random(rectangles6x6, random_pos6x6)

                    if event.key == pygame.K_q:
                        pygame.quit()
                        quit()

        screen.fill(background_color)

        draw_fruits_random(fruits6x6, random_pos6x6)
        draw_rectangles_random(rectangles6x6)

        screen.blit(headline, (screen_width/2 - 150, 0))
        screen.blit(player_1, (10, 10))
        screen.blit(player_2, (10, 50))
        screen.blit(player_3, (640, 10))
        screen.blit(player_4, (640, 50))
        screen.blit(fin, (0, 200))
        screen.blit(win, (124, 200))
        screen.blit(instructions, (180, 400))

        pygame.display.flip()
        clock.tick(fps)
