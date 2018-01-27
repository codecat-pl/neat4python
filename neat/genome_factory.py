from .innovation_factory import InnovationFactory
from .genome import Genome


class GenomeFactory:
    def __init__(self, conf):
        self.conf = conf
        self.ifac = InnovationFactory(conf)

    def initConfig(self, gen):
        ifac = gen.factory = self.ifac
        for i in range(self.conf.inputsCount):
            gen.addGene(ifac.createNode('input'))
        for i in range(self.conf.outputsCount):
            gen.addGene(ifac.createNode('output'))
        for source in gen.input:
            for destination in gen.output:
                gen.addGene(ifac.createConnection(source, destination))

    def createInitial(self):
        gen = Genome(self.conf)
        self.initConfig(gen)
        return gen

    def createInitialPopulation(self, count):
        gen = Genome(self.conf)
        for i in range(count):
            yield self.createCopy(gen)

    def createCopy(self, source):
        gen = Genome(self.conf)
        gen.factory = self.ifac
        [gen.addGene(gene.clone()) for gene in source.nodes]
        [gen.addGene(gene.clone()) for gene in source.connections]
        return gen

    def createByCrossing(self, g1, g2):
        out = Genome(self.conf)
        out.factory = self.ifac
        for gene in g1.genes:
            if gene.innovationNumber not in g2.dict:
                out.addGene(gene.clone())
            else:
                out.addGene(self.ifac.createGeneByCrossing(gene, g2.dict[gene.innovationNumber]))
        for gene in g2.genes:
            if gene.innovationNumber not in g1.dict:
                out.addGene(gene.clone())
        return out