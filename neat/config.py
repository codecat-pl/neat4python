import random
from .mutation_rates import MutationRates

class Config:
    def __init__(self, inp, out):
        self.population = 10

        self.inputsCount = inp
        self.outputsCount = out

        self.connectionMutationRate = 0.8
        self.connectionReplaceRate = 0.1
        self.connectionMutationMi = 0
        self.connectionMutationSi = 0.01

        self.genomeConnectionMutationRate = 0.5
        self.genomeNodeMutationRate = 0.3
        self.genomeRemoveConnectionRate = 0.2
        self.genomeRemoveNodeRate = 0.1

        self.distanceWeightCoefficient = 1.0
        self.distanceDisjointCoefficient = 1.0

        self.mutationRates = MutationRates(self)

    def randint(self, a, b):
        return random.randint(a, b)

    def rand(self):
        return random.random()

    def gauss(self, mi, si):
        return random.gauss(mi,si)
