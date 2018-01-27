from .command import Command
from .add_connection_mutation import AddConnectionMutation
from .remove_node_mutation import RemoveNodeMutation
from .remove_connection_mutation import RemoveConnectionMutation
from .split_connection_mutation import SplitConnectionMutation


class Mutate(Command):
    def onGenome(self, gen):
        self.mutateAllGenes(gen)

        r = gen.conf.mutationRates
        if r.shouldAddConnection():
            gen.exec(AddConnectionMutation())
        if r.shouldAddNode():
            gen.exec(SplitConnectionMutation())
        if r.shouldRemoveConnection():
            gen.exec(RemoveConnectionMutation())
        if r.shouldRemoveNode():
            gen.exec(RemoveNodeMutation())

    def mutateAllGenes(self, gen):
        [g.exec(self) for g in gen.genes]

    def onConnection(self, con):
        r = con.conf.mutationRates
        if r.shouldChangeConnection():
            rate = r.getMutationRate()
            if r.shouldReplaceConnection():
                con.learning_rate = rate
            else:
                con.learning_rate += rate

