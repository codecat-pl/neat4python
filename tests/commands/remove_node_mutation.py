import tensorflow as tf

from ...neat import *
from ...neat.commands import *

class RemoveNodeMutationOpTest(tf.test.TestCase):
    def testOpRemoveNodeMutation(self):
        genome = GenomeFactory(Config(1, 1)).createInitial()
        node = genome.factory.createNode('hidden')
        genome.addGene(node)
        genome.exec(RemoveNodeMutation())
        self.assertEqual(2, len(genome.nodes))

