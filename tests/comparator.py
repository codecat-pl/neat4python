import tensorflow as tf

from ..neat import *
from ..neat.commands import *


class ComparatorTests(tf.test.TestCase):
    def setUp(self):
        self.comp = GenomeComparator()
        self.config = Config(1, 1)

    def testComparationOfSameGenomes(self):
        g1, g2 = self.createTwoSameGenomes()
        distance = self.comp.distance(g1, g2)
        self.assertEqual(0, distance)

    def testDifferentLearningRate(self):
        g1, g2 = self.createTwoGenomesWithLearningRate(difference=2)
        distance = self.comp.distance(g1, g2)
        self.assertEqual(2, distance)

    def testDifferentTopology(self):
        g1, g2 = self.createTwoGenomesOneSplited()
        distance = self.comp.distance(g1, g2)
        self.assertEqual(4, distance)

    def testWeightCoefficient(self):
        self.config.distanceWeightCoefficient = 0.5
        self.config.distanceDisjointCoefficient = 0
        g1, g2 = self.createTwoGenomesWithLearningRate(difference=2)
        distance = self.comp.distance(g1, g2)
        self.assertEqual(1, distance)

    def testDisjointCoefficient(self):
        self.config.distanceWeightCoefficient = 0
        self.config.distanceDisjointCoefficient = 2
        g1, g2 = self.createTwoGenomesOneSplited()
        distance = self.comp.distance(g1, g2)
        self.assertEqual(6, distance)

    def createTwoGenomesOneSplited(self):
        g1, g2 = self.createTwoSameGenomes()
        g2.exec(SplitConnectionMutation())
        return g1, g2

    def createTwoGenomesWithLearningRate(self, difference):
        g1, g2 = self.createTwoSameGenomes()
        g1.connections[0].learning_rate = 2
        g2.connections[0].learning_rate = 2 + difference
        return g1, g2

    def createTwoSameGenomes(self):
        fac = GenomeFactory(self.config)
        g1 = fac.createInitial()
        g2 = fac.createCopy(g1)
        return g1, g2