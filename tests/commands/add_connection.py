import tensorflow as tf

from ...neat import *
from ...neat.commands import *


class AddConnectionOpTest(tf.test.TestCase):
    def testOpAddConnection(self):
        genome = GenomeFactory(Config(1, 1)).createInitial()
        node = genome.factory.createNode('hidden')
        genome.addGene(node)
        genome.exec(AddConnection(genome.input[0].innovationNumber, node.innovationNumber))
        self.assertEqual(2, len(genome.connections))

