import pygame
from enum import IntEnum

FPS = 60

pygame.init()

WIDTH = 1000
HEIGHT = 800

window = pygame.display.set_mode((WIDTH,HEIGHT))
bg_img = pygame.image.load('background.jpg')
bg_img = pygame.transform.scale(bg_img,(WIDTH,HEIGHT))

clock = pygame.time.Clock()
 
i = 0
runing = True

class Direction(IntEnum):
    LEFT = -1
    RIGHT = 1

direction = Direction.LEFT

while runing:
    clock.tick(FPS)

    window.fill((0,0,0))
    window.blit(bg_img,(i,0))
    
    window.blit(bg_img,(-WIDTH+i,0))
    window.blit(bg_img,(WIDTH+i,0))

    if (i==(WIDTH * direction)):
        window.blit(bg_img,((WIDTH * direction) + i,0))
        i=0
    i+= (1 * direction)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runing = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                direction = Direction.RIGHT
            if event.key == pygame.K_RIGHT:
                direction = Direction.LEFT
            if event.key == pygame.K_q:
                runing = False

    pygame.display.update()
pygame.quit()
 