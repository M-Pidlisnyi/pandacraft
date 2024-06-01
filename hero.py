import builtins
class Hero:
    def __init__(self, pos:tuple, land):
        self.land = land
        self.hero = builtins.loader.loadModel("smiley")
        self.hero.setScale(0.3)
        self.hero.setPos(pos)
        self.hero.setH(180)
        self.hero.reparentTo(builtins.render)

        self.spectatorMode = True

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
        h = self.hero.getH() % 360
        self.hero.setH(h+5)

    def turnRight(self):
        h = self.hero.getH() % 360
        self.hero.setH(h-5)
    

    def justMove(self, angle):
        new_pos = self.lookAt(angle)
        self.hero.setPos(new_pos)


    def tryMove(self, angle):
        pass

    def moveTo(self, angle):
        if self.spectatorMode:
            self.justMove(angle)
        else:
            self.tryMove(angle)
    

    def lookAt(self,angle):
        from_x = round(self.hero.getX())
        from_y = round(self.hero.getY())
        from_z = round(self.hero.getZ())

        dx, dy = self.checkDir(angle)

        return from_x+dx, from_y+dy, from_z

    def checkDir(self,angle):
        if angle >= 0 and angle <= 20:
            return 0, -1
        elif angle <= 65:
            return +1, -1
        elif angle <= 110:
            return +1, 0
        elif angle <= 155:
            return +1, +1
        elif angle <= 200:
            return 0, +1
        elif angle <= 245:
            return -1, +1
        elif angle <= 290:
            return -1, 0
        elif angle <= 335:
            return -1, -1
        else:
            return 0, -1

    def forward(self):
        h = self.hero.getH() % 360
        self.moveTo(h)

    def backward(self):
        h = (self.hero.getH() + 180)  % 360
        self.moveTo(h)

    def left(self):
        h = (self.hero.getH() + 90) % 360
        self.moveTo(h)

    def right(self):
        h = (self.hero.getH() + 270) % 360
        self.moveTo(h)

    def up(self):
        if self.spectatorMode:
            z = self.hero.getZ()
            self.hero.setZ(z+1)

    def down(self):
        if self.spectatorMode:
            z = self.hero.getZ()
            self.hero.setZ(z-1)

    def changeMode(self):
        self.spectatorMode = not self.spectatorMode
       


    def acceptEvents(self):
        builtins.base.accept(change_camera_key, self.changeCamera)
        builtins.base.accept(turn_left_key, self.turnLeft)
        builtins.base.accept(turn_left_key+"-repeat", self.turnLeft)
        builtins.base.accept(turn_right_key, self.turnRight)
        builtins.base.accept(turn_right_key+"-repeat", self.turnRight)

        builtins.base.accept(move_forward_key, self.forward)
        builtins.base.accept(move_forward_key+"-repeat", self.forward)

        builtins.base.accept(move_backward_key, self.backward)
        builtins.base.accept(move_backward_key+"-repeat", self.backward)

        builtins.base.accept(move_left_key, self.left)
        builtins.base.accept(move_left_key+"-repeat", self.left)

        builtins.base.accept(move_right_key, self.right)
        builtins.base.accept(move_right_key+"-repeat", self.right)

        builtins.base.accept(change_mode_key, self.changeMode)
        builtins.base.accept(move_up_key, self.up)
        builtins.base.accept(move_down_key, self.down)

        

 
change_camera_key = "c"
turn_left_key = "arrow_left"
turn_right_key = "arrow_right"
move_forward_key = "w"
move_backward_key = "s"
move_left_key = "a"
move_right_key = "d"
change_mode_key = "z"
move_up_key = "shift"
move_down_key = "control"