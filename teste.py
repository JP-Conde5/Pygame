import pygame as py


#inicializa o módulo, premitindo que seja interpretado
py.init()

width = 640
high = 480
#determina o tamanho da tela
screen = py.display.set_mode((width, high))

#cria objeto do tipo clock
clock = py.time.Clock()
running = True

while running:
    #percorre os eventos possíveis do pygame
    for event in py.event.get():
        #se o evento for o QUIT, para a loop
        if event.type == py.QUIT:
           running = False 
    #preenche a tela
    screen.fill((255,255,255))
    #
    py.display.flip()
    #determina o número de frames
    clock.tick(60)

