import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft.create()

parcelLength = 3
parcelWidth = 3
x,y,z = 7,100,364

mc.player.setTilePos(x,y+8,z)

spacing = 8

rows = 4
columns = 3

startZ = z
startX = x

parcelCoordinates = []

def clearTestZone():
    xLength = rows * parcelLength + spacing * (rows + 2)
    zWidth = columns * parcelWidth + spacing * (columns + 2)

    mc.setBlocks(x,y,z,x+xLength,y+50,z+zWidth,0)
    mc.setBlocks(x,y-5,z,x+xLength,y-1,z+zWidth,1)
    #return xLength, zWidth

clearTestZone()

z += spacing

for row in range(rows):
    for column in range(columns):
        #add padding to x
        x += spacing
        mc.setBlocks(x,y-5,z,x+parcelLength,y,z+parcelWidth,1)
        parcelCoordinates.append([x,y,z])
        #add parcelLength offset to x
        x += parcelLength
    z+= spacing
    x = startX

print(parcelCoordinates)
