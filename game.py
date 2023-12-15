from direct.showbase.ShowBase import ShowBase
from mapmanager import MapManager
from hero import Hero

class Game(ShowBase):
    def __init__(self):
        super().__init__()
        self.land = MapManager()
        self.land.loadLand("land.txt")
        self.hero=Hero((3,5,1),self.land)
        base.setBackgroundColor(0,0.6,0.7)
        base.camLens.setFov(90)
        taskMgr.add(self.hero.followMouse, "followMouse")
      
Game().run()

