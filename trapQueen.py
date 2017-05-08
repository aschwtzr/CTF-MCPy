import ratInCage
import lavaPool
import fire_trap
import Ssanso
import ahmedoo
import earthSwallow

def activateTrap(trapName, entityId):
    switcher = {
        "lavaPool":lavaPool.lavaPool,
        "ratInCage":ratInCage.ratInACage,
        "fireTrap":fire_trap.fireTrap,
        "Ssanso":Ssanso.void,
        "ahmedoo":ahmedoo.anvilTrap,
        "earthSwallow":earthSwallow.earthSwallow
        }
        
    switcher[trapName](entityId)
