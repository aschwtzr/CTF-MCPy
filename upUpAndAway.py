def upUpAndAway(entityId):

    from mcpi.minecraft import Minecraft
    mc = Minecraft.create()

    x, y, z = mc.entity.getTilePos(entityId)

    mc.entity.setTilePos(entityId, x, y + 20, z)
    mc.setBlocks(x - 2, y + 28, z - 2, x + 2, y + 28, z + 2, 1)

    
