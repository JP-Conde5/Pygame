import pygame as py
from pygame.locals import *
from random import randint
from sys import exit

#cores
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
CYAN = (0,255,255)

#inicializa o módulo, premitindo que seja interpretado
py.init()

#tela
width = 640
high = 480
#determina o tamanho da tela
screen = py.display.set_mode((width, high))
py.display.set_caption('O JOGO')
#cria objeto do tipo clock
clock = py.time.Clock()
running = True

#desenho do sqr_1
width_1 = 40
x_1 = (width/2) - (width_1/2)
y_1 = (high/2) - (width_1/2)

#desenho do cir_1
radius = 15
x_2 = randint(radius, width - radius)
y_2 = randint(radius, width - radius)
while running:
    #preenche a tela
    screen.fill(WHITE)
    #atualiza toda a página
    #py.display.flip()
    #determina o número de frames
    clock.tick(30)
    #percorre os eventos possíveis do pygame
    #for event in py.event.get():
    event = py.event.poll()
    #se o evento for o QUIT, para a loop
    if event.type == py.QUIT:
        running = False 
    #movimentação (.key dentro de pygame.locals)
    if py.key.get_pressed()[K_a]:
        x_1 = x_1 - 20
    elif py.key.get_pressed()[K_d]:
        x_1 = x_1 + 20
    elif py.key.get_pressed()[K_w]:
        y_1 = y_1 - 20
    elif py.key.get_pressed()[K_s]:
        y_1 = y_1 + 20
    
    #manter na tela
    if x_1 >= width:
        x_1 = 0
    elif x_1 <= -width_1:
        x_1 = width - width_1
    elif y_1 >= width:
        y_1 = 0
    elif y_1 <= -width_1:
        y_1 = width - width_1
        
    #objetos na tela    
    sqr_1 = py.draw.rect(screen, CYAN, (x_1, y_1, width_1, width_1))
    cir_1 = py.draw.circle(screen, RED, (x_2, y_2),radius, 0)
    py.display.update()

    

