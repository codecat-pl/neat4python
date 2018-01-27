from .command import Command
from .add_connection import AddConnection


class AddConnectionMutation(Command):
    def onGenome(self, gen):
        source = gen.getRandomNode()
        destination = gen.getRandomNode()
        while source.type == 'output':
            source = gen.getRandomNode()
        while destination.type == 'input':
            destination = gen.getRandomNode()
        gen.exec(AddConnection(source.innovationNumber, destination.innovationNumber))

