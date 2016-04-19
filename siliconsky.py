#!/usr/bin/env python

from direct.showbase.ShowBase import ShowBase

class SiliconSky(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

if __name__ == "__main__":
    game = SiliconSky()
    game.run()
