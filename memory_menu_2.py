import pygame
from pygame.locals import *
import pygameMenu
from pygameMenu.locals import *
import os
from memory import *

# menu from https://github.com/ppizarror/pygame-menu
# inspired by example menu: https://github.com/ppizarror/pygame-menu/blob/master/example2.py


# ----- variables

# constants
orange = (255, 190, 50)
black = (0, 0, 0)
white = (255, 255, 255)
fps = 30.0
menu_background = (200, 200, 200)
screen_width = 800
screen_height = 640
screen_size = (screen_width, screen_height)
clock = pygame.time.Clock()

# init pygame
pygame.init()
os.environ['SDL_VIDEO_CENTERED'] = '1'

# screen and objects
surface = pygame.display.set_mode(screen_size)
screen = pygame.display.set_mode([screen_width, screen_height])
pygame.display.set_caption('Fruit Memory')
clock = pygame.time.Clock()
dt = 1 / fps

# sets player number and field to initial values
PLAYERS = [1]
FIELD = ['4x4']


# ----- functions

# prints the selected number of players
def change_player_num(n):
    print ('Selected number of players: {0}'.format(n))
    PLAYERS[0] = n


# prints the selected size of field
def change_field_size(f):
    print ('Selected size of field: {0}'.format(f))
    FIELD[0] = f


def main_background():
    surface.fill(orange)


# sets game according to chosen parameters
def game_function(players, field):

    players = players[0]
    field = field[0]

    assert isinstance(players, int)
    assert isinstance(field, str)

    if field == '4x4':
        if 1 <= players <= 4:
            memory4x4(players)
        else:
            raise Exception('Unknown number of players {0}.'.format(players))

    elif field == '6x6':
        if 1 <= players <= 4:
            memory6x6(players)
        else:
            raise Exception('Unknown number of players {0}.'.format(players))
    else:
        raise Exception('Unknown field size {0}.'.format(field))

    main_menu.disable()
    main_menu.reset(1)


# ----- menu

# menu for choosing number of players and field size
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

# start game of memory with chosen players and field size
main_menu.add_option('Start', game_function, PLAYERS, FIELD)

# select number of players from 1 to 4
main_menu.add_selector('Select Number', [('1 Player', 1),
                                         ('2 Players', 2),
                                         ('3 Players', 3),
                                         ('4 Players', 4)],
                       onreturn=None,
                       onchange=change_player_num)

# select size of playing field, either 4x4 or 6x6
main_menu.add_selector('Select Size', [('4x4', '4x4'),
                                       ('6x6', '6x6')],
                       onreturn=None,
                       onchange=change_field_size)

# closes game window
main_menu.add_option('Quit Game', PYGAME_MENU_EXIT)


# ----- main loop

while True:

    clock.tick(30)

    events = pygame.event.get()
    for event in events:
        if event.type == QUIT:
            exit()

    # menu of game
    main_menu.mainloop(events)

    pygame.display.flip()

