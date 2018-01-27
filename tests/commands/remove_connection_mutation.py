import tensorflow as tf

from ...neat import *
from ...neat.commands import *


class RemoveConnectionMutationOpTest(tf.test.TestCase):
    def testOpRemoveConnectionMutation(self):
        genome = GenomeFactory(Config(1, 1)).createInitial()
        genome.exec(RemoveConnectionMutation())
        self.assertEqual(0, len(genome.connections))


