import pygame as py
from pygame.locals import *
from random import randint
from sys import exit

#CORES
WHITE = (255,255,255)
BLACK = (0,0,0)
CYAN = (0,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
PURPLE = (255,0,255)
PINK = (255,203,219)
ORANGE = (255,165,0)
LAVENDER = (230,230,250)
COLORS = (CYAN, RED, GREEN, BLUE, PURPLE, PINK, ORANGE, LAVENDER)

#TELA
width = 680
height = 400
screen = py.display.set_mode((width, height))
py.display.set_caption('COLLISION')

#CONFIGURATIONS
py.init()
clock = py.time.Clock()
running = True
points = 0
font = py.font.SysFont('arial', 20, bold=True, italic=True)

#MUSIC AND SOUND
back_music = py.mixer.music.load('./Musics/back_song.mp3')
py.mixer.music.play(-1)
sound = py.mixer.Sound('./Musics/sound_collision.mp3')

#SQUARE
sqr_side = 40
sqr_x = (width/2) - (sqr_side/2)
sqr_y = (height/2) - (sqr_side/2)
sqr_color = CYAN

#RECTANGULE
rct_width = 10
rct_height = 20
rct_x = randint(50, width - 50)
rct_y = randint(50, height - 50)
rct_color = RED

#ENEMIES
enm_size = 10
enm_color = BLACK
enm = [
    {'x': 0, 'y': 100, 'vel': 5, 'obj': 0, 'img': 0}, 
    {'x': width - enm_size, 'y': 300, 'vel': -5, 'obj': 0, 'img': 0}, 
    {'x': 200, 'y': 0, 'vel': 5, 'obj': 0, 'img': 0}, 
    {'x': 480, 'y': height - enm_size, 'vel': -5, 'obj': 0, 'img': 0}
]

while running:
    clock.tick(30)
    screen.fill(WHITE)

    conq = points >= 20
    msg = f'Pontos: {points}'
    text = font.render(msg, True, BLACK)

    #CRIANDO ÁREAS
    rectangule = py.Rect(rct_x, rct_y, rct_width, rct_height)
    square = py.Rect(sqr_x, sqr_y, sqr_side, sqr_side)
    for i in range(0,4):
        if not (i > 1 and conq):
            enm[i]['obj'] = py.Rect(enm[i]['x'], enm[i]['y'], enm_size, enm_size)

    #EVENTOS    
    event = py.event.poll()
    if event.type == QUIT:
        py.quit()
        exit()

    #MOVIMENTO
    if py.key.get_pressed()[K_a]:
        sqr_x = sqr_x - 15
    elif py.key.get_pressed()[K_d]:
        sqr_x = sqr_x + 15
    elif py.key.get_pressed()[K_s]:
        sqr_y = sqr_y + 15
    elif py.key.get_pressed()[K_w]:
        sqr_y = sqr_y - 15
    
    if sqr_x >= width:
        sqr_x = 0
    elif sqr_x <= -sqr_side:
        sqr_x = width - sqr_side
    elif sqr_y >= height:
        sqr_y = 0
    elif sqr_y <= -sqr_side:
        sqr_y = height - sqr_side

    #CONFERINDO COLISÃO
    if square.colliderect(rectangule):
        rct_x = randint(50, width - 50)
        rct_y = randint(50, height - 50)
        
        color = randint(0,len(COLORS) - 1)
        sqr_color = COLORS[color]
        color = randint(0,len(COLORS) - 1)
        rct_color = COLORS[color]
        
        points += 1
        sound.play()  

        for i in range(0,4):
            if enm[i]['vel'] > 0:
                enm[i]['vel'] += 2
            else:
                enm[i]['vel'] -= 2

    for i in range(0,4):
        if not (conq and i > 1):
            if square.colliderect(enm[i]['obj']) :
                running = False

    #DESENHANDO ÁREAS
    sqr_image = py.draw.rect(screen, sqr_color, square)
    rct_image = py.draw.rect(screen, rct_color, rectangule)
    for i in range(0,4):
        if not (conq and i > 1):    
            enm[i]['img'] = py.draw.rect(screen, enm_color, enm[i]['obj'])

    screen.blit(text, (500, 50))

    #MOVIMENTO 
    for i in range(0,4):
        if enm[i]['x'] > width:
            enm[i]['x'] = 0
        elif enm[i]['x'] < -enm_size:
            enm[i]['x'] = width - enm_size
        elif enm[i]['y'] > height:
            enm[i]['y'] = 0
        elif enm[i]['y'] < -enm_size:
            enm[i]['y'] = height - enm_size

    py.display.update()
py.mixer.music.stop()


    

