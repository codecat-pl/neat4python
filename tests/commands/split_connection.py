import tensorflow as tf

from ...neat import *
from ...neat.commands import *

class SplitConnectionOpTest(tf.test.TestCase):
    def testSplitedConnectionShouldBeDisabled(self):
        genome = GenomeFactory(Config(1, 1)).createInitial()
        op = SplitConnection(genome.connections[0].innovationNumber)
        genome.exec(op)
        self.assertTrue(genome.connections[0].disabled)

    def testInPlaceOfConnectionShouldCreateNewNodeAndConnections(self):
        genome = GenomeFactory(Config(1, 1)).createInitial()
        con = genome.connections[0]
        genome.exec(SplitConnection(con.innovationNumber))
        self.assertEqual(3, len(genome.nodes))
        self.assertEqual(3, len(genome.connections))

    def testSplitedConnectionShouldBeSameAsEndOne(self):
        gen = self.setUpSimpleGenome()
        con2 = gen.connections[2]
        self.assertEqual(con2.destination, gen.output[0].innovationNumber)
        self.assertEqual(3, con2.learning_rate)
        self.assertEqual(2, con2.weight)

    def testConnectionSplitBeginingShouldBeWithBaseValues(self):
        gen = self.setUpSimpleGenome()
        con2 = gen.connections[1]
        self.assertEqual(0.01, con2.learning_rate)
        self.assertEqual(1, con2.weight)

    def testSplitOfNoneShouldThrow(self):
        gen = self.setUpSimpleGenome()
        try:
            gen.exec(SplitConnection(None))
            self.fail()
        except(NEATDQNException):
            pass

    def testSplitOfNotExistingShouldThrow(self):
        gen = self.setUpSimpleGenome()
        try:
            gen.exec(SplitConnection(213))
            self.fail()
        except(NEATDQNException):
            pass

    def setUpSimpleGenome(self):
        gen = GenomeFactory(Config(1, 1)).createInitial()
        con = gen.connections[0]
        con.weight = 2
        con.learning_rate = 3
        gen.exec(SplitConnection(con.innovationNumber))
        return gen

