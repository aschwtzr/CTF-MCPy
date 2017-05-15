import mcpi.minecraft as minecraft
import whitelist
import trapQueen
import time
from multiprocessing import Pool

mc = minecraft.Minecraft.create()
threads = []

# whitelist returns two Lists with player objects
blue, red = whitelist.getBlueRed(mc)
print(blue)
print(red)

def updateLocation(playerList):
    for player in playerList:
        player.position = mc.entity.getTilePos(player.entityId)

class Trap(object):
    def __init__(self,x,y,z,name):
        self.x = x
        self.y = y
        self.z = z
        self.name = name

#put both the traps into lists
redTraps = [Trap(15,60,372,"ratInCage"),
            Trap(26,60,372,"fireTrap"),
            Trap(37,60,372,"Ssanso")]

blueTraps = [Trap(15,60,380,"earthSwallow"),
             Trap(26,60,380,"ahmedoo"),
             Trap(37,60,380, "lavaPool")]

print(redTraps)
print(blueTraps)

if __name__ == '__main__':
    pool = Pool(processes=3)
    print("success")

while True:
    start = time.time()
    updateLocation(blue)
    updateLocation(red)
    for player in blue:
        traps = pool.map_async(player.checkTraps, redTraps)
    for player in red:
        traps = pool.map_async(player.checkTraps, blueTraps)
    end = time.time()
    print(end - start)
