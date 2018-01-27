import tensorflow as tf

from ...neat import *
from ...neat.commands import *

class MutationTestConfig(Config):
    def __init__(self, inp, out):
        super().__init__(inp, out)

        self.shouldAddConnection = False
        self.shouldAddNode = False
        self.shouldChangeConnection = False
        self.shouldRemoveConnection = False
        self.shouldRemoveNode = False
        self.shouldReplaceConnection = False
        self.mutationRate = 1
        self.mutationRates = TestMutationRates(self)


class TestMutationRates(MutationRates):
    def shouldAddConnection(self):
        return self.conf.shouldAddConnection

    def shouldAddNode(self):
        return self.conf.shouldAddNode

    def shouldChangeConnection(self):
        return self.conf.shouldChangeConnection

    def shouldRemoveConnection(self):
        return self.conf.shouldRemoveConnection

    def shouldRemoveNode(self):
        return self.conf.shouldRemoveNode

    def shouldReplaceConnection(self):
        return self.conf.shouldReplaceConnection

    def getMutationRate(self):
        return self.conf.mutationRate

class MutationGenomeFactory(GenomeFactory):
    def __init__(self, conf = MutationTestConfig(1, 1)):
        super().__init__(conf)

    def createInitial(self):
        gen = MutationGenome(self.conf)
        self.initConfig(gen)
        gen.addGene(self.ifac.createNode('hidden'))
        return gen


class MutationGenome(Genome):
    def exec(self, op):
        self.lastType = type(op)


class FakeNode(Node):
    def __init__(self, conf):
        super().__init__(conf, 123, 'hidden')
        self.last = None
        self.learning_rate = 1

    def exec(self, op):
        self.last = type(op)


class FakeConnection(Connection):
    def __init__(self, conf, learning_rate=1):
        super().__init__(conf, 5, 4, 3)
        self.learning_rate = learning_rate

