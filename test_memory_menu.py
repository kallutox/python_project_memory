# coding=utf-8

# Import pygame and libraries
from pygame.locals import *
from random import randrange
import os
import pygame
from memory import *

# Import pygameMenu
import pygameMenu
from pygameMenu.locals import *

COLOR_BACKGROUND = (128, 0, 128)
COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)
FPS = 60.0
MENU_BACKGROUND_COLOR = (228, 55, 36)
WINDOW_SIZE = (640, 480)

####################################################################
# Init pygame
pygame.init()
os.environ['SDL_VIDEO_CENTERED'] = '1'

# Create pygame screen and objects
surface = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption('PygameMenu example 2')
clock = pygame.time.Clock()
dt = 1 / FPS

# Global variables
DIFFICULTY = ['EASY']
####################################################################

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


################################################################################

def change_difficulty(d):
    """
    Change difficulty of the game.

    :return:
    """

    print ('Selected difficulty: {0}'.format(d))
    DIFFICULTY[0] = d


def random_color():
    """
    Return random color.

    :return: Color tuple
    """
    return randrange(0, 255), randrange(0, 255), randrange(0, 255)


def play_function(difficulty, font):
    """
    Main game function

    :param difficulty: Difficulty of the game
    :param font: Pygame font
    :return: None
    """

    difficulty = difficulty[0]
    assert isinstance(difficulty, str)

    if difficulty == 'EASY':
        f = font.render('Playing as baby', 1, COLOR_WHITE)
    elif difficulty == 'MEDIUM':
        f = font.render('Playing as normie', 1, COLOR_WHITE)
    elif difficulty == 'HARD':
        f = font.render('Playing as god', 1, COLOR_WHITE)
    else:
        raise Exception('Unknown difficulty {0}'.format(difficulty))

    # Draw random color and text
    bg_color = random_color()
    f_width = f.get_size()[0]

    # Reset main menu and disable
    # You also can set another menu, like a 'pause menu', or just use the same
    # main_menu as the menu that will check all your input.
    main_menu.disable()
    main_menu.reset(1)

    while True:

        # Clock tick
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


def main_background():
    """
    Function used by menus, draw on background while menu is active.

    :return: None
    """
    surface.fill(COLOR_BACKGROUND)
################################################################################

PLAYERS = ['2 Players']
FIELD = ['4x4']


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
        if players == [1, 4]:
            memory4x4(players)
        else:
            raise Exception('Unknown number of players {0}.'.format(players))

    elif field == '6x6':
        if players == [1, 4]:
            memory6x6(players)
        else:
            raise Exception('Unknown number of players {0}.'.format(players))
    else:
        raise Exception('Unknown field size {0}.'.format(field))

    main_menu.disable()
    main_menu.reset(1)

    '''
    while True:

        # Clock tick
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


# -----------------------------------------------------------------------------
# PLAY MENU
play_menu = pygameMenu.Menu(surface,
                            bgfun=main_background,
                            color_selected=COLOR_WHITE,
                            font=pygameMenu.fonts.FONT_BEBAS,
                            font_color=COLOR_BLACK,
                            font_size=30,
                            menu_alpha=100,
                            menu_color=MENU_BACKGROUND_COLOR,
                            menu_height=int(WINDOW_SIZE[1] * 0.6),
                            menu_width=int(WINDOW_SIZE[0] * 0.6),
                            onclose=PYGAME_MENU_DISABLE_CLOSE,
                            option_shadow=False,
                            title='Play menu',
                            window_height=WINDOW_SIZE[1],
                            window_width=WINDOW_SIZE[0]
                            )
# When pressing return -> play(DIFFICULTY[0], font)
play_menu.add_option('Start', game_function, PLAYERS, FIELD)

play_menu.add_selector('Select difficulty', [('Easy', 'EASY'),
                                             ('Medium', 'MEDIUM'),
                                             ('Hard', 'HARD')],
                       onreturn=None,
                       onchange=change_difficulty)
play_menu.add_option('Return to main menu', PYGAME_MENU_BACK)

# ABOUT MENU
about_menu = pygameMenu.TextMenu(surface,
                                 bgfun=main_background,
                                 color_selected=COLOR_WHITE,
                                 font=pygameMenu.fonts.FONT_BEBAS,
                                 font_color=COLOR_BLACK,
                                 font_size_title=30,
                                 font_title=pygameMenu.fonts.FONT_8BIT,
                                 menu_color=MENU_BACKGROUND_COLOR,
                                 menu_color_title=COLOR_WHITE,
                                 menu_height=int(WINDOW_SIZE[1] * 0.6),
                                 menu_width=int(WINDOW_SIZE[0] * 0.6),
                                 onclose=PYGAME_MENU_DISABLE_CLOSE,
                                 option_shadow=False,
                                 text_color=COLOR_BLACK,
                                 text_fontsize=20,
                                 title='About',
                                 window_height=WINDOW_SIZE[1],
                                 window_width=WINDOW_SIZE[0]
                                 )


# MAIN MENU
main_menu = pygameMenu.Menu(surface,
                            bgfun=main_background,
                            color_selected=COLOR_WHITE,
                            font=pygameMenu.fonts.FONT_BEBAS,
                            font_color=COLOR_BLACK,
                            font_size=30,
                            menu_alpha=100,
                            menu_color=MENU_BACKGROUND_COLOR,
                            menu_height=int(WINDOW_SIZE[1] * 0.6),
                            menu_width=int(WINDOW_SIZE[0] * 0.6),
                            onclose=PYGAME_MENU_DISABLE_CLOSE,
                            option_shadow=False,
                            title='Main menu',
                            window_height=WINDOW_SIZE[1],
                            window_width=WINDOW_SIZE[0]
                            )
main_menu.add_option('Play', play_menu)
main_menu.add_option('About', about_menu)
main_menu.add_option('Quit', PYGAME_MENU_EXIT)

# -----------------------------------------------------------------------------
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
