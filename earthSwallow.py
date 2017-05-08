from mcpi.minecraft import Minecraft
import time
mc = Minecraft.create()

def earthSwallow(entityId):

    x = [-215, -216]
    y = [62]
    z = [3, 4]

    mc.setBlocks(x[0], y[0] - 10, z[0], x[len(x)-1], y[0], z[len(z)-1], 0)
    time.sleep(.3)
    mc.setBlocks(x[0], y[0] - 5, z[0], x[len(x)-1], y[0], z[len(z)-1], 1)
