from .command import Command
from .remove_node import RemoveNode


class RemoveNodeMutation(Command):
    def onGenome(self, gen):
        node = gen.getRandomHiddenNode()
        if node is None:
            return
        gen.exec(RemoveNode(node.innovationNumber))

