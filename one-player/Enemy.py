import pygame


class Enemy(pygame.sprite.Sprite):
        def __init__(self, gs=None):
                pygame.sprite.Sprite.__init__(self)
                self.gs = gs
                self.sprite = 0
                self.image = pygame.image.load("media/luigi/luigi-" + str(self.sprite + 1) + ".png")
                self.rect = self.image.get_rect()
                self.rect.x = 450
                self.rect.y = 364

                # keep original image to limit resize errors
                self.orig_image = self.image

        def tick(self):
                self.sprite = (self.sprite + 1) % 3  # incrementing sprite
                self.image = pygame.image.load("media/luigi/luigi-" + str(self.sprite + 1) + ".png")
