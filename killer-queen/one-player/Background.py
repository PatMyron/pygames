import pygame


class Background(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("media/night-edit.jpg")
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(self.image, (int(self.rect.w/2.475925925925926), int(self.rect.h/2.475925925925926)))
        self.rect = self.image.get_rect()
