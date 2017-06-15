import mcpi.minecraft as minecraft
import mcpi.block as block
import time

mc = minecraft.Minecraft.create()




def StuckintheBasement(entityid):
    pos = mc.entity.getTilePos(entityid)
    x = pos.x
    y = pos.y
    z = pos.z

    mc.setBlocks(x-3,y-63,z-3,x+3,y-57,z+3,0)
    mc.setBlocks(x-6,y-66,z-6,x+6,y-54,z+6,49)
    mc.entity.setPos(entityid,x,y-60,z)
