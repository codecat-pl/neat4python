from .gene_connection import Connection
from .gene_node import Node


class Genome:
    def __init__(self, conf):
        self.conf = conf
        self.genes = []
        self.input = []
        self.nodes = []
        self.hidden = []
        self.output = []
        self.connections = []
        self.dict = {}

    @property
    def inputsCount(self):
        return len(self.input)

    @property
    def outputsCount(self):
        return len(self.output)

    def addGene(self, gene):
        if gene is None:
            return

        self.__addGene(gene)
        if type(gene) is Node:
            self.__addNode(gene)
        if type(gene) is Connection:
            self.__addConnection(gene)

    def rmGene(self, gene):
        if gene is None:
            return None

        if type(gene) is Node:
            self.__rmNode(gene)
        if type(gene) is Connection:
            self.__rmConnection(gene)
        self.__rmGene(gene)

    def findInnov(self, id):
        if id in self.dict:
            return self.dict[id]
        else:
            return None

    def getRandomNode(self):
        return self.nodes[self.conf.randint(0, len(self.nodes)-1)]

    def getRandomHiddenNode(self):
        if len(self.hidden) == 0:
            return None
        return self.hidden[self.conf.randint(0, len(self.hidden)-1)]

    def getRandomConnection(self):
        if len(self.connections) == 0:
            return None
        return self.connections[self.conf.randint(0, len(self.connections)-1)]

    def getConnectionsByNode(self, innov):
        return [c for c in self.connections if c.source == innov or c.destination == innov]

    def exec(self, op):
        return op.onGenome(self)

    def __rmGene(self, gene):
        del self.dict[gene.innovationNumber]
        self.genes.remove(gene)

    def __rmConnection(self, gene):
        self.connections.remove(gene)

    def __rmNode(self, gene):
        self.nodes.remove(gene)
        met = getattr(self, gene.type)
        met.remove(gene)

    def __addGene(self, gene):
        self.dict[gene.innovationNumber] = gene
        self.genes.append(gene)

    def __addNode(self, gene):
        self.nodes.append(gene)
        met = getattr(self, gene.type)
        met.append(gene)

    def __addConnection(self, gene):
        self.connections.append(gene)

