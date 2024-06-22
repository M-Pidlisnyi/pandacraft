from direct.showbase.ShowBase import ShowBase
from direct.gui.OnscreenImage import OnscreenImage
import builtins
from mapmanager import MapManager
from hero import Hero

class Game(ShowBase):
    def __init__(self):
        super().__init__()
        self.land  = MapManager()
        self.land.loadLand("land.txt")
        self.hero = Hero((2,0,2), self.land)
        OnscreenImage(parent=builtins.render2d, image="stars.jpg")
        builtins.base.cam.node().getDisplayRegion(0).setSort(20)
        builtins.base.setBackgroundColor(0, 0.4, 0.9)
        builtins.base.camLens.setFov(90)
        builtins.taskMgr.add(self.hero.followMouse, "followMouse")


game = Game()
game.run()