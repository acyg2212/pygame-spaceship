import pygame
import os

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Fighters")
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FPS = 60
vel = 5
SPACESHIP_HEIGHT = 40
SPACESHIP_WIDTH = 55
BORDER = pygame.Rect(WIDTH/2-5, 0, 10, HEIGHT)

YELLOW_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('Assets', 'spaceship_yellow.png'))
YELLOW_SPACESHIP = pygame.transform.rotate(
    pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (55, 40)), 90)

RED_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('Assets', 'spaceship_red.png'))
RED_SPACESHIP = pygame.transform.rotate(
    pygame.transform.scale(RED_SPACESHIP_IMAGE, (55, 40)), 270)


def draw_window(red, yellow):

    WIN.fill(WHITE)
    pygame.draw.rect(WIN, BLACK, BORDER)
    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    WIN.blit(RED_SPACESHIP, (red.x, red.y))
    pygame.display.update()


def yellow_handle_movement(keys_pressed, yellow):
    if keys_pressed[pygame.K_a] and yellow.x - vel > 0:  # left
        yellow.x -= vel
    if keys_pressed[pygame.K_d] and yellow.x + vel + yellow.width < BORDER.x:  # right
        yellow.x += vel
    if keys_pressed[pygame.K_w] and yellow.y - vel > 0:  # up
        yellow.y -= vel
    if keys_pressed[pygame.K_s] and yellow.y + vel + yellow.width < HEIGHT:  # down
        yellow.y += vel


def red_handle_movement(keys_pressed, red):
    if keys_pressed[pygame.K_LEFT]:  # left
        red.x -= vel
    if keys_pressed[pygame.K_RIGHT]:  # right
        red.x += vel
    if keys_pressed[pygame.K_UP]:  # up
        red.y -= vel
    if keys_pressed[pygame.K_DOWN]:  # down
        red.y += vel


def main():
    red = pygame.Rect(700, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys_pressed = pygame.key.get_pressed()
        yellow_handle_movement(keys_pressed, yellow)
        red_handle_movement(keys_pressed, red)
        draw_window(red, yellow)
    pygame.quit()


if __name__ == "__main__":
    main()
