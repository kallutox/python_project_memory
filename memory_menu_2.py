import pygame
from pygame.locals import *
import pygameMenu
from pygameMenu.locals import *
import os
from memory import *
import numpy as np

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

pygame.init()
os.environ['SDL_VIDEO_CENTERED'] = '1'

# Create screen and objects
surface = pygame.display.set_mode(screen_size)
screen = pygame.display.set_mode([screen_width, screen_height])
pygame.display.set_caption('Fruit Memory')
clock = pygame.time.Clock()
dt = 1 / fps

game_size = '4x4'
player_num = 2


players = np.array([1, 2, 3, 4])

'''
def change_num(n):
    print ('Selected number: {0}'.format(n))
    return players[n]
'''

def change_player_num(n):
    return n


def change_field_size(size):
    return size


def main_background():
    surface.fill(orange)


# menu for starting the  game
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
'''
# default, will be changed later
Play_Info_Players = 'Number of Players: 2'
Play_Info_Size = 'Size of Field: 4x4'


if player_num != 0:
    Play_Info_Players = 'Number of Players Selected:  ' + str(change_player_num(player_num))
if game_size != '':
    Play_Info_Size = 'Size of Field Selected:  ' + str(change_field_size(game_size))
'''

Play_Info_Players = 'Number of Players Selected:  ' + str(change_player_num(player_num))
Play_Info_Size = 'Size of Field Selected:  ' + str(change_field_size(game_size))

Play_Info = [Play_Info_Players,
             Play_Info_Size]

for m in Play_Info:
    game_menu.add_line(m)
    game_menu.add_line(PYGAMEMENU_TEXT_NEWLINE)

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
main_menu.add_selector('Select Number', [('1 Player', 1),
                                             ('2 Players', 2),
                                             ('3 Players', 3),
                                           ('4 Players', 4)],
                       onreturn=None,
                       onchange=change_player_num(2))

main_menu.add_selector('Select Size', [('4 x 4', 1),
                                             ('6 x 6', 2)],
                       onreturn=None,
                       onchange=change_player_num(2))

main_menu.add_option('Quit Game', PYGAME_MENU_EXIT)


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

