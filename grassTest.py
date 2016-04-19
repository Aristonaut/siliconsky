#!/usr/bin/env python

from math import pi, sin, cos

from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from panda3d.core import CardMaker

class Test(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        cm = CardMaker('grass')
        cm.setFrame(-1, 1, -1, 1)

        grass1 = render.attachNewNode(cm.generate())
        grass2 = render.attachNewNode(cm.generate())

        grass1.setTexture(loader.loadTexture("data/env/grass1.png"), 1)
        grass2.setTexture(loader.loadTexture("data/env/grass2.png"), 1)

        grass1.setTransparency(True)
        grass2.setTransparency(True)

        grass1.setBillboardPointEye()
        grass2.setBillboardPointEye()

        grass1.setHpr(0, -40, 0)
        grass2.setHpr(0, -40, 0)

        grass1.setPos(0, 1, -0.4)
        grass2.setPos(0, 1, -0.3)

        self.taskMgr.add(self.panCameraTask, "PanCameraTask")

    def panCameraTask(self, task):
        posDegrees = task.time * 6.0
        posRadians = posDegrees * (pi / 180.0)

        self.camera.setPos( 0.4 * cos(4.0 * posRadians), 0, -0.01)

        return Task.cont


if __name__ == "__main__":
    test = Test()
    test.run()
