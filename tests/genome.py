import tensorflow as tf

from ..neat import *
from ..neat.commands import *

class GenomeTests(tf.test.TestCase):
    def setUp(self):
        self.factory = GenomeFactory(Config(3, 4))
        self.genome = self.factory.createInitial()
        pass

    def testGenomeShouldHaveInputsAndOutputs(self):
        self.assertEqual(3, len(self.genome.input))
        self.assertEqual(4, len(self.genome.output))

    def testGenomeShouldCreateInputNodes(self):
        self.assertEqual(3, len(self.genome.input))
        self.assertEqual(Node, type(self.genome.input[0]))

    def testGenomeShouldCreateWithUniqueInnovation(self):
        id1 = self.genome.input[0].innovationNumber
        id2 = self.genome.input[1].innovationNumber
        id3 = self.genome.output[0].innovationNumber
        id4 = self.genome.output[1].innovationNumber
        self.assertNotEqual(id1, id2)
        self.assertNotEqual(id3, id4)
        self.assertNotEqual(id1, id3)

    def testGenomeShouldCreateOutputs(self):
        self.assertEqual(4, len(self.genome.output))
        self.assertEqual(Node, type(self.genome.output[0]))

    def testGenomeShouldCreateFullyConnected(self):
        self.assertEqual(12, len(self.genome.connections))

    def testClone(self):
        genome2 = self.factory.createCopy(self.genome)
        genome2.connections[0].weight += 1
        self.assertEqual(genome2.inputsCount, self.genome.inputsCount)
        self.assertEqual(genome2.outputsCount, self.genome.outputsCount)
        self.assertNotEqual(genome2.connections[0].weight, self.genome.connections[0].weight)

    def testCloneShouldMoveFactory(self):
        genome2 = self.factory.createCopy(self.genome)
        id1 = genome2.factory.createNode('hidden').innovationNumber
        id2 = self.genome.factory.createNode('hidden').innovationNumber
        self.assertEqual(id1+1, id2)

    def testConfigWithRandomIntValues(self):
        class TestConfig(Config):
            def randint(self, a, b):
                return 1
        conf = TestConfig(1, 2)
        gen = GenomeFactory(conf).createInitial()
        gen.exec(SplitConnectionMutation())
        self.assertTrue(gen.connections[1].disabled)
