from .command import Command
from .split_connection import SplitConnection


class SplitConnectionMutation(Command):
    def onGenome(self, gen):
        con = gen.getRandomConnection()
        while con.disabled:
            con = gen.getRandomConnection()
        gen.exec(SplitConnection(con.innovationNumber))
