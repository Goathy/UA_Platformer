import pygame
import os
import os.path

BG_COLOR = (255, 255, 255)

WIDTH = 1000
HEIGHT = 800

FPS = 30

PLAYER_VEL = 30

pygame.init()

pygame.display.set_caption("platformer")

window = pygame.display.set_mode((WIDTH, HEIGHT))

def get_background(name):
    image = pygame.image.load(os.path.join(name))
    _, _, width, height = image.get_rect()

    tiles = []

    for i in range(WIDTH // width + 1):
        for j in range(HEIGHT // height + 1):
            pos = [i * width, j * height]
            tiles.append(pos)

    return tiles, image


def draw(window, background, bg_image):
    for tile in background:
        window.blit(bg_image, tile)

    pygame.display.update()


def main(window):
    clock = pygame.time.Clock()
    background, bg_image = get_background("Blue.png")

    run = True
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    run = False
                    break

        draw(window, background, bg_image)

    pygame.quit()
    quit()


if __name__ == "__main__":
    main(window)
