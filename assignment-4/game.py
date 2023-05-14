import pygame
import pygame.image
import requests
import io
import math
import random

pygame.init()

WIDTH = 960
HEIGHT = 840

WHITE = "white"
BLACK = "black"

FPS = 60

window = pygame.display.set_mode((WIDTH, HEIGHT))

def load_image(url):
    response = requests.get(url)
    image = pygame.image.load(io.BytesIO(response.content))
    return pygame.transform.scale(image, (WIDTH, HEIGHT))

image = load_image("https://i.imgur.com/H37kxPH.jpeg")

def calculate_brightness(image):
    brightness_map = []
    for y in range(HEIGHT):
        row = []
        for x in range(WIDTH):
            red, green, blue, _ = image.get_at((x, y))
            brightness = math.sqrt(0.299 * (red ** 2) +
                                0.587 * (green ** 2) +
                                0.114 * (blue ** 2)) / 100
            cell = [brightness]
            row.append(cell)
        brightness_map.append(row)
    return brightness_map

brightness_map = calculate_brightness(image)

class Droplet:
    def __init__(self):
        self.x = int(random.uniform(0, 1) * WIDTH)
        self.y = 0
        self.speed = random.uniform(0, 1) * 3.5
        self.size = 1 + random.uniform(0, 1) * 1

    def animation_step(self):
        self.vel = brightness_map[int(self.y)][int(self.x)][0]
        self.y += (2.6 - self.vel) + self.speed
        if self.y >= HEIGHT:
            self.y = 0
            self.x = int(random.uniform(0, 1) * WIDTH)

    def draw(self, window):
        pygame.draw.circle(window, WHITE, (int(self.x), int(self.y)), int(self.size))

droplets = [Droplet() for _ in range(5000)]

clock = pygame.time.Clock()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    window.fill(BLACK)
    window.blit(image, (0, 0))

    for droplet in droplets:
        droplet.animation_step()
        droplet.draw(window)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
