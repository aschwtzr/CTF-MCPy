import mcpi.minecraft as minecraft
import mcpi.block as block
import time
import math

mc = minecraft.Minecraft.create()

def anvilTrap(entityId):
    pos = mc.entity.getTilePos(entityId)
    x = pos.x
    y = pos.y + 15
    z = pos.z


    mc.setBlocks(x + 1, y + 1,z - 1, x + 1, y + 1, z + 2, 49)
    mc.setBlocks(x - 1, y + 1,z - 1, x + 1, y + 1, z + 2, 49)
    mc.setBlocks(x, y + 1,z - 1, 49)
    mc.setBlocks(x, y + 1,z + 1, 49)
    mc.setBlock(x, y + 20, z)
