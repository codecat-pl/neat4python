class Command:
    def exec(self, ob):
        met = getattr(self, "on"+type(ob).__name__)
        return met(ob)

    def onNode(self, a):
        pass

    def onConnection(self, a):
        pass

    def onGenome(self, a):
        pass
