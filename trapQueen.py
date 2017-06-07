import ratInCage
import lavaPool
import fire_trap
import Ssanso
import ahmedoo
import earthSwallow
import sufferInSand
import nadia
import khalidTrap1
import khalid2
import khalid3
import blackHole
import anvilTrap
import tntTrap

def activateTrap(trapName, entityId):
    switcher = {
        "lavaPool":lavaPool.lavaPool,
        "ratInCage":ratInCage.ratInACage,
        "fireTrap":fire_trap.fireTrap,
        "Ssanso":Ssanso.void,
        "ahmedoo":ahmedoo.anvilTrap,
        "earthSwallow":earthSwallow.earthSwallow,
        "sufferInSand":sufferInSand.sufferInSand,
        "nadia":nadia.StuckintheBasement,
        "khalidTrap1":khalidTrap1.Khalid1,
        "khalid2":khalid2.Khalid2,
        "khalid3":khalid3.Khalid3,
        "anvilTrap":anvilTrap.anviltrap,
        "tntTrap":tntTrap.tntTrap
        }

    switcher[trapName](entityId)
