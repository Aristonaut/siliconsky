
from ssky.pawn.pawn import Pawn
from ssky.pawn.pawnPart2d import PawnPart2d
from ssky.pawn.pawnPart3d import PawnPart3d

from panda3d.core import NodePath, PandaNode
from direct.actor.Actor import Actor

class TestPanda3d(PandaNode):
    def __init__(self, *args, **argv):
        PandaNode.__init__(self, *args, **argv)

        self.pandaActor = Actor("panda-model",
                                {"walk": "panda-walk4"})
        self.pandaActor.reparentTo(self)
        print("self:" + str(self.is_empty()))
        self.pandaActor.loop("walk")

class TestPanda2d(Pawn):
    def __init__(self):
        Pawn.__init__(self)

class TestPandaMix(Pawn):
    def __init__(self):
        Pawn.__init__(self)
