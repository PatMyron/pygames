from datetime import datetime
from twisted.internet.task import LoopingCall
from twisted.internet import reactor
import pygame
from Enemy import Enemy
from Player import Player
from Background import Background

class GameSpace:
        def __init__(self):
		pass
        def main(self):
                pygame.init()
                self.size = self.width, self.height = 1366, 444
                self.black = 0, 0, 0
                self.screen = pygame.display.set_mode(self.size)

		self.player = Player(self)
		self.enemy = Enemy(self)		
		self.bg = Background(self)
		
		go = LoopingCall(self.ticker)
		go.start(0.01)
		reactor.run()

	def ticker(self):
		pygame.event.get()
		self.player.tick()
		self.enemy.tick()
		self.bg.tick()		

		self.screen.fill(self.black)
		self.screen.blit(self.bg.image, self.bg.rect)
		self.screen.blit(self.player.image, self.player.rect)
		self.screen.blit(self.enemy.image, self.enemy.rect)
		pygame.display.flip()


if __name__ == '__main__':
        gs = GameSpace()
        gs.main()
