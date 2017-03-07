import json

from twisted.internet import reactor
from twisted.internet.protocol import ClientFactory
from twisted.internet.protocol import Protocol

from GameSpace import GameSpace

SERVER_HOST = "127.0.0.1"
SERVER_PORT = 40086

# Connection factory
class ServerConnFactory(ClientFactory):
    def buildProtocol(self, addr):
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


    def connectionlost(self, reason):
        print "lost connection"
        reactor.stop()

if __name__ == '__main__':
    reactor.connectTCP(SERVER_HOST, SERVER_PORT, ServerConnFactory())
    reactor.run()
