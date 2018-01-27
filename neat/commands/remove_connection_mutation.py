from .command import Command
from .remove_connection import RemoveConnection


class RemoveConnectionMutation(Command):
    def onGenome(self, gen):
        con = gen.getRandomConnection()
        if con is not None:
            gen.exec(RemoveConnection(con.innovationNumber))

