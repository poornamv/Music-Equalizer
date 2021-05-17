import pygame,sys,os
from pygame.locals import*

black = (0,0,0)
pygame.init()

window = pygame.display.set_mode((500,500))
pygame.display.set_caption("Music Equaliser")

screen = pygame.display.get_surface()
screen.fill(black)
pygame.display.set_caption("Music Equaliser")


while True :
    for event in pygame.event.get():
        print(event)
        if event.type == QUIT :
            pygame.quit()
            sys.exit()
        pygame.display.update()