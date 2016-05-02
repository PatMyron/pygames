import pygame
class Background(pygame.sprite.Sprite):
        def __init__(self, gs=None):
                pygame.sprite.Sprite.__init__(self)
                self.gs = gs
                self.image = pygame.image.load("media/level1zoomed.png")
                self.rect = self.image.get_rect()
                self.rect.x = 0
                self.rect.y = 0

                # keep original image to limit resize errors
                self.orig_image = self.image
        def tick(self):
                pass



# 396-397 px down to ground
