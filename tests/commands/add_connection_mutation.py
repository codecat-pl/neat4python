import tensorflow as tf

from ...neat import *
from ...neat.commands import *


class AddConnectionMutationOpTest(tf.test.TestCase):
    def testOpAddConnectionMutation(self):
        genome = GenomeFactory(Config(1, 1)).createInitial()
        node = genome.factory.createNode('hidden')
        genome.addGene(node)
        genome.exec(AddConnectionMutation())
        self.assertEqual(2, len(genome.connections))


