import tensorflow as tf

from ..neat import *

class InnovationFactoryTest(tf.test.TestCase):
    def setUp(self):
        self.factory = InnovationFactory(Config(1,1))
        self.node_in = self.factory.createNode('input')
        self.node_out = self.factory.createNode('output')

    def testFactoryNode(self):
        self.assertTrue(type(self.factory.createNode('hidden')) is Node)

    def testFactoryCreatingObjectsWithUniqueInnovationNumber(self):
        id1 = self.node_in.innovationNumber
        id2 = self.node_out.innovationNumber
        self.assertNotEqual(id1, id2, 'Factory returned innovation numbers that are not unique')

    def testFactoryConnection(self):
        self.assertTrue(type(self.factory.createConnection(self.node_in, self.node_out)) is Connection)

    def testFactoryCreatingUniqueInnovationsAcrossAllTypes(self):
        id1 = self.node_in.innovationNumber
        id3 = self.node_out.innovationNumber
        id2 = self.factory.createConnection(self.node_in, self.node_out).innovationNumber
        self.assertNotEqual(id1, id2, 'Factory returned innovation numbers that are not unique')
        self.assertNotEqual(id1, id3, 'Factory returned innovation numbers that are not unique')
        self.assertNotEqual(id2, id3, 'Factory returned innovation numbers that are not unique')

    def testFactoryShouldCreateConnectionsOnlyIfNotExist(self):
        id1 = self.factory.createConnection(self.node_in, self.node_out).innovationNumber
        id2 = self.factory.createConnection(self.node_in, self.node_out).innovationNumber
        self.assertEqual(id1, id2)

    def testCrossingNodes(self):
        p1 = self.factory.createNode('hidden')
        p2 = self.factory.createNode('hidden')
        node = self.factory.createGeneByCrossing(p1, p2)
        self.assertEqual(Node, type(node))
        self.assertEqual('hidden', node.type)
        self.assertNotEqual(node, p1)
        self.assertNotEqual(node, p2)

    def crossingGenesCommon(self, rand):
        class FakeConf(Config):
            def rand(self):
                return rand

        conf = FakeConf(1, 1)
        fac = InnovationFactory(conf)
        p1 = Connection(conf, 2, 1, 2)
        p2 = p1.clone()
        p1.learning_rate = 3
        p2.learning_rate = 5
        return fac.createGeneByCrossing(p1, p2)

    def testCrosingConnectionsTakeRight(self):
        node = self.crossingGenesCommon(1)
        self.assertEqual(5, node.learning_rate)

    def testCrosingConnectionsTakeLeft(self):
        node = self.crossingGenesCommon(0)
        self.assertEqual(3, node.learning_rate)
