import random

class MutationRates:
    def __init__(self, conf):
        self.conf = conf

    def rand(self):
        return random.random()

    def shouldAddConnection(self):
        return self.conf.rand() < self.conf.genomeConnectionMutationRate

    def shouldRemoveConnection(self):
        return self.conf.rand() < self.conf.genomeRemoveConnectionRate

    def shouldAddNode(self):
        return self.conf.rand() < self.conf.genomeNodeMutationRate

    def shouldRemoveNode(self):
        return self.conf.rand() < self.conf.genomeRemoveNodeRate

    def shouldChangeConnection(self):
        return self.conf.rand() < self.conf.connectionMutationRate

    def shouldReplaceConnection(self):
        return self.conf.rand() < self.conf.connectionReplaceRate

    def getMutationRate(self):
        return self.conf.gauss(self.conf.connectionMutationMi, self.conf.connectionMutationSi)
