
import tensorflow as tf
import random
from ..neat import *


class FakeConf(Config):
    def __init__(self):
        super().__init__(1, 1)
        self.randomValue = 0

    def rand(self):
        return self.randomValue

    def gauss(self, mi, si):
        return mi+si


class TestRates(tf.test.TestCase):
    def testShouldAddConnectionTrue(self):
        r = self.setupRatesAndRandom(0.3, 0.2)
        self.assertTrue(r.shouldAddConnection())

    def testShouldAddConnectionFalse(self):
        r = self.setupRatesAndRandom(0.3, 0.4)
        self.assertFalse(r.shouldAddConnection())

    def testShouldRemoveConnectionTrue(self):
        r = self.setupRatesAndRandom(0.3, 0.2)
        self.assertTrue(r.shouldRemoveConnection())

    def testShouldRemoveConnectionFalse(self):
        r = self.setupRatesAndRandom(0.3, 0.4)
        self.assertFalse(r.shouldRemoveConnection())

    def testShouldRemoveNodeTrue(self):
        r = self.setupRatesAndRandom(0.3, 0.2)
        self.assertTrue(r.shouldRemoveNode())

    def testShouldRemoveNodeFalse(self):
        r = self.setupRatesAndRandom(0.3, 0.4)
        self.assertFalse(r.shouldRemoveNode())

    def testShouldAddNodeTrue(self):
        r = self.setupRatesAndRandom(0.3, 0.2)
        self.assertTrue(r.shouldAddNode())

    def testShouldAddNodeFalse(self):
        r = self.setupRatesAndRandom(0.3, 0.4)
        self.assertFalse(r.shouldAddNode())

    def testShouldMutateConnectionTrue(self):
        r = self.setupRatesAndRandom(0.3, 0.2)
        self.assertTrue(r.shouldChangeConnection())

    def testShouldMutateConnectionFalse(self):
        r = self.setupRatesAndRandom(0.3, 0.4)
        self.assertFalse(r.shouldChangeConnection())

    def testShouldReplaceConnectionTrue(self):
        r = self.setupRatesAndRandom(0.3, 0.2)
        self.assertTrue(r.shouldReplaceConnection())

    def testShouldReplaceConnectionFalse(self):
        r = self.setupRatesAndRandom(0.3, 0.4)
        self.assertFalse(r.shouldReplaceConnection())

    def testGetMutationRate(self):
        conf = FakeConf()
        conf.connectionMutationMi = 2
        conf.connectionMutationSi = 3
        r = MutationRates(conf)
        self.assertEqual(5, r.getMutationRate())

    def setupRatesAndRandom(self, rates, rand):
        conf = FakeConf()
        conf.randomValue = rand
        conf.genomeConnectionMutationRate = rates
        conf.genomeRemoveConnectionRate = rates
        conf.genomeNodeMutationRate = rates
        conf.genomeRemoveNodeRate = rates
        conf.connectionReplaceRate = rates
        conf.connectionMutationRate = rates
        return MutationRates(conf)