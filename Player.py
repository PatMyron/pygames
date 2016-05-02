from pygame import mixer
from pygame.locals import *
import pygame
import math
def rot_center(image, rect, angle):
        rot_image = pygame.transform.rotate(image, angle)
        rot_rect = rot_image.get_rect(center=rect.center)
        return rot_image,rot_rect
class Player(pygame.sprite.Sprite):
	def __init__(self, gs=None):
		pygame.sprite.Sprite.__init__(self)
		self.gs = gs
		self.sprite = 0
                self.image = pygame.image.load("media/mario/mario-" + str(self.sprite + 1) +  ".png")
		self.rect = self.image.get_rect()
		self.rect.y = 364

		# keep original image to limit resize errors
		self.orig_image = self.image

	def tick(self):
		self.sprite = (self.sprite + 1) % 3  # incrementing sprite
                self.image = pygame.image.load("media/mario/mario-" + str(self.sprite + 1) +  ".png")

		keys = pygame.key.get_pressed()
		if keys[K_RIGHT]:
		    self.rect.x += 5
		if keys[K_LEFT]:
		    self.rect.x -= 5
		if keys[K_UP]:
		    self.rect.y -=5
		if keys[K_DOWN]:
		    self.rect.y += 5
