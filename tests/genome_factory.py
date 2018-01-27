import tensorflow as tf

from ..neat import *

class GenomeFactoryTest(tf.test.TestCase):
    def setUp(self):
        self.factory = GenomeFactory(Config(2,3))

    def testGenomeCreation(self):
        gen = self.factory.createInitial()
        self.assertEqual(2, len(gen.input))
        self.assertEqual(3, len(gen.output))
        self.assertEqual(6, len(gen.connections))

    def testMassCreateInitital(self):
        ret = []
        for a in self.factory.createInitialPopulation(10):
            ret.append(a)
        self.assertEqual(10, len(ret))

    def testCopy(self):
        gen, gen2 = self.createCopiedGenomes()
        self.assertEqual(len(gen.connections), len(gen2.connections))
        self.assertEqual(len(gen.nodes), len(gen2.nodes))

    def testOtherObjectAfterCopy(self):
        gen, gen2 = self.createCopiedGenomes()
        gen2.connections[0].weight += 1
        self.assertNotEqual(gen.connections[0].weight, gen2.connections[0].weight)

    def testCrossing(self):
        gen, gen2 = self.createCopiedGenomes()
        gen2.addGene(gen2.factory.createNode('hidden'))
        gen3 = self.factory.createByCrossing(gen, gen2)
        self.assertEqual(6, len(gen3.nodes))

    def createCopiedGenomes(self):
        gen = self.factory.createInitial()
        gen2 = self.factory.createCopy(gen)
        return gen, gen2