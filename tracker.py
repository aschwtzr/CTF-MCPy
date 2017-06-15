import mcpi.minecraft as minecraft
import whitelist
import time
from settings import Settings
from multiprocessing import Pool


mc = minecraft.Minecraft.create()

settings = Settings(mc)

#TODO: check if we need these threads
threads = []

# whitelist returns two Lists with player objects
blue, red = whitelist.getBlueRed(mc,settings)
print(blue)
print(red)

def updateLocation(playerList):
    for player in playerList:
        player.position = mc.entity.getTilePos(player.entityId)

if __name__ == '__main__':
    pool = Pool(processes=3)
    print("success")


while True:
    start = time.time()
    updateLocation(blue)
    updateLocation(red)
    for player in blue:
        traps = pool.map_async(player.checkTraps, settings.redTraps)
    for player in red:
        traps = pool.map_async(player.checkTraps, settings.blueTraps)
    end = time.time()
    print(end - start)
