import pygame
from twisted.internet import reactor
from twisted.internet.task import LoopingCall

from Background import Background
from Player import Player


class GameSpace:
    def __init__(self):
        pygame.init()
        self.size = self.width, self.height = 1920//2, 1080//2
        self.screen = pygame.display.set_mode(self.size)

        self.player = Player()
        self.bg = Background()

        go = LoopingCall(self.ticker)
        go.start(0.01)
        reactor.run()

    def ticker(self):
        pygame.event.get()
        self.player.tick()

        self.screen.fill((0, 0, 0))  # black
        self.screen.blit(self.bg.image, self.bg.rect)
        self.screen.blit(self.player.image, self.player.rect)
        pygame.display.flip()


if __name__ == '__main__':
    gs = GameSpace()
