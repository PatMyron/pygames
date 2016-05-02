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
		self.image = pygame.image.load("media/deathstar.png")
		self.rect = self.image.get_rect()

		# keep original image to limit resize errors
		self.orig_image = self.image

	def tick(self):
		# get the mouse x and y position on the screen
		mx, my = pygame.mouse.get_pos()

		but1, but2, but3 = pygame.mouse.get_pressed()
