import mcpi.minecraft as minecraft
import mcpi.block as block
import time

mc = minecraft.Minecraft.create()

#ezra = mc.getPlayerEntityId("emeran1")

#location = mc.player.getPos()

x, y, z = 5212, 76, 247 #location.x + 2, location.y, location.z + 2

def ratInACage(entityId):

    location = mc.entity.getTilePos(entityId)

    x,y,z = location.x,location.y,location.z

    __buildStructure(x,y,z)

    time.sleep(1)
    mc.entity.setTilePos(entityId,x+5,y+2,z+5)
    time.sleep(6)
    mc.setBlocks(x + 1, y + 1, z, x + 1, y + 5, z + 6,1)
    time.sleep(1)
    mc.setBlocks(x + 2, y + 1, z, x + 2, y + 5, z + 6,1)
    time.sleep(1)
    mc.setBlocks(x + 3, y + 1, z, x + 3, y + 5, z + 6,1)
    time.sleep(1)
    mc.setBlocks(x + 4, y + 1, z, x + 4, y + 5, z + 6,1)
    time.sleep(4)
    print("clear")

    mc.setBlocks(x+5,y+6,z+1,x+5,y+6,z+5,0)



def __buildStructure(x,y,z):
    x,y,z = x,y,z
    mc.setBlocks(x,y - 1,z,x + 6, y + 6, z + 6, 1)
    mc.setBlocks(x + 1, y + 1, z + 1, x + 5, y + 6, z + 5,0)
    mc.setBlocks(x + 1, y + 6, z + 1, x + 5, y + 6, z + 5,20)
    mc.setBlocks(x, y + 7, z, x + 6, y + 7, z + 6, 11)
