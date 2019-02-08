import pygame
import random

'''
Fruits
'''

apfelImg = pygame.image.load('images/apfel.png')
bananeImg = pygame.image.load('images/banane.png')
erdbeereImg = pygame.image.load('images/erdbeere.png')
weintraubeImg = pygame.image.load('images/weintraube.png')
kirscheImg = pygame.image.load('images/kirsche.png')
kiwiImg = pygame.image.load('images/kiwi.png')
orangeImg = pygame.image.load('images/orange.png')
wassermeloneImg = pygame.image.load('images/wassermelone.png')

ananasImg = pygame.image.load('images/6x6/ananas.png')
apfel_rotImg = pygame.image.load('images/6x6/apfel_rot.png')
avocadoImg = pygame.image.load('images/6x6/avocado.png')
birneImg = pygame.image.load('images/6x6/birne.png')
brokkoliImg = pygame.image.load('images/6x6/brokkoli.png')
kokosnuss = pygame.image.load('images/6x6/kokosnuss.png')
pfirsichImg = pygame.image.load('images/6x6/pfirsich.png')
pomeloImg = pygame.image.load('images/6x6/pomelo.png')
tomateImg = pygame.image.load('images/6x6/tomate.png')
zitroneImg = pygame.image.load('images/6x6/zitrone.png')


fruits4x4 = [apfelImg, apfelImg, bananeImg, bananeImg, erdbeereImg, erdbeereImg, weintraubeImg, weintraubeImg,
             kirscheImg, kirscheImg, kiwiImg, kiwiImg, orangeImg, orangeImg, wassermeloneImg, wassermeloneImg]

fruits6x6 = [apfelImg, apfelImg, bananeImg, bananeImg, erdbeereImg, erdbeereImg, weintraubeImg, weintraubeImg,
             kirscheImg, kirscheImg, kiwiImg, kiwiImg, orangeImg, orangeImg, wassermeloneImg, wassermeloneImg,
             ananasImg, ananasImg, apfel_rotImg, apfel_rotImg, avocadoImg, avocadoImg, birneImg, birneImg,
             brokkoliImg, brokkoliImg, kokosnuss, kokosnuss, pfirsichImg, pfirsichImg, pomeloImg, pomeloImg,
             tomateImg, tomateImg, zitroneImg, zitroneImg]


'''
Sound and Music
'''
pygame.mixer.init()

background_music = pygame.mixer.Sound('audio/background_music32kbps.mp3')

coin = pygame.mixer.Sound('audio/coin.wav')
cancel = pygame.mixer.Sound('audio/cancel.wav')
good = pygame.mixer.Sound('audio/good.wav')
start = pygame.mixer.Sound('audio/start.wav')
switch = pygame.mixer.Sound('audio/switch.wav')
wrong = pygame.mixer.Sound('audio/wrong.wav')


'''
Positions 
'''

# Positions 4x4

pos4x4_0 = (120, 100)
pos4x4_1 = (280, 100)
pos4x4_2 = (440, 100)
pos4x4_3 = (600, 100)

pos4x4_4 = (120, 240)
pos4x4_5 = (280, 240)
pos4x4_6 = (440, 240)
pos4x4_7 = (600, 240)

pos4x4_8 = (120, 380)
pos4x4_9 = (280, 380)
pos4x4_10 = (440, 380)
pos4x4_11 = (600, 380)

pos4x4_12 = (120, 520)
pos4x4_13 = (280, 520)
pos4x4_14 = (440, 520)
pos4x4_15 = (600, 520)

pos4x4 = [pos4x4_0, pos4x4_1, pos4x4_2, pos4x4_3, pos4x4_4, pos4x4_5, pos4x4_6, pos4x4_7,
          pos4x4_8, pos4x4_9, pos4x4_10, pos4x4_11, pos4x4_12, pos4x4_13, pos4x4_14, pos4x4_15]

