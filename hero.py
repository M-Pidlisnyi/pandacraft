from direct.task.Task import Task
from panda3d.core import WindowProperties
class Hero:
    def __init__(self, pos, land):
        self.land = land
        self.cameraOn = True
        self.spectatorMode = True
        self.hero = loader.loadModel("smiley")

        self.hero.setColor(1, 0.5, 0, 1)
        self.hero.setScale(0.3)
        self.hero.setPos(pos)
        
        self.hero.reparentTo(render)

        self.cameraBind()

        self.acceptEvents()

    def cameraBind(self):
        base.disableMouse()
        base.camera.reparentTo(self.hero)
        base.camera.setPos(0,0,1.5)
        base.camera.setH(180)

        self.cameraOn = True

    def cameraUnbind(self):
        base.enableMouse()
        base.camera.reparentTo(render)
        
        pos = self.hero.getPos()
        base.mouseInterfaceNode.setPos(-pos[0], -pos[1], -pos[2]-1)

        self.cameraOn = False
        
    def changeCamera(self):
        if self.cameraOn:
            self.cameraUnbind()
        else:
            self.cameraBind()
    
    # -----------------методи повороту камери-------------------
    def turnLeft(self):
        # angle = self.hero.getH()
        # angle += 5
        # self.hero.setH(angle)
        self.hero.setH((self.hero.getH() + 5))

    def turnRight(self):
        self.hero.setH((self.hero.getH() - 5))
    
    def turnUp(self):
        self.hero.setP((self.hero.getP() + 5))

    def turnDown(self):
        self.hero.setP((self.hero.getP() - 5))
    #-----------



    def just_move(self, angle):
        pos = self.lookAt(angle)
        self.hero.setPos(pos)

    def try_move(self, angle):
        pos = self.lookAt(angle)
        if self.land.isEmpty(pos):
            pos = self.land.findHighestEmpty(pos)
            self.hero.setPos(pos)
        else:
            pos = pos[0], pos[1], pos[2]+1
            if self.land.isEmpty(pos):
                self.hero.setPos(pos)

    def move_to(self, angle):
        if self.spectatorMode:
            self.just_move(angle)
        else:
            self.try_move(angle)


    def changeMode(self):
        self.spectatorMode = not self.spectatorMode


    def lookAt(self, angle):
        x = round(self.hero.getX())
        y = round(self.hero.getY())
        z = round(self.hero.getZ())

        dx, dy = self.checkDir(angle)

        return (x+dx, y+dy, z)

    def checkDir(self, angle):
        if angle >= 0 and angle <= 20:
            return (0,-1)
        elif angle <= 65:
            return (+1,-1)
        elif angle <=  110:
            return (+1,0)
        elif angle <= 155:
            return (+1,+1)
        elif angle <= 200:
            return (0, +1)
        elif angle <= 245:
            return (-1,+1)
        elif angle <= 290:
            return (-1,0)
        elif angle <= 335:
            return (-1,-1)
        else:
            return (0,-1)

        

    def forward(self):
        angle = self.hero.getH() % 360
        self.move_to(angle)

    def backward(self):
        angle = (self.hero.getH()+180) % 360
        self.move_to(angle)

    def left(self):
        angle = (self.hero.getH()+90) % 360
        self.move_to(angle)

    def right(self):
        angle = (self.hero.getH()+270) % 360
        self.move_to(angle)

    def up(self):
        if self.spectatorMode:
            self.hero.setZ(self.hero.getZ()+1)

    
    def down(self):
        if self.spectatorMode:
            self.hero.setZ(self.hero.getZ()-1)
    
    def build(self):
        angle = self.hero.getH() % 360
        pos = self.lookAt(angle)
        self.land.addBlock(pos)
    
    def destroy(self):
        angle = self.hero.getH() % 360
        pos = self.lookAt(angle)
        self.land.removeBlock(pos)

    
    
    
    def acceptEvents(self):
        base.accept(change_mode_key, self.changeMode)
        base.accept(change_camera_key, self.changeCamera)

        base.accept(turn_left_key, self.turnLeft)
        base.accept(turn_left_key+"-repeat", self.turnLeft)

        base.accept(turn_right_key, self.turnRight)
        base.accept(turn_right_key+"-repeat", self.turnRight)

        base.accept(turn_up_key, self.turnUp)
        base.accept(turn_up_key+"-repeat", self.turnUp)

        base.accept(turn_down_key, self.turnDown)
        base.accept(turn_down_key+"-repeat", self.turnDown)

        base.accept(forward_key, self.forward)
        base.accept(forward_key+"-repeat", self.forward)

        base.accept(backward_key, self.backward)
        base.accept(backward_key+"-repeat", self.backward)

        base.accept(left_key, self.left)
        base.accept(left_key+"-repeat", self.left)

        base.accept(right_key, self.right)
        base.accept(right_key+"-repeat", self.right)

        base.accept(up_key, self.up)
        base.accept(up_key+"-repeat", self.up)

        base.accept(down_key, self.down)
        base.accept(down_key+"-repeat", self.down)

        base.accept(add_block_key, self.build)
        base.accept(remove_block_key, self.destroy)

        base.accept(save_key, self.land.saveMapToBin)
        base.accept(load_key, self.land.loadMapFromBin)

    def followMouse(self, task):
        if base.mouseWatcherNode.hasMouse():
            mpos = base.mouseWatcherNode.getMouse()

            self.hero.setH(trim(mpos.getX())*-180)
            self.hero.setP(trim(mpos.getY(), mn=-0.5, mx=0.5)*-180)
        
            props = base.win.getProperties()
            mprops = base.win.getPointer(0)

            new_props = WindowProperties()
            new_props.setCursorHidden(True)
            base.win.requestProperties(new_props)

            if mpos.getX() >= 0.99:
                base.win.movePointer(0, 5, int(mprops.getY()))
            
            if mpos.getX() <= -0.99:
                base.win.movePointer(0, props.getXSize()-5, int(mprops.getY()))




        
        return Task.cont

def trim(i, mn=-1, mx=1):
    return min( max(i, mn) , mx)




change_camera_key = "c"
change_mode_key = "z"


turn_left_key = "arrow_left"
turn_right_key = "arrow_right"
turn_up_key = "arrow_up"
turn_down_key = "arrow_down"

forward_key = "w"
backward_key = "s"
left_key = "a"
right_key = "d"

up_key = "r"
down_key = "f"

add_block_key = "mouse3"
remove_block_key = "mouse1"

save_key = "f5"
load_key = "f9"