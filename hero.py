import builtins
class Hero:
    def __init__(self, pos:tuple, land):
        self.land = land
        self.hero = builtins.loader.loadModel("smiley")
        self.hero.setScale(0.3)
        self.hero.setPos(pos)
        self.hero.setH(180)
        self.hero.reparentTo(builtins.render)


        self.cameraBind()
        self.acceptEvents()
        


    def cameraBind(self):
        builtins.base.disableMouse()
        builtins.base.camera.reparentTo(self.hero)
        builtins.base.camera.setPos(0,0,1.5)
        builtins.base.camera.setH(180)
        self.cameraOn = True

    
    def cameraUnbind(self):
        pos = self.hero.getPos()
        builtins.base.mouseInterfaceNode.setPos(-pos[0], -pos[1], pos[2]-4)
        builtins.base.camera.reparentTo(builtins.render)
        builtins.base.enableMouse()
        self.cameraOn = False

    
    def changeCamera(self):
        if self.cameraOn:
            self.cameraUnbind()
        else:
            self.cameraBind()
        
    
    def turnLeft(self):
        h = self.hero.getH()
        self.hero.setH(h+5)

    def turnRight(self):
        h = self.hero.getH()
        self.hero.setH(h-5)
    

    def justMove(self, angle):
        pass
    def tryMove(self, angle):
        pass
    def moveTo(self, angle):
        pass
    


    def acceptEvents(self):
        builtins.base.accept(change_camera_key, self.changeCamera)
        builtins.base.accept(turn_left_key, self.turnLeft)
        builtins.base.accept(turn_left_key+"-repeat", self.turnLeft)
        builtins.base.accept(turn_right_key, self.turnRight)
        builtins.base.accept(turn_right_key+"-repeat", self.turnRight)


change_camera_key = "c"
turn_left_key = "arrow_left"
turn_right_key = "arrow_right"
