import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft.create()

def fireTrap(entityId):
    loc = mc.entity.getTilePos(entityId)
    x,y,z = loc.x,loc.y,loc.z

    mc.setBlock(x,y,z, block.Block(50))
