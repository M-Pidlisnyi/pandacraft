
class MapManager():
    def __init__(self):
        self.startNew()
        self.model = "block.egg"
        self.texture = "block.png"

        self.color = (0.1, 0.5, 0.9, 1)#rgba
        self.addBlock((0,10,0))

    def startNew(self):
        self.land = render.attachNewNode("Land")

    def addBlock(self, position ):
        self.block = loader.loadModel(self.model)
        self.block.setTexture( loader.loadTexture(self.texture) )

        self.block.setColor(self.color)

        self.block.setPos(position)
        self.block.reparentTo(self.land)
