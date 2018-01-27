import tensorflow as tf

from ..neat import *
from ..neat.commands import *

class ConnectionTest(tf.test.TestCase):
    def setUp(self):
        class TestConfig(Config):
            def __init__(self):
                super().__init__(1, 2)
                self.randValue = 0
                self.gaussValue = 7

            def rand(self):
                return self.randValue

            def gauss(self, mi, si):
                return self.gaussValue

        self.conf = TestConfig()
        self.factory = InnovationFactory(self.conf)
        self.node_in = self.factory.createNode('input')
        self.node_hidden = self.factory.createNode('hidden')
        self.node_out = self.factory.createNode('output')

    def testConnectionShouldHaveDestinationAndSource(self):
        con = self.factory.createConnection(self.node_in, self.node_out)
        self.assertTrue(type(con.source) is int)
        self.assertTrue(type(con.destination) is int)


    def testConnectionCantHaveInputAsDestination(self):
        try:
            self.factory.createConnection(self.node_hidden, self.node_in)
            self.fail()
        except(NEATDQNException):
            pass

    def testConnectionCantHaveOutputAsSource(self):
        try:
            self.factory.createConnection(self.node_out, self.node_hidden)
            self.fail()
        except(NEATDQNException):
            pass

    def testConnectionShouldHaveWeight(self):
        con = self.factory.createConnection(self.node_in, self.node_out)
        self.assertEqual(float, type(con.weight))

    def testConfigRandomForReplaceLearningRate(self):
        con = self.factory.createConnection(self.node_in, self.node_out)
        con.exec(Mutate())
        self.assertEqual(7, con.learning_rate)

    def testConfigRandomForModifyLearningRate(self):
        con = self.factory.createConnection(self.node_in, self.node_out)
        con.learning_rate = 2
        self.conf.randValue = 0.1
        self.conf.connectionReplaceRate = 0
        con.exec(Mutate())
        self.assertEqual(9, con.learning_rate)
