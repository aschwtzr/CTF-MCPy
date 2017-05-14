import trapQueen
class Player(object):

    def __init__(self, entityId, position):
        self.position = position
        self.entityId = entityId

    def checkTraps(self, traps):
        for trap in traps:
            self.checkGeoFence(trap)

    def checkGeoFence(trap):
        pos = self.position
        if trap.z < pos.z < trap.z + 3:
            if trap.x < pos.x < trap.x + 3:
                if trap.y < pos.y < trap.y + 3:
                    print(trap.name, True)
                    trapQueen.activateTrap(trap.name, self.entityId)