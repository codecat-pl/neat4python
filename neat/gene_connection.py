
from .exceptions import NEATDQNException


class Connection:
    def __init__(self, conf,  innovation, source, destination):
        self.conf = conf
        self.innovationNumber = innovation
        self.learning_rate = 0.01
        self.weight = 1.0
        self.source = source
        self.destination = destination
        self.disabled = False

    def clone(self):
        con = Connection(self.conf, self.innovationNumber, self.source, self.destination)
        con.learning_rate = self.learning_rate
        con.weight = self.weight
        con.disabled = self.disabled
        return con

    def exec(self, op):
        return op.onConnection(self)