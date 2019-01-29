import pygame
from pygame.locals import *
import random
import pygameMenu
from pygameMenu.locals import *
import os
import sys

orange = (255, 165, 0)
black = (0, 0, 0)
white = (255, 255, 255)
fps = 60.0
menu_background = (190, 190, 190)
screen_width = 800
screen_height = 640
screen_size = (screen_width, screen_height)
clock = pygame.time.Clock()

pygame.init()
os.environ['SDL_VIDEO_CENTERED'] = '1'

# Create pygame screen and objects
surface = pygame.display.set_mode(screen_size)
pygame.display.set_caption('Fruit Memory')
clock = pygame.time.Clock()
dt = 1 / fps



def main_background():
    surface.fill(orange)


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
play_menu.add_option('Return to main menu', PYGAME_MENU_BACK)
'''

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
player_menu.add_option('Return to main menu', PYGAME_MENU_BACK)
'''

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


#main_menu.add_option('Start Game', )
main_menu.add_option('Number of Players', player_menu, pygame.font.Font(pygameMenu.fonts.FONT_FRANCHISE, 30))
main_menu.add_option('Size of Field', size_menu, pygame.font.Font(pygameMenu.fonts.FONT_FRANCHISE, 30))
main_menu.add_option('Quit Game', PYGAME_MENU_EXIT)



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

