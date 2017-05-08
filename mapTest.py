import mcpi.minecraft as minecraft
import mcpi.vec3 as vec3
import time

blue = {
"SuhaibThePro": vec3.Vec3(1,2,3),"Mirna1000": vec3.Vec3(1,2,3),
"Ahmidoo": vec3.Vec3(1,2,3),"Albertthe3": vec3.Vec3(1,2,3),"SuhaibThePro": vec3.Vec3(1,2,3),"Mirna1000": vec3.Vec3(1,2,3),
"Ahmidoo": vec3.Vec3(1,2,3),"Albertthe3": vec3.Vec3(1,2,3)
}

red = {
"SuhaibThePro": vec3.Vec3(1,2,3),"Mirna1000": vec3.Vec3(1,2,3),
"Ahmidoo": vec3.Vec3(1,2,3),"Albertthe3": vec3.Vec3(1,2,3),"SuhaibThePro": vec3.Vec3(1,2,3),"Mirna1000": vec3.Vec3(1,2,3),
"Ahmidoo": vec3.Vec3(1,2,3),"Albertthe3": vec3.Vec3(1,2,3)
}

class trap(object):
    def __init__(self,x,y,z,name):
        self.x = x
        self.y = y
        self.z = z
        self.name = name

#put both the traps into lists
#red team
redTraps = [trap(15,60,372,"ratInCage"),
            trap(26,60,372,"fireTrap"),
            trap(37,60,372,"Ssanso")]

#blue team
blueTraps = [trap(15,60,380,"earthSwallow"),
             trap(26,60,380,"ahmedoo"),
             trap(37,60,380, "lavaPool")]

#function takes a team List and trap List
def checkTraps(team,traps):
    for member in team:
        for trap in traps:
            checkGeoFence(member, team[member], trap)

def checkGeoFence(entityId,vec3,trap):
    if trap.y < vec3.y < trap.y + 3:
        if trap.x < vec3.x < trap.x + 3:
            if trap.z < vec3.z < trap.z + 3:
                print(trap.name, True)
                trapQueen.activateTrap(trap.name,entityId)
    else:
        print(trap.name, False)

while True:
    start = time.time()
    checkTraps(blue, blueTraps)
    checkTraps(red, redTraps)
    end = time.time()
    print(end - start)
