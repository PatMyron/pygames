import pygame
class Enemy(pygame.sprite.Sprite):
        def __init__(self, gs=None):
                pygame.sprite.Sprite.__init__(self)
                self.gs = gs
                self.image = pygame.image.load("media/globe.png")
                self.rect = self.image.get_rect()
		self.rect.x = 450
		self.rect.y = 330

                # keep original image to limit resize errors
                self.orig_image = self.image
        def tick(self):
		pass