random_pos4x4 = list(pos4x4)
random.shuffle(random_pos4x4)


# Positions 6x6

pos6x6_0 = (100, 100)
pos6x6_1 = (205, 100)
pos6x6_2 = (310, 100)
pos6x6_3 = (415, 100)
pos6x6_4 = (520, 100)
pos6x6_5 = (625, 100)

pos6x6_6 = (100, 185)
pos6x6_7 = (205, 185)
pos6x6_8 = (310, 185)
pos6x6_9 = (415, 185)
pos6x6_10 = (520, 185)
pos6x6_11 = (625, 185)

pos6x6_12 = (100, 270)
pos6x6_13 = (205, 270)
pos6x6_14 = (310, 270)
pos6x6_15 = (415, 270)
pos6x6_16 = (520, 270)
pos6x6_17 = (625, 270)

pos6x6_18 = (100, 355)
pos6x6_19 = (205, 355)
pos6x6_20 = (310, 355)
pos6x6_21 = (415, 355)
pos6x6_22 = (520, 355)
pos6x6_23 = (625, 355)

pos6x6_24 = (100, 440)
pos6x6_25 = (205, 440)
pos6x6_26 = (310, 440)
pos6x6_27 = (415, 440)
pos6x6_28 = (520, 440)
pos6x6_29 = (625, 440)

pos6x6_30 = (100, 525)
pos6x6_31 = (205, 525)
pos6x6_32 = (310, 525)
pos6x6_33 = (415, 525)
pos6x6_34 = (520, 525)
pos6x6_35 = (625, 525)


pos6x6 = [pos6x6_0, pos6x6_1, pos6x6_2, pos6x6_3, pos6x6_4, pos6x6_5,
          pos6x6_6, pos6x6_7, pos6x6_8, pos6x6_9, pos6x6_10, pos6x6_11,
          pos6x6_12, pos6x6_13, pos6x6_14, pos6x6_15, pos6x6_16, pos6x6_17,
          pos6x6_18, pos6x6_19, pos6x6_20, pos6x6_21, pos6x6_22, pos6x6_23,
          pos6x6_24, pos6x6_25, pos6x6_26, pos6x6_27, pos6x6_28, pos6x6_29,
          pos6x6_30, pos6x6_31, pos6x6_32, pos6x6_33, pos6x6_34, pos6x6_35]

random_pos6x6 = list(pos6x6)
random.shuffle(random_pos6x6)


'''
Rectangles
'''

properties = (80, 80)

# Rectangles 4x4

rect4x4_0 = pygame.Rect(random_pos4x4[0], properties)
rect4x4_1 = pygame.Rect(random_pos4x4[1], properties)
rect4x4_2 = pygame.Rect(random_pos4x4[2], properties)
rect4x4_3 = pygame.Rect(random_pos4x4[3], properties)

rect4x4_4 = pygame.Rect(random_pos4x4[4], properties)
rect4x4_5 = pygame.Rect(random_pos4x4[5], properties)
rect4x4_6 = pygame.Rect(random_pos4x4[6], properties)
rect4x4_7 = pygame.Rect(random_pos4x4[7], properties)


rect4x4_8 = pygame.Rect(random_pos4x4[8], properties)
rect4x4_9 = pygame.Rect(random_pos4x4[9], properties)
rect4x4_10 = pygame.Rect(random_pos4x4[10], properties)
rect4x4_11 = pygame.Rect(random_pos4x4[11], properties)

rect4x4_12 = pygame.Rect(random_pos4x4[12], properties)
rect4x4_13 = pygame.Rect(random_pos4x4[13], properties)
rect4x4_14 = pygame.Rect(random_pos4x4[14], properties)
rect4x4_15 = pygame.Rect(random_pos4x4[15], properties)

