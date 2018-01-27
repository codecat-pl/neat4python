from .exceptions import NEATDQNException
from .config import Config
from .genome import *
from .innovation_factory import InnovationFactory


class GenomeComparator:
    def distance(self, gen, gen2):
        dist = 0
        weights = 0
        checked = []
        for key in gen.dict:
            checked.append(key)
            if key not in gen2.dict:
                dist += 1
            else:
                weights += self.geneDistance(gen.dict[key], gen2.dict[key])

        for key in gen2.dict:
            if key not in checked:
                if key not in gen.dict:
                    dist += 1
                else:
                    weights += self.geneDistance(gen.dict[key], gen2.dict[key])

        return gen.conf.distanceDisjointCoefficient * dist + gen.conf.distanceWeightCoefficient * weights

    def geneDistance(self, g1, g2):
        if g1.innovationNumber != g2.innovationNumber:
            raise NEATDQNException('cannot check distance of object with different innovationNumbers')
        if type(g1) == Connection:
            return self.connectionDistance(g1, g2)
        else:
            return self.nodeDistance(g1, g2)

    def connectionDistance(self, g1,g2):
        additional = 0
        if g1.disabled != g2.disabled:
            additional += 1
        return abs(g1.learning_rate - g2.learning_rate) + \
               abs(g1.weight - g2.weight) + \
               additional

    def nodeDistance(self, g1, g2):
        return 0
