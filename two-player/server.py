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

# Create connection to client
class MyConnection(LineReceiver):
    def __init__(self):
        pass

    def dataReceived(self, data):
        # Store data and tick
        self.gs.receive(data)
        self.gs.ticker()


    def connectionMade(self):
        # Instantiate gamespace
        self.gs = GameSpace(self, "mario")
        self.gs.main()
        #self.go = LoopingCall(self.gs.ticker)
        #self.go.start(0.01)    
        print 'made connection to '+SERVER_HOST+' port '+str(SERVER_PORT)

    def connectionLost(self):
        print "lost connection"
        reactor.stop()

# Connection Factory
class MyConnectionFactory(Factory):
    def buildProtocol(self):
        return MyConnection()

if __name__ == '__main__':
    reactor.listenTCP(SERVER_PORT, MyConnectionFactory())
    reactor.run()
