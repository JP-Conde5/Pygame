import pygame as py
from pygame.locals import *
from random import randint

#CORES
WHITE = (255,255,255)
BLACK = (0,0,0)
CYAN = (0,255,255)
RED = (0,0,0)

#TELA
width = 680
height = 400
screen = py.display.set_mode((width, height))
py.display.set_caption('O JOGO')

#SQUARE
sqr_side = 40
sqr_x = (width/2) - (sqr_side/2)
sqr_y = (height/2) - (sqr_side/2)
square = py.Rect(sqr_x, sqr_y, sqr_side, sqr_side)

#RECTANGULE
rct_width = 10
rct_height = 20
rct_x = randint(50, width - 50)
rct_y = randint(50, height - 50)
rectangule = py.Rect(rct_x, rct_y, rct_width, rct_height)

#CONFIGURATIONS
clock = py.time.Clock()
running = True

while running:
    clock.tick(30)
    screen.fill(WHITE)
    
    event = py.event.poll()
    if event.type == QUIT:
        running = False
    
    if py.key.get_pressed()[K_a]:
        py.Rect.move_ip(square, -10, 0)
    elif py.key.get_pressed()[K_d]:
        py.Rect.move_ip(square, 10, 0)
    elif py.key.get_pressed()[K_s]:
        py.Rect.move_ip(square, 0, 10)
    elif py.key.get_pressed()[K_w]:
        py.Rect.move_ip(square, 0, -10)
    
    if sqr_x >= width:
        py.Rect.move_ip(square, 0, 0)
    elif sqr_x <= -sqr_side:
        py.Rect.move_ip(square, width - sqr_side, 0)
    elif sqr_y >= height:
        py.Rect.move_ip(square, 0, 0)
    elif sqr_y <= -sqr_side:
        py.Rect.move_ip(square, 0, width - sqr_side)
    
    if square.colliderect(rectangule):
        rct_x = randint(50, width - 50)
        rct_y = randint(50, height - 50)
        py.Rect.move_ip(rectangule, rct_x, rct_y)

    sqr_image = py.draw.rect(screen, CYAN, square)
    rct_image = py.draw.rect(screen, RED, rectangule)
    
    py.display.update()



    

