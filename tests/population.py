
import tensorflow as tf

from ..neat import *


class Population:
    def __init__(self, conf):
        self.count = conf.population
        self.individuals = []
        self.factory = GenomeFactory(conf)

    def init(self):
        for i in self.factory.createInitialPopulation(self.count):
            self.individuals.append(i)


class PopulationTest(tf.test.TestCase):
    def testPopulation(self):
        pop = Population(Config(1, 1))
        self.assertEqual(0, len(pop.individuals))

    def testInitialPopulation(self):
        pop = Population(Config(1,1))
        pop.init()
        self.assertEqual(10, pop.count)
        self.assertEqual(10, len(pop.individuals))
        self.assertEqual(Genome, type(pop.individuals[0]))
