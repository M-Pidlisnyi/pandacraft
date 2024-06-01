import builtins

class MapManager():
    def __init__(self) -> None:
        self.model = "block.egg"
        self.texture = "block.png"
        self.color = (0.2, 0.2, 0.35, 1)

        self.startNew()
        self.addBlock((0,10,0))


    def startNew(self):
        self.land = builtins.render.attachNewNode("Land")

    def addBlock(self, position:  tuple[int,int,int]):
        self.block = builtins.loader.loadModel(self.model)
        texture = builtins.loader.loadTexture(self.texture)
        self.block.setTexture(texture)
        self.block.setColor(self.color)
        self.block.setPos(position)
        self.block.reparentTo(self.land)

        self.block.setTag("at", str(position))

    def clear(self):
        self.land.removeNode()
        self.startNew()

    def loadLand(self, filename):
        self.clear()
        with open(filename, 'r') as file:
            y = 0
            for line in file:
                x = 0
                line = line.split(" ")
                for z in line:
                    for z0 in range(int(z)+1):
                        self.addBlock((x, y,z0))
                    x += 1
                y += 1
    

    def isEmpty(self, pos):
        blocks = self.findBlock(pos)
        
        return not bool(blocks)
    
    def findHighestEmpty(self,pos):
        x,y,z = pos
        z = 1
        while not self.isEmpty((x,y,z)):
            z += 1
        return (x,y,z)

    
    def findBlock(self, pos):
        return self.land.findAllMatches("=at="+str(pos))
