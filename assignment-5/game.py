from enum import IntEnum
from os import listdir
from os.path import isfile, join

import pygame

FPS = 60

pygame.init()

WIDTH = 600
HEIGHT = 450

window = pygame.display.set_mode((WIDTH,HEIGHT))
BACKGROUND = pygame.image.load('background.jpg')
BACKGROUND = pygame.transform.scale(BACKGROUND,(WIDTH,HEIGHT))

class Direction(IntEnum):
    LEFT = -1
    RIGHT = 1


def flip(sprites):
    return [pygame.transform.flip(sprite, True, False) for sprite in sprites]


def load_sprite_sheets(width, height, direction=False):
    path = join(".")
    images = [
        f for f in listdir(path) if isfile(join(path, f)) and f.endswith(".png")
    ]

    all_sprites = {}

    for image in images:
        sprite_sheet = pygame.image.load(join(path, image)).convert_alpha()

        sprites = []
        for i in range(sprite_sheet.get_width() // width):
            surface = pygame.Surface((width, height), pygame.SRCALPHA, 32)
            rect = pygame.Rect(i * width, 0, width, height)
            surface.blit(sprite_sheet, (0, 0), rect)
            sprites.append(pygame.transform.scale2x(surface))

        if direction:
            all_sprites[image.replace(".png", "") + "_right"] = sprites
            all_sprites[image.replace(".png", "") + "_left"] = flip(sprites)
        else:
            all_sprites[image.replace(".png", "")] = sprites

    return all_sprites


class Player(pygame.sprite.Sprite):
    COLOR = (255, 0, 0)
    SPRITES = load_sprite_sheets(32, 32, True)

    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.direction = "right"

    def move(self, dir: Direction):
        if dir == Direction.LEFT:
            self.direction = 'right'
        if dir == Direction.RIGHT:
            self.direction = 'left'

    def draw(self, win):
        self.sprite = self.SPRITES["idle_" + self.direction][0]
        win.blit(self.sprite, (self.rect.x, self.rect.y))


clock = pygame.time.Clock()
 
i = 0

runing = True

direction = Direction.LEFT

player = Player(WIDTH/2 - 10, HEIGHT-138, 100, 100)

while runing:
    clock.tick(FPS)

    window.fill((0,0,0))
    window.blit(BACKGROUND,(i,0))
    
    window.blit(BACKGROUND,(-WIDTH+i,0))
    window.blit(BACKGROUND,(WIDTH+i,0))

    if (i==(WIDTH * direction)):
        window.blit(BACKGROUND,((WIDTH * direction) + i,0))
        i=0
    i+= (1 * direction)


    player.move(direction)

    player.draw(window)

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
