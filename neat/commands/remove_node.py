from .command import Command


class RemoveNode(Command):
    def __init__(self, id):
        self.id = id

    def onGenome(self, gen):
        node = gen.findInnov(self.id)
        if node is None:
            return
        for c in gen.getConnectionsByNode(self.id):
            gen.rmGene(c)
        gen.rmGene(node)

