import pygame
from pygame.locals import *

from bounds import check


class Player(pygame.sprite.Sprite):
    def __init__(self, gs=None):
        pygame.sprite.Sprite.__init__(self)
        self.gs = gs
        self.sprite = 0
        self.image = pygame.image.load("media/mario/mario-" + str(self.sprite + 1) + ".png")
        self.rect = self.image.get_rect()
        self.rect.y = 365
        self.rect.x = 450
        self.x = 450
        self.jumping = False
        self.falling = False

    def tick(self):
        self.sprite = (self.sprite + 1) % 3  # incrementing sprite
        self.image = pygame.image.load("media/mario/mario-" + str(self.sprite + 1) + ".png")

        keys = pygame.key.get_pressed()
        if keys[K_RIGHT] and check(self.x + 5, self.rect.y):
            self.x += 5
        if keys[K_LEFT] and check(self.x - 5, self.rect.y):
            self.x -= 5
        if keys[K_UP] and not self.jumping and not self.falling:
            self.jumping = True
            self.jumpsLeft = 31

        if self.jumping:
            if self.jumpsLeft == 0 or not check(self.x, self.rect.y - 5):
                self.jumping = False
                self.falling = True
            else:
                self.rect.y -= 5
                self.jumpsLeft -= 1

        if not self.jumping and check(self.x, self.rect.y + 5):  # gravity
            self.rect.y += 5
            self.falling = True

        if not self.jumping and not check(self.x, self.rect.y + 5):
            self.falling = False
