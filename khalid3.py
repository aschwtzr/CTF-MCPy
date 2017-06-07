import mcpi.minecraft as minecraft
import mcpi.block as block
import time
mc = minecraft.Minecraft.create()
#mc = minecraft.Minecraft.create("172.16.10.58", 4711)

def Khalid3(entityId):

    loc = mc.entity.getTilePos(entityId)
    x,y,z = loc.x,loc.y,loc.z


    x2 = loc.x
    y2 = loc.y
    z2 = loc.z

    blockbelow = mc.getBlock(x,y-2,z)


    #platform


    y=y+25
    mc.setBlocks(x+6,y,z+6,x-6,y+8,z-6,49)
    mc.setBlocks(x+5,y+1,z+5,x-5,y+8,z-5,0)
    mc.setBlocks(x+6,y,z-1,x+6,y+2,z+1,0)

    #ladder:

    mc.setBlocks(x+8,y+3,z,x+8,y-25,z,49)
    mc.setBlocks(x+7,y+3,z-1,x+7,y-3,z+1,49)
    mc.setBlocks(x+7,y+3,z,x+7,y-25,z,0)

    mc.setBlocks(x+7,y+3,z,x+7,y-10,z,65,4)
    starty=loc.y
    mc.entity.setTilePos(entityId,x,loc.y+27,z)
