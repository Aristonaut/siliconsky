
from panda3d.core import NodePath

class PawnPart(NodePath):
    """ PawnPart
    PawnPart is part of an animated character or object
    PawnPart is the base class of PawnPart2d and PawnPart3d
    A body object should lie at the root with PawnPart2d
    and PawnPart3d objects as children
    """
    def __init__(self):
        NodePath.__init__(self)
