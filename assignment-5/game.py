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


# direction = 'right'

# while runing:
#     clock.tick(FPS)

#     window.fill((0,0,0))
#     window.blit(bg_img,(i,0))
#     if direction == 'right':
#         window.blit(bg_img,(-WIDTH+i,0))

#     if direction == 'left':
#         window.blit(bg_img,(WIDTH-i,0)) 

#     if  direction == 'left' and i==-WIDTH:
#         window.blit(bg_img,(WIDTH-i,0))
#         i=0

#     if direction == 'right' and i==WIDTH:
#         window.blit(bg_img,(-WIDTH+i,0))
#         i=0

#     if direction == 'left':
#         i+=1
#     if direction == 'right':
#         i-=1

#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             runing = False
#         if event.type == pygame.KEYUP:
#             if event.key == pygame.K_LEFT:
#                 direction = 'left'
#             if event.key == pygame.K_RIGHT:
#                 direction = 'right'
#     pygame.display.update()
# pygame.quit() 