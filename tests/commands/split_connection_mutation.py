import tensorflow as tf

from ...neat import *
from ...neat.commands import *


class SplitConnectionMutationOpTest(tf.test.TestCase):
    def testOpSplitConnectionMutation(self):
        genome = GenomeFactory(Config(1, 1)).createInitial()
        op = SplitConnectionMutation()
        genome.exec(op)
        self.assertEqual(3, len(genome.nodes))
