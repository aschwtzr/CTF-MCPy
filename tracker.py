import mcpi.minecraft as minecraft
import mcpi.block as block
import whitelist
import time
import mcpi.vec3 as vec3
import trapQueen
from threading import Thread

mc = minecraft.Minecraft.create()
threads = []
blue, red = whitelist.getBlueRed()
# blue = {
# "Albertthe3": vec3.Vec3(1,2,3),"Albertthe3": vec3.Vec3(1,2,3),
# "Albertthe3": vec3.Vec3(1,2,3),"Albertthe3": vec3.Vec3(1,2,3),"Albertthe3": vec3.Vec3(1,2,3),"Mirna1000": vec3.Vec3(1,2,3),
# "Albertthe3": vec3.Vec3(1,2,3),"Albertthe3": vec3.Vec3(1,2,3)
# }
#
# red = {
# "Albertthe3": vec3.Vec3(1,2,3),"Albertthe3": vec3.Vec3(1,2,3),
# "Albertthe3": vec3.Vec3(1,2,3),"Albertthe3": vec3.Vec3(1,2,3),"Albertthe3": vec3.Vec3(1,2,3),"Mirna1000": vec3.Vec3(1,2,3),
# "Albertthe3": vec3.Vec3(1,2,3),"Albertthe3": vec3.Vec3(1,2,3)
# }

def updateLocation(playerDict):
    for player in playerDict:
        playerDict[player] = mc.entity.getTilePos(player)

class trap(object):
    def __init__(self,x,y,z,name):
        self.x = x
        self.y = y
        self.z = z
        self.name = name

#put both the traps into lists
#red team
redTraps = [trap(15,60,372,"ratInCage"),
            trap(26,60,372,"fireTrap"),
            trap(37,60,372,"Ssanso")]

#blue team
blueTraps = [trap(15,60,380,"earthSwallow"),
             trap(26,60,380,"ahmedoo"),
             trap(37,60,380, "lavaPool")]

class teamThread(Thread):
    def __init__(self,team,traps):
        Thread.__init__(self)
        self.team = team
        self.traps = traps

    def run(self):
        for player in self.team:
            thread = trapThread(player, self.team[player], self.traps)
            #print("p thread")
            thread.start()

class trapThread(Thread):
    def __init__(self,player, position, traps):
        Thread.__init__(self)
        self.player = player
        self.position = position
        self.traps = traps

    def run(self):
        checkTraps(self.player, self.position, self.traps)
        threads.append(self)

def checkTraps(player,position,traps):
    for trap in traps:
        checkGeoFence(player, position, trap)

def checkGeoFence(entityId,vec3,trap):
    if trap.z < vec3.z < trap.z + 3:
        if trap.x < vec3.x < trap.x + 3:
            if trap.y < vec3.y < trap.y + 3:
                print(trap.name, True)
                trapQueen.activateTrap(trap.name,entityId)

while True:
    start = time.time()
    updateLocation(blue)
    updateLocation(red)
    blueThread = teamThread(blue, blueTraps)
    blueThread.start()
    redThread = teamThread(red, redTraps)
    redThread.start()
    #checkTrapsOld(blue, blueTraps)
    #checkTrapsOld(red, redTraps)
    for t in threads:
        t.join()
    end = time.time()
    print(end - start)
