import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft.create()

def lavaPool(entityId):
    loc = mc.entity.getTilePos(entityId)
    x,y,z = loc.x,loc.y,loc.z

    mc.setBlocks(x,y-1,z,x+3,y-2,z+3,10)
