import pygame
from pygame.locals import *

from bounds import check


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("media/small.png")
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(self.image, (int(self.rect.w/2), int(self.rect.h/2)))
        self.rect = self.image.get_rect()
        self.jumping = False
        self.falling = False

    def tick(self):
        keys = pygame.key.get_pressed()
        if keys[K_RIGHT] and check(self.rect.x + 5, self.rect.y):
            self.rect.x += 5
        if keys[K_LEFT] and check(self.rect.x - 5, self.rect.y):
            self.rect.x -= 5
        if keys[K_UP] and not self.jumping and not self.falling:
            self.jumping = True
            self.jumpsLeft = 25

        if self.jumping:
            if self.jumpsLeft == 0 or not check(self.rect.x, self.rect.y - 5):
                self.jumping = False
                self.falling = True
            else:
                self.rect.y -= 5
                self.jumpsLeft -= 1

        if not self.jumping and check(self.rect.x, self.rect.y + 5):  # gravity
            self.rect.y += 5
            self.falling = True

        if not self.jumping and not check(self.rect.x, self.rect.y + 5):
            self.falling = False
