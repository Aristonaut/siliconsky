
from panda3d.core import NodePath

class PawnPart3d(NodePath):
    def __init__(self):
        NodePath.__init__(self)

from direct.showbase.DirectObject import DirectObject
from pandac.PandaModules import TextureStage
from pandac.PandaModules import NodePath ,CardMaker

class tileSHEET():
    def __init__(self,speed,raws,cells,tex):
        self.timer=0
        self.offsetV = 0
        self.offsetU = 0
        self.u = 0
        self.v = 0

        self.speed = speed

        self.raws = raws
        self.sizeRAWS = 1.00/self.raws

        self.cells = cells
        self.sizeCELLS = 1.00/self.cells

        self.ts = TextureStage('ts')
        self.tile = self.createCARD(tex, self.sizeCELLS, self.sizeRAWS)

        taskMgr.add(self.anim,"anim")

    def createCARD(self, tex, sizeCELLS, sizeRAWS):
        card = CardMaker("tilesheet")
        tile = NodePath(card.generate())
        tile.reparentTo(render2d)
        tile.setTexScale(self.ts,sizeCELLS,sizeRAWS)
        tile.setTexture(self.ts, tex)
        return tile

    def setPOS(self, x, y, z):
        self.tile.setPos(x,y,z)

    def swap(self, timer):
        self.tile.setTexOffset(self.ts,self.offsetU,self.offsetV)
        if (self.timer > self.speed):
            self.timer =0
            self.offsetU+=self.sizeRAWS
            self.u+=1
            if (self.u >= self.cells):
                self.u = 0
                self.v+=1
                self.offsetU = 0
                self.offsetV+=self.sizeCELLS
            if (self.v >= self.cells):
                self.v= 0
                self.offsetV = 0

    def anim(self, task):
        self.timer+=1
        self.swap(self.timer)
        return task.cont
