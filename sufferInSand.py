#Mohamed Amal
import mcpi.minecraft as minecraft
import mcpi.block as block
import time
mc = minecraft.Minecraft.create()

def sufferInSand(entityId):
    loc = mc.entity.getTilePos(entityId)
    x,y,z = loc.x,loc.y,loc.z

    mc.setBlocks(x - 2, y, z - 2, x + 2, y + 5, z + 2, 49)
    mc.setBlocks(x - 1, y, z - 1, x + 1, y + 5, z + 1, 0)
    for i in range(15):
        mc.setBlocks(x - 1, y + 9,z - 1,x + 1, y + 10,z + 1, 12)
        time.sleep(1)
