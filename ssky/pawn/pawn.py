
from panda3d.core import NodePath

class Pawn(NodePath):
    """ Pawn
    Pawn is the base of an animated character or object
    A body object should lie at the root with PawnPart2d
    and PawnPart3d objects as children
    """
    def __init__(self):
        NodePath.__init__(self)
