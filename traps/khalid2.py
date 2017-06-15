import mcpi.minecraft as minecraft
import mcpi.block as block
import time
mc = minecraft.Minecraft.create()
#mc = minecraft.Minecraft.create("172.16.10.58", 4711)

def Khalid2(entityId):

    loc = mc.entity.getTilePos(entityId)
    x,y,z = loc.x,loc.y,loc.z

    newposition= (x+10,y+25,z+10)

    mc.player.setPos(newposition[0],newposition[1],newposition[2])

    mc.setBlocks(newposition[0] + 4, newposition[1] -10, newposition[2] -4, newposition[0] -4, newposition[1] + 10, newposition[2] + 4,49)

    np = (x+10,y+25,z+10)

    mc.setBlocks(np[0] + 1, np[1] -9, np[2] - 1, np[0] - 1, np[1] +9, np[2] +1, 0)

    mc.setBlocks(np[0] + 2, np[1], np[2] -2, np[0]-2,np[1] - 8,np[2]+2,49)
