import pygame
from pygame.locals import *
import random
import pygameMenu
from pygameMenu.locals import *
import os
from memory_assets import *


orange = (255, 165, 0)
black = (0, 0, 0)
white = (255, 255, 255)
lightblue = (173, 216, 230)
fps = 60.0
menu_background = (190, 190, 190)
screen_width = 800
screen_height = 640
screen_size = (screen_width, screen_height)
clock = pygame.time.Clock()

pygame.init()
os.environ['SDL_VIDEO_CENTERED'] = '1'

# Create screen and objects
surface = pygame.display.set_mode(screen_size)
screen = pygame.display.set_mode([screen_width, screen_height])
pygame.display.set_caption('Fruit Memory')
clock = pygame.time.Clock()
dt = 1 / fps

player_num = 0
game_size = ''

# functions for game

'''
Functions
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
                            win = win_font.render(who_won(), True, white, grey)
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
                            win = win_font.render(who_won(), True, white, grey)
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
                            win = win_font.render(who_won(), True, white, grey)
                            instructions = instructions_font.render('Press R to restart | Press Q to quit | Press M to'
                                                                    + ' return to Menu', True, black, grey)
                    elif check_cards(card_1, card_2) is False:
                        player_counter += 1
                        if player_counter == 5:
                            player_counter = 1
                        repaint_player(player_counter)
            counter += 1


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
                print "card " + str(counter) + " clicked"
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

                    print "2 cards chosen!"
                    if check_cards(card_1, card_2) is True:
                        print "right pick!"
                        rectangles6x6[card_1].move_ip(0, 2000)
                        rectangles6x6[card_2].move_ip(0, 2000)
                        score_1 += 10
                        score_overall += 10
                        player_1 = score_font.render('Player 1: ' + str(score_1), False, navy_blue)
                        chosen = 0

                        if score_overall == 180:
                            fin = fin_font.render('All fruits found!', True, white, grey)
                            instructions = instructions_font.render('Press R to restart | Press Q to quit | Press M to'
                                                                    + ' return to Menu', True, black, grey)

            counter += 1

    if no_of_player == 2:
        for i in rectangles6x6:
            if i.collidepoint(mouse):
                print "card " + str(counter) + " clicked"
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

                    print "2 cards chosen!"
                    if check_cards(card_1, card_2) is True:
                        print "right pick!"
                        rectangles6x6[card_1].move_ip(0, 2000)
                        rectangles6x6[card_2].move_ip(0, 2000)
                        score_player(player_counter)
                        score_overall += 10
                        repaint_player(player_counter)
                        chosen = 0

                        if score_overall == 180:
                            win = win_font.render(who_won(), True, white, grey)
                            instructions = instructions_font.render('Press R to restart | Press Q to quit | Press M to'
                                                                    + ' return to Menu', True, black, grey)
                    elif check_cards(card_1, card_2) is False:
                        player_counter += 1
                        if player_counter == 3:
                            player_counter = 1
                        repaint_player(player_counter)
            counter += 1

    if no_of_player == 3:
        for i in rectangles6x6:
            if i.collidepoint(mouse):
                print "card " + str(counter) + " clicked"
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

                    print "2 cards chosen!"
                    if check_cards(card_1, card_2) is True:
                        print "right pick!"
                        rectangles6x6[card_1].move_ip(0, 2000)
                        rectangles6x6[card_2].move_ip(0, 2000)
                        score_player(player_counter)
                        score_overall += 10
                        repaint_player(player_counter)
                        chosen = 0

                        if score_overall == 180:
                            win = win_font.render(who_won(), True, white, grey)
                            instructions = instructions_font.render('Press R to restart | Press Q to quit | Press M to'
                                                                    + ' return to Menu', True, black, grey)
                    elif check_cards(card_1, card_2) is False:
                        player_counter += 1
                        if player_counter == 4:
                            player_counter = 1
                        repaint_player(player_counter)
            counter += 1

    if no_of_player == 4:
        for i in rectangles6x6:
            if i.collidepoint(mouse):
                print "card " + str(counter) + " clicked"
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

                    print "2 cards chosen!"
                    if check_cards(card_1, card_2) is True:
                        print "right pick!"
                        rectangles6x6[card_1].move_ip(0, 2000)
                        rectangles6x6[card_2].move_ip(0, 2000)
                        score_player(player_counter)
                        score_overall += 10
                        repaint_player(player_counter)
                        chosen = 0

                        if score_overall == 180:
                            win = win_font.render(who_won(), True, white, grey)
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


def close_cards4x4():
    global card_1
    global card_2
    rectangles4x4[card_1].move_ip(-70, 0)
    rectangles4x4[card_2].move_ip(-70, 0)


def close_cards6x6():
    global card_1
    global card_2
    rectangles6x6[card_1].move_ip(-2000, 0)
    rectangles6x6[card_2].move_ip(-2000, 0)


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
    elif c1 == 16 and c2 == 17 or c1 == 17 and c2 == 16:
        return True
    elif c1 == 18 and c2 == 19 or c1 == 19 and c2 == 18:
        return True
    elif c1 == 20 and c2 == 21 or c1 == 21 and c2 == 20:
        return True
    elif c1 == 22 and c2 == 23 or c1 == 23 and c2 == 22:
        return True
    elif c1 == 24 and c2 == 25 or c1 == 25 and c2 == 24:
        return True
    elif c1 == 26 and c2 == 27 or c1 == 27 and c2 == 26:
        return True
    elif c1 == 28 and c2 == 29 or c1 == 29 and c2 == 28:
        return True
    elif c1 == 30 and c2 == 31 or c1 == 31 and c2 == 30:
        return True
    elif c1 == 32 and c2 == 33 or c1 == 33 and c2 == 32:
        return True
    elif c1 == 34 and c2 == 35 or c1 == 35 and c2 == 34:
        return True
    else:
        return False


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
    random.shuffle(random_positions)




'''
# set number of players
def set_num_players(player_num):


