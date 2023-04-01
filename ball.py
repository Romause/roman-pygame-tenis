import pygame
import random
import pygame

class Ball:
    def __init__(self):
        self.image = pygame.image.load("img.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.speed = [random.randint(5, 10), random.randint(5, 10)]


    def update(self, width, screen):
        if self.rect.top < 0:
            self.speed[1] = -self.speed[1]
        if self.rect.left < 0:
            self.speed[0] = -self.speed[0]
        if self.rect.right > width:
            self.speed[0] = -self.speed[0]
        screen.blit(self.image, self.rect)
        self.move()

    def move(self):
        self.rect.x += self.speed[0]
        self.rect.y += self.speed[1]

    def respawn(self, width):
        self.rect.x = 50
        self.rect.x = random.randint(50, width-50)