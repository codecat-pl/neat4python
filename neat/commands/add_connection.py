from .command import Command


class AddConnection(Command):
    def __init__(self, f, t):
        self.f = f
        self.t = t

    def onGenome(self, gen):
        a = gen.findInnov(self.f)
        b = gen.findInnov(self.t)
        con = gen.factory.createConnection(a, b)
        gen.addGene(con)

