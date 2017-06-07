from player import Player

# write in the username for each player here, divided into teams
blueStrings = ["IKNS1","IKNS2","IKNS3", "IKNS4","IKN5","IKNS6","Albertthe3"]
redStrings = ["Bayan1","Bayan2","Bayan3", "Bayan4","Bayan5","Bayan6","Albertthe3"]

#function takes a minecraft instance
def getBlueRed(minecraftInstance):
    print("building player objects")
    mc = minecraftInstance
    blue = []
    red = []

    for player in blueStrings:
        try:
            entityId = mc.getPlayerEntityId(player)
        except:
            continue
        else:
            position = mc.entity.getTilePos(entityId)
            blue.append(Player(entityId, position))

    for player in redStrings:
        try:
            entityId = mc.getPlayerEntityId(player)
        except:
            continue
        else:
            position = mc.entity.getTilePos(entityId)
            red.append(Player(entityId, position))

    return blue, red
