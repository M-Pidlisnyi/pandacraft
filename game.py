from direct.showbase.ShowBase import ShowBase
import builtins
from mapmanager import MapManager


class Game(ShowBase):
    def __init__(self):
        super().__init__()
        self.land  = MapManager()
        self.land.loadLand("land.txt")
        builtins.base.camLens.setFov(90)


game = Game()
game.run()