# set size of field (4x4, 6x6, 8x8?)
def set_field_size(game_size):


# start game
def play_function(p_num, g_size):

    set_num_players(p_num)
    set_field_size(g_size)

    
    main_menu.disable()
    main_menu.reset(1)
    

    while True:

        clock.tick(60)

        # Application events
        playevents = pygame.event.get()
        for e in playevents:
            if e.type == QUIT:
                exit()
            elif e.type == KEYDOWN:
                if e.key == K_ESCAPE and main_menu.is_disabled():
                    main_menu.enable()

                    # Quit this function, then skip to loop of main-menu on line 217
                    return

        # Pass events to main_menu
        main_menu.mainloop(playevents)
        
        # Continue playing
        surface.fill(bg_color)
        surface.blit(f, ((WINDOW_SIZE[0] - f_width) / 2, WINDOW_SIZE[1] / 2))
        pygame.display.flip()
        
'''
def main_background():
    surface.fill(orange)


# Menu for changing size of field
size_menu = pygameMenu.Menu(surface,
                            bgfun=main_background,
                            color_selected=white,
                            font=pygameMenu.fonts.FONT_BEBAS,
                            font_color=white,
                            font_size=30,
                            menu_alpha=100,
                            menu_color=menu_background,
                            menu_height=int(screen_height * 0.6),
                            menu_width=int(screen_width * 0.6),
                            onclose=PYGAME_MENU_DISABLE_CLOSE,
                            option_shadow=False,
                            title='Select Size of Field',
                            window_height=screen_height,
                            window_width=screen_width
                            )
'''
size_menu.add_option('Start', play_function, DIFFICULTY,
                     pygame.font.Font(pygameMenu.fonts.FONT_FRANCHISE, 30))
size_menu.add_selector('Select Size of Field', [('Small', 'SMALL'),
                      ('Medium', 'MEDIUM'),
                      ('Large', 'LARGE')],
                      onreturn=None,
                      onchange=change_difficulty)
