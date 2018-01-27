import tensorflow as tf

from ...neat import *
from ...neat.commands import *


class RemoveConnectionOpTest(tf.test.TestCase):
    def testOpRemoveConnectionMutation(self):
        genome = GenomeFactory(Config(1, 1)).createInitial()
        genome.exec(RemoveConnection(genome.connections[0].innovationNumber))
        self.assertEqual(0, len(genome.connections))

