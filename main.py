from turtle import speed
import random
import pygame  # Импорт модуля пайгейм

pygame.init()

ping = pygame.mixer.Sound("ball.mp3")
loose = pygame.mixer.Sound("loose.mp3")
pygame.mixer.music.load("fon.mp3")
pygame.mixer.music.set_volume(0.1)
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
game_rounds = 3

ball1 = pygame.image.load('img.png')
ball1 = pygame.transform.scale(ball1, (50, 50))
ball1_rect = ball1.get_rect()

platform = pygame.image.load('platform.png')
platform_rect = platform.get_rect()

platform_rect.x = width / 2 - platform.get_width() / 2
platform_rect.y = height - 60

speedX = 10
speedY = 10

clock = pygame.time.Clock()
run = True
while run:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    key = pygame.key.get_pressed()

    screen.fill(CYAN)
    screen.blit(ball1, ball1_rect)
    screen.blit(platform, platform_rect)


    draw_text(screen,'score: ' + str(score), 50, width // 2, 40, BLACK)
    draw_text(screen, 'rounds: ' + str(game_rounds), 50, 1250, 40, BLACK)

    ball1_rect.x += speedX
    ball1_rect.y += speedY



    if key[pygame.K_LEFT] and platform_rect.left > 0:
        platform_rect.x -= 10
    if key[pygame.K_RIGHT] and platform_rect.right < width:
        platform_rect.x += 10

    if ball1_rect.colliderect(platform_rect):
        ping.play()
        score = score + 1
        speedY = -speedY

    if ball1_rect.top < 0:
        speedY = -speedY
    if ball1_rect.left < 0:
        speedX = -speedX
    if ball1_rect.right > width:
        speedX = -speedX
    if ball1_rect.bottom > height:
        # run = False
        ball1_rect.x = random.randint(100, width - 100)
        ball1_rect.y = 100
        game_rounds = game_rounds - 1
        loose.play()
    if game_rounds < 1:
        run = False
    pygame.display.update()
pygame.quit()
