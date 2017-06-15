import mcpi.minecraft as minecraft
import mcpi.block as block
import time
mc = minecraft.Minecraft.create()

def Khalid1(entityId):

    loc = mc.entity.getTilePos(entityId)
    x,y,z = loc.x,loc.y,loc.z

    air = 0

    npx = x - 5
    npy = y + 10
    npz = z + 5
    mc.player.setPos(npx,npy,npz)
    mc.postToChat("Whoops.  Bad idea!")
    mc.setBlocks(npx - 6, npy - 2, npz + 6, npx + 6, npy + 7, npz - 6, 49)
    mc.setBlocks(npx - 5, npy - 1, npz + 5, npx + 5, npy + 6, npz - 5, air)
    mc.setBlocks(npx - 5, npy + 7, npz + 5, npx + 5, npy + 7, npz - 5, 20)
    mc.setBlocks(npx - 5, npy + 5, npz + 5, npx + 5, npy + 5, npz - 5, 20)
    mc.setBlocks(npx - 5, npy + 6, npz + 5, npx + 5, npy + 6, npz - 5, 10)
    time.sleep(1)
    mc.setBlocks(npx - 4, npy - 2, npz + 4, npx + 4, npy + 7, npz - 4, 49)
    mc.setBlocks(npx - 3, npy - 1, npz + 3, npx + 3, npy + 6, npz - 3, air)
    mc.setBlocks(npx - 3, npy + 7, npz + 3, npx + 3, npy + 7, npz - 3, 20)
    mc.setBlocks(npx - 3, npy + 5, npz + 3, npx + 3, npy + 5, npz - 3, 20)
    mc.setBlocks(npx - 3, npy + 6, npz + 3, npx + 3, npy + 6, npz - 3, 10)
    time.sleep(1)
    mc.setBlocks(npx - 3, npy - 2, npz + 3, npx + 3, npy + 7, npz - 3, 49)
    mc.setBlocks(npx - 2, npy - 1, npz + 2, npx + 2, npy + 6, npz - 2, air)
    mc.setBlocks(npx - 2, npy + 7, npz + 2, npx + 2, npy + 7, npz - 2, 20)
    mc.setBlocks(npx - 2, npy + 5, npz + 2, npx + 2, npy + 5, npz - 2, 20)
    mc.setBlocks(npx - 2, npy + 6, npz + 2, npx + 2, npy + 6, npz - 2, 10)
    time.sleep(1)
    mc.setBlocks(npx - 2, npy - 2, npz + 2, npx + 2, npy + 7, npz - 2, 49)
    mc.setBlocks(npx - 1, npy - 1, npz + 1, npx + 1, npy + 6, npz - 1, air)
    mc.setBlocks(npx - 1, npy + 7, npz + 1, npx + 1, npy + 7, npz - 1, 20)
    mc.setBlocks(npx - 1, npy + 5, npz + 1, npx + 1, npy + 5, npz - 1, 20)
    mc.setBlocks(npx - 1, npy + 6, npz + 1, npx + 1, npy + 6, npz - 1, 10)
    time.sleep(1)


    mc.setBlocks(npx - 1, npy + 5, npz + 1, npx + 1, npy + 5, npz - 1, air)
