from .command import Command
from ..exceptions import NEATDQNException


class SplitConnection(Command):
    def __init__(self, id):
        self.id = id

    def onGenome(self, gen):
        tcon = gen.findInnov(self.id)
        if tcon is None:
            raise NEATDQNException("split of not existing connection")
        tcon.disabled = True
        source = gen.findInnov(tcon.source)
        destination = gen.findInnov(tcon.destination)
        node = gen.factory.createNode('hidden')
        gen.addGene(node)
        con1 = gen.factory.createConnection(source, node)
        con2 = gen.factory.createConnection(node, destination)
        con2.learning_rate = tcon.learning_rate
        con2.weight = tcon.weight
        gen.addGene(con1)
        gen.addGene(con2)
