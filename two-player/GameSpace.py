import json

import pygame

from Background import Background
from Enemy import Enemy
from Player import Player


class GameSpace:
    # Pass connection and character
    def __init__(self, connection, character):
        self.connection = connection
        self.character = character

        # initialize the game space
        pygame.init()
        self.size = self.width, self.height = 900, 444
        self.screen = pygame.display.set_mode(self.size)

        self.player = Player(self, self.character)
        self.enemy = Enemy(self, self.character)
        self.bg = Background(self, self.player)

        self.clock = pygame.time.Clock()

        self.received = [450, 365, 450, 365]
        self.p1 = [450, 365]
        self.p2 = [450, 365]

    # Store data
    def receive(self, data):
        self.received = json.loads(data)

    def ticker(self):

        # get events
        pygame.event.get()

        # Check for winner and blit win message
        if len(self.received) == 0:
            if self.character == "mario":
                self.screen.blit(pygame.image.load('media/lugado.png'), self.player.rect)
                pygame.display.flip()
                return
            else:
                self.screen.blit(pygame.image.load('media/mariano.png'), self.player.rect)
                pygame.display.flip()
                return

        # check for moves
        self.p1 = self.player.tick()
        self.p2 = self.enemy.tick(self.received, self.p1)
        self.bg.tick()

        # blit screen and wait
        self.screen.fill((0, 0, 0))  # black
        self.screen.blit(self.bg.image, self.bg.rect)
        self.screen.blit(self.player.image, self.player.rect)
        self.screen.blit(self.enemy.image, self.enemy.rect)
        pygame.display.flip()
        self.clock.tick(200)

        # message
        self.var = [self.p1[0], self.p1[1]]

        # Check for win condition
        if self.p1[0] >= 6328:
            if self.character == "mario":
                print "here"
                self.screen.blit(pygame.image.load('media/mariano.png'), self.player.rect)
                pygame.display.flip()
                self.connection.transport.write(json.dumps([]))
            else:
                print "here"
                self.screen.blit(pygame.image.load('media/lugado.png'), self.player.rect)
                pygame.display.flip()
                self.connection.transport.write(json.dumps([]))

        # If no winner, send data and tick again
        else:
            self.connection.transport.write(json.dumps(self.var))
