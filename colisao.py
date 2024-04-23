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
COLORS = (BLACK, CYAN, RED, GREEN, BLUE, PURPLE, PINK, ORANGE, LAVENDER)


#TELA
width = 680
height = 400
screen = py.display.set_mode((width, height))
py.display.set_caption('O JOGO')

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
while running:
    clock.tick(30)
    screen.fill(WHITE)

    msg = f'Pontos: {points}'
    text = font.render(msg, True, BLACK)

    #Criando áreas
    rectangule = py.Rect(rct_x, rct_y, rct_width, rct_height)
    square = py.Rect(sqr_x, sqr_y, sqr_side, sqr_side)

    event = py.event.poll()
    if event.type == QUIT:
        py.quit()
        exit()

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
    
    #Conferindo colisão
    if square.colliderect(rectangule):
        rct_x = randint(50, width - 50)
        rct_y = randint(50, height - 50)
        color = randint(0,len(COLORS) - 1)
        sqr_color = COLORS[color]
        color = randint(0,len(COLORS) - 1)
        rct_color = COLORS[color]
        sound.play()
        points += 1
    
    #Desenhando área
    sqr_image = py.draw.rect(screen, sqr_color, square)
    rct_image = py.draw.rect(screen, rct_color, rectangule)
    
    screen.blit(text, (500, 50))

    py.display.update()



    

