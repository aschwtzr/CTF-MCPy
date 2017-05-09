import mcpi.minecraft as minecraft
import mcpi.block as block
import whitelist
import time
import mcpi.vec3 as vec3
import trapQueen

mc = minecraft.Minecraft.create()

blue, red = whitelist.getBlueRed()

def updateLocation(playerDict):
    for player in playerDict:
        playerDict[player] = mc.entity.getTilePos(player)

class trap(object):
    def __init__(self,x,y,z,name):
        self.x = x
        self.y = y
        self.z = z
        self.name = name
        
#red team
ratInACage = trap(15,60,372,"ratInCage")
fireTrap = trap(26,60,372,"fireTrap")
Ssanso = trap(37,60,372,"Ssanso")

#blue team
earthSwallow = trap(15,60,380,"earthSwallow")
ahmedoo = trap(26,60,380,"ahmedoo")
lavaPool2 = trap(37,60,380, "lavaPool")

def checkGeoFence(entityId,vec3,trap):
    if trap.y < vec3.y < trap.y + 3:
        if trap.x < vec3.x < trap.x + 3:
            if trap.z < vec3.z < trap.z + 3:
                print(trap.name, True)
                trapQueen.activateTrap(trap.name,entityId)
    else:
        print(trap.name, False)

while True:
    start = time.time()
    updateLocation(blue)
    updateLocation(red)
    for entityId in blue:
        checkGeoFence(entityId,blue[entityId],ratInACage)
        checkGeoFence(entityId,blue[entityId],fireTrap)
        checkGeoFence(entityId,blue[entityId],Ssanso)

    for entityId in red:
        checkGeoFence(entityId,red[entityId],earthSwallow)
        checkGeoFence(entityId,red[entityId],ahmedoo)
        checkGeoFence(entityId,red[entityId],lavaPool2)
    end = time.time()
    print(end - start)
