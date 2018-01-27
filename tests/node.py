import tensorflow as tf

from ..neat import Config, InnovationFactory, Node


class NodeTest(tf.test.TestCase):
    def setUp(self):
        self.factory = InnovationFactory(Config(1,1))

    def testNode(self):
        node = Node(Config(1, 1), 0, 'hidden')
        self.assertTrue(type(node.innovationNumber) is int)

    def testNodeShouldHaveType(self):
        node = self.factory.createNode('input')
        self.assertTrue(node.type, 'input')