rectangles4x4 = [rect4x4_0, rect4x4_1, rect4x4_2, rect4x4_3, rect4x4_4, rect4x4_5, rect4x4_6, rect4x4_7,
                 rect4x4_8, rect4x4_9, rect4x4_10, rect4x4_11, rect4x4_12, rect4x4_13, rect4x4_14, rect4x4_15]


# Rectangles 6x6

rect6x6_0 = pygame.Rect(random_pos6x6[0], properties)
rect6x6_1 = pygame.Rect(random_pos6x6[1], properties)
rect6x6_2 = pygame.Rect(random_pos6x6[2], properties)
rect6x6_3 = pygame.Rect(random_pos6x6[3], properties)
rect6x6_4 = pygame.Rect(random_pos6x6[4], properties)
rect6x6_5 = pygame.Rect(random_pos6x6[5], properties)

rect6x6_6 = pygame.Rect(random_pos6x6[6], properties)
rect6x6_7 = pygame.Rect(random_pos6x6[7], properties)
rect6x6_8 = pygame.Rect(random_pos6x6[8], properties)
rect6x6_9 = pygame.Rect(random_pos6x6[9], properties)
rect6x6_10 = pygame.Rect(random_pos6x6[10], properties)
rect6x6_11 = pygame.Rect(random_pos6x6[11], properties)

rect6x6_12 = pygame.Rect(random_pos6x6[12], properties)
rect6x6_13 = pygame.Rect(random_pos6x6[13], properties)
rect6x6_14 = pygame.Rect(random_pos6x6[14], properties)
rect6x6_15 = pygame.Rect(random_pos6x6[15], properties)
rect6x6_16 = pygame.Rect(random_pos6x6[16], properties)
rect6x6_17 = pygame.Rect(random_pos6x6[17], properties)

rect6x6_18 = pygame.Rect(random_pos6x6[18], properties)
rect6x6_19 = pygame.Rect(random_pos6x6[19], properties)
rect6x6_20 = pygame.Rect(random_pos6x6[20], properties)
rect6x6_21 = pygame.Rect(random_pos6x6[21], properties)
rect6x6_22 = pygame.Rect(random_pos6x6[22], properties)
rect6x6_23 = pygame.Rect(random_pos6x6[23], properties)

rect6x6_24 = pygame.Rect(random_pos6x6[24], properties)
rect6x6_25 = pygame.Rect(random_pos6x6[25], properties)
rect6x6_26 = pygame.Rect(random_pos6x6[26], properties)
rect6x6_27 = pygame.Rect(random_pos6x6[27], properties)
rect6x6_28 = pygame.Rect(random_pos6x6[28], properties)
rect6x6_29 = pygame.Rect(random_pos6x6[29], properties)

rect6x6_30 = pygame.Rect(random_pos6x6[30], properties)
rect6x6_31 = pygame.Rect(random_pos6x6[31], properties)
rect6x6_32 = pygame.Rect(random_pos6x6[32], properties)
rect6x6_33 = pygame.Rect(random_pos6x6[33], properties)
rect6x6_34 = pygame.Rect(random_pos6x6[34], properties)
rect6x6_35 = pygame.Rect(random_pos6x6[35], properties)

rectangles6x6 = [rect6x6_0, rect6x6_1, rect6x6_2, rect6x6_3, rect6x6_4, rect6x6_5,
                 rect6x6_6, rect6x6_7, rect6x6_8, rect6x6_9, rect6x6_10, rect6x6_11,
                 rect6x6_12, rect6x6_13, rect6x6_14, rect6x6_15, rect6x6_16, rect6x6_17,
                 rect6x6_18, rect6x6_19, rect6x6_20, rect6x6_21, rect6x6_22, rect6x6_23,
                 rect6x6_24, rect6x6_25, rect6x6_26, rect6x6_27, rect6x6_28, rect6x6_29,
                 rect6x6_30, rect6x6_31, rect6x6_32, rect6x6_33, rect6x6_34, rect6x6_35]
