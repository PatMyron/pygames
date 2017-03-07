import pygame


class Background(pygame.sprite.Sprite):
    def __init__(self, gs, player):
        pygame.sprite.Sprite.__init__(self)
        self.gs = gs
        self.player = player
        self.image = pygame.image.load("media/level1zoomed.png")
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0

    def tick(self):
        self.rect.x = 450 - self.player.x
