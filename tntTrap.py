import mcpi.minecraft as minecraft
import mcpi.block as block
import time
import math

mc = minecraft.Minecraft.create()

def tntTrap(entityId):
    #floor
    mc.setBlocks(35,152,356,39,152,360,46)
    #right wall
    mc.setBlocks(35,152,356,39,156,356,46)
    #left wall
    mc.setBlocks(35,152,356,35,156,360,46)
    #back wall
    mc.setBlocks(39,152,356,39,156,360,46)
    #front wall
    mc.setBlocks(36,152,361,38,156,361,46)
