"""
Set up the game here.
Don't forget to update the trapQueen.py file and add the file for each trap in the traps folder!
"""

from time import sleep

class Trap(object):
    def __init__(self,x,y,z,name, minecraftInstance):
        self.x = x
        self.y = y
        self.z = z
        self.name = name
        mc = minecraftInstance

        sleep(1)
        mc.postToChat("TRAP " + self.name + " ACTIVATED!")

class Settings(object):
    def __init__ (self, minecraftInstance):
        self.blueNameStrings = ["IKNS1","IKNS2","IKNS3", "IKNS4","IKN5","IKNS6","Albertthe3"]
        self.redNameStrings = ["Bayan1","Bayan2","Bayan3", "Bayan4","Bayan5","Bayan6","Albertthe3"]

        mc = minecraftInstance

        self.redTraps = [Trap(84,69,-167,"khalidTrap1",mc),
                    Trap(50,69,-164,"khalid2",mc),
                    Trap(-14,69,146,"sufferInSand",mc)]

        self.blueTraps = [Trap(61,68,-169,"earthSwallow",mc),
                      Trap(51,76,-156,"lavaPool",mc),
                      Trap(54,76,-162, "nadia",mc)]
