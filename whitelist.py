from player import Player

# write in the username for each player here, divided into teams
blueStrings = ["Albertthe3","Ssanso","emeran1"]
redStrings = ["emeran1","_Biohazard_","SuhaibThePro","Ahmidoo","Albertthe3"]

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
