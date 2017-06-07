
def earthSwallow(entityId):
    from mcpi.minecraft import Minecraft
    mc = Minecraft.create()

    x, y, z = mc.entity.getTilePos(entityId)

    mc.setBlocks(x - 2, y, z - 2, x + 2, y - 20, z + 2, 0)
