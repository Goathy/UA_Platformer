import pygame

BACKGROUND="black"

WIDTH = 1000
HEIGHT = 800

FPS = 60

PLAYER_VEL = 15
PLAYER_STOP = 0

pygame.init()

pygame.display.set_caption('Platformer_game')

window = pygame.display.set_mode((WIDTH, HEIGHT))

class Rectangle(pygame.sprite.Sprite):
    COLOR = "red"

    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.x_vel = 0
        self.y_vel = 0

    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

    def move_x(self, vel):
        self.x_vel = vel

    def move_y(self, vel):
        self.y_vel = vel
    
    def loop(self):
        self.move(self.x_vel, self.y_vel)

    def draw(self, win):    
        pygame.draw.rect(win, self.COLOR, self.rect)

def handle_move(player, key):
    if key == pygame.K_LEFT:
        if player.x_vel > 0:
            player.move_x(PLAYER_STOP)
            player.move_y(PLAYER_STOP)
        else:
            player.move_x(-PLAYER_VEL)
            player.move_y(PLAYER_STOP)

    if key == pygame.K_RIGHT:
        if player.x_vel < 0:
            player.move_x(PLAYER_STOP)
            player.move_y(PLAYER_STOP)
        else:
            player.move_x(PLAYER_VEL)
            player.move_y(PLAYER_STOP)

    if key == pygame.K_UP:
        if player.y_vel > 0:
            player.move_y(PLAYER_STOP)
            player.move_x(PLAYER_STOP)
        else:
            player.move_y(-PLAYER_VEL)
            player.move_x(PLAYER_STOP)

    if key == pygame.K_DOWN:
        if player.y_vel < 0:
            player.move_y(PLAYER_STOP)
            player.move_x(PLAYER_STOP)
        else:
            player.move_y(PLAYER_VEL)
            player.move_x(PLAYER_STOP)

def draw(window, player):
    window.fill(BACKGROUND)

    player.draw(window)

    pygame.display.update()

def main(window):
    clock = pygame.time.Clock()

    player = Rectangle(100, 100, 50, 50)

    run = True 
    while run:
        clock.tick(FPS)

        player.loop()
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    run = False
                    break
                case pygame.KEYUP:
                    handle_move(player, event.key)

        draw(window, player)

    pygame.quit()
    quit()

if __name__ == "__main__":
    main(window)
