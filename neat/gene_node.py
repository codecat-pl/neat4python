
from .exceptions import NEATDQNException


class Node:
    def __init__(self, conf, innovation, type):
        self.conf = conf
        self.type = type
        self.innovationNumber = innovation

    def clone(self):
        return Node(self.conf, self.innovationNumber, self.type)

    def exec(self, op):
        return op.onNode(self)