'''
size_menu.add_option('Return to main menu', PYGAME_MENU_BACK)

# Menu for changing number of players
player_menu = pygameMenu.TextMenu(surface,
                                  bgfun=main_background,
                                  color_selected=white,
                                  font=pygameMenu.fonts.FONT_BEBAS,
                                  font_color=white,
                                  font_size=30,
                                  menu_alpha=100,
                                  menu_color=menu_background,
                                  menu_height=int(screen_height * 0.6),
                                  menu_width=int(screen_width * 0.6),
                                  onclose=PYGAME_MENU_DISABLE_CLOSE,
                                  option_shadow=False,
                                  title='Select Number',
                                  window_height=screen_height,
                                  window_width=screen_width
                                  )

'''
player_menu.add_option('Start', play_function, DIFFICULTY,
                     pygame.font.Font(pygameMenu.fonts.FONT_FRANCHISE, 30))
player_menu.add_selector('Select Size of Field', [('Small', 'SMALL'),
                      ('Medium', 'MEDIUM'),
                      ('Large', 'LARGE')],
                      onreturn=None,
                      onchange=change_difficulty)
                      '''
player_menu.add_option('Return to main menu', PYGAME_MENU_BACK)

# Menu for starting game
game_menu = pygameMenu.TextMenu(surface,
                                bgfun=main_background,
                                color_selected=white,
                                font=pygameMenu.fonts.FONT_BEBAS,
                                font_color=white,
                                font_size=30,
                                menu_alpha=100,
                                menu_color=menu_background,
                                menu_height=int(screen_height * 0.6),
                                menu_width=int(screen_width * 0.6),
                                onclose=PYGAME_MENU_DISABLE_CLOSE,
                                option_shadow=False,
                                title='Start Game',
                                window_height=screen_height,
                                window_width=screen_width
                                )

# Zu Machen: Dieser Text wird nur gezeigt, falls keine anderen Einstellungen im Menu vorgenommen
# Ansonsten wird hier die Auswahl des Users aus den anderen Menus gezeigt


Play_Info_Players = 'Number of Players: 2'
Play_Info_Size = 'Size of Field: Small'

if player_num != 0:
    Play_Info_Players = 'Number of Players:  ' + player_num
if game_size != '':
    Play_Info_Size = 'Size of Field:  ' + game_size

Play_Info = [Play_Info_Players,
             Play_Info_Size]

for m in Play_Info:
    game_menu.add_line(m)
    game_menu.add_line(PYGAMEMENU_TEXT_NEWLINE)

# game_menu.add_option('Start Game', )
# game_menu.add_option('Start Game', play_function, DIFFICULTY,
#                     pygame.font.Font(pygameMenu.fonts.FONT_FRANCHISE, 30))
# game_menu.add_option('Start Game', play_function(player_num, game_size))
game_menu.add_option('Return to menu', PYGAME_MENU_BACK)


main_menu = pygameMenu.Menu(surface,
                            bgfun=main_background,
                            color_selected=white,
                            font=pygameMenu.fonts.FONT_BEBAS,
                            font_color=white,
                            font_size=30,
                            menu_alpha=100,
                            menu_color=menu_background,
                            menu_height=int(screen_height * 0.6),
                            menu_width=int(screen_width * 0.6),
                            onclose=PYGAME_MENU_DISABLE_CLOSE,
                            option_shadow=False,
                            title='Fruit Memory',
                            window_height=screen_height,
                            window_width=screen_width
                            )


main_menu.add_option('Start Game', game_menu)
main_menu.add_option('Number of Players', player_menu, pygame.font.Font(pygameMenu.fonts.FONT_FRANCHISE, 30))
main_menu.add_option('Size of Field', size_menu, pygame.font.Font(pygameMenu.fonts.FONT_FRANCHISE, 30))
main_menu.add_option('Quit Game', PYGAME_MENU_EXIT)

'''
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


#
def draw_fruit(i, (x, y)):
    surface.blit(fruits[i], (x, y))


def draw_fruits_random():
    for i in range(16):
        draw_fruit(i, random_pos[i])
'''

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


# Main loop
while True:

    # Tick
    clock.tick(60)

    # Application events
    events = pygame.event.get()
    for event in events:
        if event.type == QUIT:
            exit()

    # Main menu
    main_menu.mainloop(events)

    # Flip surface
    pygame.display.flip()

