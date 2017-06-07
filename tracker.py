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
redTraps = [Trap(84,649,-167,"khalidTrap1"),
            Trap(50,69,-164,"khalid2"),
            Trap(-14,69,146,"sufferInSand")]

blueTraps = [Trap(61,68,-169,"earthSwallow"),
             Trap(51,76,-156,"lavaPool"),
             Trap(54,76,-162, "nadia")]

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
