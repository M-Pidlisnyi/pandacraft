from direct.showbase.ShowBase import ShowBase
import builtins
from mapmanager import MapManager
from hero import Hero

class Game(ShowBase):
    def __init__(self):
        super().__init__()
        self.land  = MapManager()
        self.land.loadLand("land.txt")
        self.hero = Hero((2,0,2), self.land)
        builtins.base.camLens.setFov(90)


game = Game()
game.run()