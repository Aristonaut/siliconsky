#!/usr/bin/env python

from direct.showbase.ShowBase import ShowBase
from panda3d.core import OrthographicLens

from ssky.baddies.testPanda import TestPanda3d

class PawnTest(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        lens = OrthographicLens()
        base.cam.node().setLens(lens)

        panda = TestPanda3d("testPanda3d")
        #print("panda:" + str(panda.is_empty()))
        panda.reparentTo(render)

if __name__ == "__main__":
    game = PawnTest()
    game.run()
