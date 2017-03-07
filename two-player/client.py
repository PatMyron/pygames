import os
from twisted.internet.protocol import Factory
from twisted.internet.protocol import Protocol
from twisted.protocols.basic import LineReceiver
from twisted.internet.tcp import Port
from twisted.internet import reactor
from twisted.internet.protocol import ClientFactory
from GameSpace import GameSpace
from twisted.internet.task import LoopingCall
import json

SERVER_HOST = "127.0.0.1"
SERVER_PORT = 40086

# Connection factory
class ServerConnFactory(ClientFactory):
    def buildProtocol(self):
        return ServerConnection()

# Create Connection to server
class ServerConnection(Protocol):
    def dataReceived(self, data):
        
        # store data and tick
        self.gs.receive(data)
        self.gs.ticker()

    def connectionMade(self):
        # instantiate gamespace
        self.gs = GameSpace(self, "luigi")
        self.gs.main()
        #self.go = LoopingCall(self.gs.ticker)
        #self.go.start(0.01)

        print 'made connection to '+SERVER_HOST+' port '+str(SERVER_PORT)
        self.transport.write(json.dumps([450, 365, 450, 365]))


    def connectionlost(self):
        print "lost connection"
        reactor.stop()

if __name__ == '__main__':
    reactor.connectTCP(SERVER_HOST, SERVER_PORT, ServerConnFactory())
    reactor.run()
