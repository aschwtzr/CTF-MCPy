import mcpi.minecraft as minecraft
import mcpi.block as block
import time

mc = minecraft.Minecraft.create()

def anviltrap(entityId):
    #around head

    loc = mc.entity.getTilePos(entityId)
    x,y,z = loc.x,loc.y,loc.z

    mc.setBlock(x+2, y+1, z, 49)
    mc.setBlock(x+2, y+1, z+1, 49)
    mc.setBlock(x+2, y+1, z-1, 49)
    mc.setBlock(x-2, y+1, z, 49)
    mc.setBlock(x-2, y+1, z+1, 49)
    mc.setBlock(x-2, y+1, z-1, 49)
    mc.setBlock(x,y+1,z+2,49)
    mc.setBlock(x+1,y+1,z+2,49)
    mc.setBlock(x-1,y+1,z+2,49)
    mc.setBlock(x,y+1,z-2,49)
    mc.setBlock(x-1,y+1,z-2,49)
    mc.setBlock(x+1,y+1,z-2,49)

    #blocks above

    mc.setBlock(x+2, y+2, z, 49)
    mc.setBlock(x+2, y+2, z+1, 49)
    mc.setBlock(x+2, y+2, z-1, 49)
    mc.setBlock(x-2, y+2, z, 49)
    mc.setBlock(x-2, y+2, z+1, 49)
    mc.setBlock(x-2, y+2, z-1, 49)
    mc.setBlock(x,y+2,z+2,49)
    mc.setBlock(x+1,y+2,z+2,49)
    mc.setBlock(x-1,y+2,z+2,49)
    mc.setBlock(x,y+2,z-2,49)
    mc.setBlock(x-1,y+2,z-2,49)
    mc.setBlock(x+1,y+2,z-2,49)

    #around feet
    mc.setBlock(x+2, y, z, 49)
    mc.setBlock(x+2, y, z+1, 49)
    mc.setBlock(x+2, y, z-1, 49)
    mc.setBlock(x-2, y, z, 49)
    mc.setBlock(x-2, y, z+1, 49)
    mc.setBlock(x-2, y, z-1, 49)
    mc.setBlock(x,y,z+2,49)
    mc.setBlock(x+1,y,z+2,49)
    mc.setBlock(x-1,y,z+2,49)
    mc.setBlock(x,y,z-2,49)
    mc.setBlock(x-1,y,z-2,49)
    mc.setBlock(x+1,y,z-2,49)
    #anvil
    mc.setBlock(x,y+40,z+1,145)
    mc.setBlock(x+1,y+40,z+1,145)
    mc.setBlock(x-1,y+40,z+1,145)
    mc.setBlock(x,y+40,z,145)
    mc.setBlock(x+1,y+40,z,145)
    mc.setBlock(x-1,y+40,z,145)
    mc.setBlock(x,y+40,z-1,145)
    mc.setBlock(x+1,y+40,z-1,145)
    mc.setBlock(x-1,y+40,z-1,145)

    #second set of anvils
    mc.setBlock(x,y+41,z+1,145)
    mc.setBlock(x+1,y+41,z+1,145)
    mc.setBlock(x-1,y+41,z+1,145)
    mc.setBlock(x,y+41,z,145)
    mc.setBlock(x+1,y+41,z,145)
    mc.setBlock(x-1,y+41,z,145)
    mc.setBlock(x,y+41,z-1,145)
    mc.setBlock(x+1,y+41,z-1,145)
    mc.setBlock(x-1,y+41,z-1,145)
