import mcpi.minecraft as minecraft

mc = minecraft.Minecraft.create()
blueStrings = ["SuhaibThePro","Mirna1000","Ahmidoo","Albertthe3"]
redStrings = ["Albertthe3","FIRE_DRAGON100","Ssanso"]

def getBlueRed():
    blue = {}
    red = {}

    for player in blueStrings:
        try:
            entityId = mc.getPlayerEntityId(player)
            blue[entityId] = mc.entity.getTilePos(entityId)
        except:
            continue

    for player in redStrings:
        try:
            entityId = mc.getPlayerEntityId(player)
            red[entityId] = mc.entity.getTilePos(entityId)
        except:
            continue
    print(blue)
    print(red)
    return blue, red
