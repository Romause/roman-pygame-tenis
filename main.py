from turtle import speed
import random
import pygame  # Импорт модуля пайгейм
import ball
import platform

pygame.init()

ping = pygame.mixer.Sound("ball.mp3")
loose = pygame.mixer.Sound("loose.mp3")
pygame.mixer.music.load("fon.mp3")
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(-1)

pygame.mixer.music.load("fon.mp3")
pygame.mixer.music.play(-1)

width = 1366
height = 768
fps = 60
gameName = 'First Project'

screen = pygame.display.set_mode((width, height))  # Создание экрана с заданными размера

def draw_text(screen, text, size, x, y, color):
    font_name =pygame.font.match_font('arial')
    font = pygame.font.Font(font_name, size)
    text_image = font.render(text, True, color)
    text_rect = text_image.get_rect()
    text_rect.center = (x, y)
    screen.blit(text_image, text_rect)



BLACK = '#000000'
WHITE = '#FFFFFF'
RED = '#FF0000'
GREEN = '#008000'
BLUE = '#0000FF'
CYAN = '#00FFFF'
score = 0
round = 3

ball1 = ball.Ball()
ball2 = ball.Ball()
ball3 = ball.Ball()


balls = [ball1, ball2, ball3]




platform = pygame.image.load('platform.png')
platform_rect = platform.get_rect()

platform_rect.x = width / 2 - platform.get_width() / 2
platform_rect.y = height - 60


clock = pygame.time.Clock()
run = True
while run:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    key = pygame.key.get_pressed()

    screen.fill(CYAN)
    for ball in balls:
        ball.update(width, screen)
        if platform_rect.colliderect(ball.rect):
            score += 1
            ball.speed[1] = -ball.speed[1]
        if ball.rect.bottom > height:
            round = round - 1
            if round == 0:
                run = False
            ball.respawn(width)

    screen.blit(platform, platform_rect)


    draw_text(screen,'score: ' + str(score), 50, width // 2, 40, BLACK)
    draw_text(screen, 'rounds: ' + str(round), 50, 1250, 40, BLACK)

    if key[pygame.K_LEFT] and platform_rect.left > 0:
        platform_rect.x -= 30
    if key[pygame.K_RIGHT] and platform_rect.right < width:
        platform_rect.x += 30


    pygame.display.update()
pygame.quit()
