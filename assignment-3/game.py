import pygame

BG_SOLID_WHITE=(255, 255, 255)
BG_SOLID_BLACK=(0, 0, 0)

WIDTH = 1000
HEIGHT = 800

FPS = 60

PLAYER_VEL = 15

pygame.init()

pygame.display.set_caption('Platformer_game')

window = pygame.display.set_mode((WIDTH, HEIGHT))

class Rectangle(pygame.sprite.Sprite):
    COLOR = (255, 0, 0)

    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.x_vel = 0
        self.y_vel = 0

    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

    def move_left(self, vel):
        self.x_vel = -vel

    def move_right(self, vel):
        self.x_vel = vel

    def move_up(self, vel):
        self.y_vel = -vel

    def move_down(self, vel):
        self.y_vel = vel
    
    def loop(self):
        self.move(self.x_vel, self.y_vel)

    def reset_x(self):
        self.x_vel = 0

    def reset_y(self):
        self.y_vel = 0

    def draw(self, win):    
        pygame.draw.rect(win, self.COLOR, self.rect)

def handle_move(player, key):
    if key == pygame.K_LEFT:
        if player.x_vel > 0:
            player.reset_x()
            player.reset_y()
        else:
            player.move_left(PLAYER_VEL)
            player.reset_y()

    if key == pygame.K_RIGHT:
        if player.x_vel < 0:
            player.reset_y()
            player.reset_x()
        else:
            player.move_right(PLAYER_VEL)
            player.reset_y()

    if key == pygame.K_UP:
        if player.y_vel > 0:
            player.reset_y()
            player.reset_x()
        else:
            player.move_up(PLAYER_VEL)
            player.reset_x()

    if key == pygame.K_DOWN:
        if player.y_vel < 0:
            player.reset_y()
            player.reset_x()
        else:
            player.move_down(PLAYER_VEL)
            player.reset_x()

def draw(window, player):
    window.fill(BG_SOLID_BLACK)

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