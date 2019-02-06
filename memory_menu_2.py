import pygame
from pygame.locals import *
import pygameMenu
from pygameMenu.locals import *
import os
from memory import *

# menu from https://github.com/ppizarror/pygame-menu
# inspired by example menu: https://github.com/ppizarror/pygame-menu/blob/master/example2.py

orange = (255, 165, 0)
black = (0, 0, 0)
white = (255, 255, 255)
lightblue = (173, 216, 230)
fps = 30.0
menu_background = (190, 190, 190)
screen_width = 800
screen_height = 640
screen_size = (screen_width, screen_height)
clock = pygame.time.Clock()

# init pygame
pygame.init()
os.environ['SDL_VIDEO_CENTERED'] = '1'

# create screen and objects
surface = pygame.display.set_mode(screen_size)
screen = pygame.display.set_mode([screen_width, screen_height])
pygame.display.set_caption('Fruit Memory')
clock = pygame.time.Clock()
dt = 1 / fps


'''
game_size = '4x4'
player_num = 2
'''

PLAYERS = [1]
FIELD = ['4x4']


# functions
def change_player_num(n):
    print ('Selected number: {0}'.format(n))
    PLAYERS[0] = n


def change_field_size(f):
    print ('Selected size: {0}'.format(f))
    FIELD[0] = f


def main_background():
    surface.fill(orange)


def game_function(players, field):

    players = players[0]
    field = field[0]

    assert isinstance(players, int)
    assert isinstance(field, str)

    if field == '4x4':
        if players == 1 or players == 2 or players == 3 or players == 4:
            memory4x4(players)
        else:
            raise Exception('Unknown number of players {0}.'.format(players))

    elif field == '6x6':
        if players == 1 or players == 2 or players == 3 or players == 4:
            memory6x6(players)
        else:
            raise Exception('Unknown number of players {0}.'.format(players))
    else:
        raise Exception('Unknown field size {0}.'.format(field))

    main_menu.disable()
    main_menu.reset(1)

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

main_menu.add_option('Start', game_function, PLAYERS, FIELD)
main_menu.add_selector('Select Number', [('1 Player', 1),
                                         ('2 Players', 2),
                                         ('3 Players', 3),
                                         ('4 Players', 4)],
                       onreturn=None,
                       onchange=change_player_num)

main_menu.add_selector('Select Size', [('4x4', '4x4'),
                                       ('6x6', '6x6')],
                       onreturn=None,
                       onchange=change_field_size)

main_menu.add_option('Quit Game', PYGAME_MENU_EXIT)


# Main loop
while True:

    # Tick
    clock.tick(30)

    # Application events
    events = pygame.event.get()
    for event in events:
        if event.type == QUIT:
            exit()

    # Main menu
    main_menu.mainloop(events)

    # Flip surface
    pygame.display.flip()

