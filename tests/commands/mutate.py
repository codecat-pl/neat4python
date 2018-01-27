import tensorflow as tf

from ...neat import *
from ...neat.commands import *
from .helpers import *

class MutateOpTest(tf.test.TestCase):
    def testAddConnectionRate(self):
        gen = self.createAndMutateGenome('shouldAddConnection')
        self.assertEqual(AddConnectionMutation, gen.lastType)

    def testConfigWithAddNodeRate(self):
        gen = self.createAndMutateGenome('shouldAddNode')
        self.assertEqual(SplitConnectionMutation, gen.lastType)

    def testConfigWithConnectionRemoveRate(self):
        gen = self.createAndMutateGenome('shouldRemoveConnection')
        self.assertEqual(RemoveConnectionMutation, gen.lastType)

    def testConfigWithNodeRemoveRate(self):
        gen = self.createAndMutateGenome('shouldRemoveNode')
        self.assertEqual(RemoveNodeMutation, gen.lastType)

    @staticmethod
    def createAndMutateGenome(action):
        gen = MutationGenomeFactory().createInitial()
        setattr(gen.conf, action, True)
        m = Mutate()
        m.onGenome(gen)
        return gen

    def testMutateShouldAffectEveryGene(self):
        conf = MutationTestConfig(1, 1)
        gen = GenomeFactory(conf).createInitial()
        node = FakeNode(conf)
        gen.addGene(node)
        gen.exec(Mutate())
        self.assertEqual(Mutate, node.last)

    def testMutationOfConnectionGene(self):
        conf = MutationTestConfig(0, 0)
        conf.shouldChangeConnection = True
        con = FakeConnection(conf, learning_rate=2)
        conf.mutationRate = 3
        con.exec(Mutate())
        self.assertEqual(5, con.learning_rate)

    def testReplacementOfConnectionGene(self):
        conf = MutationTestConfig(0, 0)
        conf.shouldChangeConnection = True
        conf.shouldReplaceConnection = True
        conf.mutationRate = 3
        con = FakeConnection(conf, learning_rate=10)
        con.exec(Mutate())
        self.assertEqual(3, con.learning_rate)
