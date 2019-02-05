import pygame
from pygame.locals import *
import pygameMenu
from pygameMenu.locals import *
import os
from memory import *
import numpy as np

# Menue aus: https://github.com/ppizarror/pygame-menu

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

game_size = ''

player_num = 2


# !!!!!!!!!!!!!!!! hier weiter machen lol
#
#
#
#
#
#
#
#
#
#
#

players = np.array([1, 2, 3, 4])

def change_player_num(n):

    print ('Selected number: {0}'.format(n))
    return players[n]


'''
# set number of players
def set_num_players(num):
    print ('Selected number: {0}'.format(num))
    player_num[0] = num

# set size of field (4x4, 6x6, 8x8?)
def set_field_size(game_size):
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

# !!!!!!!!!!!!!!!! hier weiter machen lol
#
#
#
#
#
#
#
#
#
#
#
#
player_menu.add_selector('Select Number', [('1 Player', 1),
                                             ('2 Players', 2),
                                             ('3 Players', 3),
                                           ('4 Players', 4)],
                       onreturn=None,
                       onchange=change_player_num(2))


#player_menu.add_option('1 Player', set_num_players, player_num,
#                    pygame.font.Font(pygameMenu.fonts.FONT_FRANCHISE, 30))

#player_menu.add_option('1 Player', set_num_players(1))
'''
player_menu.add_option('2 Players', set_num_players(2))
player_menu.add_option('3 Players', set_num_players(3))
player_menu.add_option('4 Players', set_num_players(4))
'''


'''
player_menu.add_selector('Select Number of Players', [('1 Player', '1'),
                                             ('2 Players', '2'),
                                             ('3 Players', '3'),
                                                      ('4 Players', '4')],
                       onreturn=None,
                       onchange=set_num_players(2))
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
Play_Info_Size = 'Size of Field: 4x4'


if player_num != 0:
    Play_Info_Players = 'Number of Players:  ' + str(player_num)
if game_size != '':
    Play_Info_Size = 'Size of Field:  ' + game_size

Play_Info = [Play_Info_Players,
             Play_Info_Size]

for m in Play_Info:
    game_menu.add_line(m)
    game_menu.add_line(PYGAMEMENU_TEXT_NEWLINE)

#game_menu.add_option('Start Game', )

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

