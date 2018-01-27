
from .exceptions import NEATDQNException
from .gene_connection import Connection
from .gene_node import Node

class InnovationFactory:
    def __init__(self, conf):
        self.conf = conf
        self.nextInnovation = 0
        self.connections = {}

    def createNode(self, type):
        node = Node(self.conf, self.nextInnovation, type)
        self.nextInnovation += 1
        return node


    def createConnection(self, source, destination):
        if destination.type == 'input' or source.type == 'output':
            raise NEATDQNException('Invalid source/destination in connection')

        id = "{0}:{1}".format(source.innovationNumber, destination.innovationNumber)
        if id in self.connections:
            connection = self.connections[id]
        else:
            connection = Connection(self.conf, self.nextInnovation, source.innovationNumber, destination.innovationNumber)
            self.connections[id] = connection
        self.nextInnovation += 1
        return connection

    def createGeneByCrossing(self, g1, g2):
        if self.conf.rand() < 0.5:
            out = g1.clone()
        else:
            out = g2.clone()
        return out