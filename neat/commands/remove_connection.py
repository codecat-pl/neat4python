from .command import Command


class RemoveConnection(Command):
    def __init__(self, id):
        self.id = id

    def onGenome(self, gen):
        gen.rmGene(gen.findInnov(self.id))


