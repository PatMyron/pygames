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
		self.rect.y = 365
		self.rect.x = 450
		self.x = 0
		self.jumping = False
		self.falling = False		

		# keep original image to limit resize errors
		self.orig_image = self.image

	def tick(self):
		self.sprite = (self.sprite + 1) % 3  # incrementing sprite
                self.image = pygame.image.load("media/mario/mario-" + str(self.sprite + 1) +  ".png")

		keys = pygame.key.get_pressed()
		if keys[K_RIGHT]:
			self.x += 5
		if keys[K_LEFT]:
			self.x -= 5
		if keys[K_UP] and not self.jumping and not self.falling:
			self.jumping = True

		if self.jumping:
			self.rect.y -= 5
			if self.rect.y < 210:
				self.jumping = False
				self.falling = True
				
		if self.falling:
			self.rect.y += 5
			if self.rect.y == 365:
				self.falling = False
