import pygame
from Enemy import Enemy
from Player import Player
class GameSpace:
        def __init__(self):
		pass
        def main(self):
                pygame.init()
                self.size = self.width, self.height = 1366, 768
                self.black = 0, 0, 0
                self.screen = pygame.display.set_mode(self.size)

		self.clock = pygame.time.Clock()
		self.player = Player(self)
		self.enemy = Enemy(self)		

		while 1:
			self.clock.tick(60)
			self.event = pygame.event.wait()

			self.player.tick()
			self.enemy.tick()

			self.screen.fill(self.black)
			self.screen.blit(self.player.image, self.player.rect)
			self.screen.blit(self.enemy.image, self.enemy.rect)
			pygame.display.flip()


if __name__ == '__main__':
        gs = GameSpace()
        gs.main()
