from player import Player
from time import sleep

# write in the username for each player here, divided into teams
#blueStrings = ["IKNS1","IKNS2","IKNS3", "IKNS4","IKN5","IKNS6","Albertthe3"]
#redStrings = ["Bayan1","Bayan2","Bayan3", "Bayan4","Bayan5","Bayan6","Albertthe3"]

#function takes a minecraft instance
def getBlueRed(minecraftInstance, settings):
    print("building player objects")
    mc = minecraftInstance
    settings = settings
    blue = []
    red = []

    for player in settings.blueNameStrings:
        try:
            entityId = mc.getPlayerEntityId(player)
        except:
            continue
        else:
            position = mc.entity.getTilePos(entityId)
            sleep(1)
            mc.postToChat("BLUE PLAYER " + player + " HAS ENTERED THE GAME")
            blue.append(Player(entityId, position))

    for player in settings.redNameStrings:
        try:
            entityId = mc.getPlayerEntityId(player)
        except:
            continue
        else:
            position = mc.entity.getTilePos(entityId)
            mc.postToChat("RED PLAYER " + player + " HAS ENTERED THE GAME")
            red.append(Player(entityId, position))

    return blue, red
