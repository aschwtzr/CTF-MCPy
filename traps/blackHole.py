#Mohamed Amal
import mcpi.minecraft as minecraft
import time
import mcpi.block as block
mc = minecraft.Minecraft.create()

def blackHole(entityId):
    loc = mc.entity.getTilePos(entityId)
    x,y,z = loc.x,loc.y,loc.z
    mc.setBlocks(x - 2,y -1,z - 2,x + 2,y + 3,z + 2, 49)
    mc.setBlocks(x - 1,y,z - 1,x + 1,y + 2, z + 1, 0)
    time.sleep(3)
    mc.setBlocks(x - 1,y,z - 1,x + 1,y,z + 1, 119)
