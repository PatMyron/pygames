import pygame
from twisted.internet import reactor
from twisted.internet.task import LoopingCall

from Background import Background
from Enemy import Enemy
from Player import Player


class GameSpace:
    def __init__(self):
        pass

    def main(self):
        pygame.init()
        self.size = self.width, self.height = 900, 444
        self.black = 0, 0, 0
        self.screen = pygame.display.set_mode(self.size)

        self.player = Player(self)
        self.enemy = Enemy(self)
        self.bg = Background(self, self.player)

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
        # self.screen.blit(self.enemy.image, self.enemy.rect)
        pygame.display.flip()


if __name__ == '__main__':
    gs = GameSpace()
    gs.main()
