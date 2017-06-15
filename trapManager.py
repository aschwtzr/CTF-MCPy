"""
Set up your traps in this file. To add your own traps drop the python file
in the traps subfolder and import them below. Don't forget to update
the switcher Dictionary as well!
"""
# import traps as traps

import traps.ratInCage as ratInCage
import traps.lavaPool as lavaPool
import traps.fire_trap as fire_trap
import traps.Ssanso as Ssanso
import traps.ahmedoo as ahmedoo
import traps.earthSwallow as earthSwallow
import traps.sufferInSand as sufferInSand
import traps.nadia as nadia
import traps.khalidTrap1 as khalidTrap1
import traps.khalid2 as khalid2
import traps.khalid3 as khalid3
import traps.blackHole as blackHole
import traps.anvilTrap as anvilTrap
import traps.tntTrap as tntTrap

def activateTrap(trapName, entityId):
    switcher = {
        "lavaPool": lavaPool.lavaPool,
        "ratInCage": ratInCage.ratInACage,
        "fireTrap": fire_trap.fireTrap,
        "Ssanso": Ssanso.void,
        "ahmedoo": ahmedoo.anvilTrap,
        "earthSwallow": earthSwallow.earthSwallow,
        "sufferInSand": sufferInSand.sufferInSand,
        "nadia": nadia.StuckintheBasement,
        "khalidTrap1": khalidTrap1.Khalid1,
        "khalid2": khalid2.Khalid2,
        "khalid3": khalid3.Khalid3,
        "anvilTrap": anvilTrap.anviltrap,
        "tntTrap": tntTrap.tntTrap
        }

    switcher[trapName](entityId)
