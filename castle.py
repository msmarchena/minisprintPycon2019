import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft.create('mcst.dynu.net')
mc.postToChat("Welcome to my castillo")

#To clean the terrain
mc.setBlocks(0,0,0,200,200,200,block.AIR)

#The following example has been taken from learnlearn and can be found
# here https://learnlearn.uk/raspberrypi/2018/08/18/code-castle-minecraft-using-python/
# #First tower
# mc.setBlocks(x+0,0,0,x+10,15,10,block.STONE)
# for x in range (11):
#     for z in range(11):
#         if x % 2 == 0 and z % 2 == 0:
#             mc.setBlock(x,16,z,block.STONE)
# mc.setBlocks(1,15,1,9,16,9,block.AIR)
# mc.setBlocks(2,14,2,8,14,8,block.AIR)

#function to create a createTower
# def createTower(tx,ty,tz):
#     mc.setBlocks(tx+0,ty+0,tz+0,tx+10,ty+15,tz+10,block.STONE)
#     for x in range (11):
#         for z in range(11):
#             if x % 2 == 0 and z % 2 == 0:
#                 mc.setBlock(tx+x,ty+16,tz+z,block.STONE)
#     mc.setBlocks(tx+1,ty+15,tz+1,tx+9,ty+16,tz+9,block.AIR)
#     mc.setBlocks(tx+2,ty+14,tz+2,tx+8,ty+14,tz+8,block.AIR)
#     mc.setBlocks(tx+1,ty+1,tz+1,tx+6,ty+12,tz+6,block.AIR)

def createTower(tx,ty,tz,height):
    mc.setBlocks(tx+0,ty+0,tz+0,tx+10,ty+height,tz+10,block.STONE)
    for x in range (0,11):
        for z in range(0,11):
            if x % 2 == 0 and z % 2 == 0:
                mc.setBlock(tx+x,ty+height+1,tz+z,block.STONE)

    mc.setBlocks(tx+1,ty+height,tz+1,tx+9,ty+height+1,tz+9,block.AIR)
    mc.setBlocks(tx+2,ty+height-1,tz+2,tx+8,ty+height-1,tz+8,block.AIR)
    mc.setBlocks(tx+2,ty+0,tz+2,tx+8,ty+height-3,tz+8,block.AIR)    #hollow out the tower


def walls(x,y,z,length,plane,height):
    if plane == "x":
        mc.setBlocks(x,y,z,x+length,y+height,z+1,block.STONE)
        for i in range (length):
            if i % 2 == 0:
                mc.setBlock(x+i,y+height,z,block.AIR)
                mc.setBlock(x+i,y+height,z+1,block.AIR)
    if plane == "z":
        mc.setBlocks(x,y,z,x+1,y+height,z+length,block.STONE)
        for i in range (length):
            if i % 2 == 0:
                mc.setBlock(x,y+height,z+i,block.AIR)
                mc.setBlock(x+1,y+height,z+i,block.AIR)
                #mc.setBlock        # mc.setBlocks(x-2,y+9,z+1,x,y+10,z+2,block.AIR)
        # mc.setBlocks(x+40,y+9,z+1,(x+length)+3,y+10,z+2,block.AIR)
        # #mc.setBlocks(x-2,y+9,z+1,x+length+1,y+10,z+2,block.AIR)(x,y+height,z+i,block.AIR)


def pasarela(x,y,z,length,plane):
    if plane == "x":
        # mc.setBlocks(x-2,y+9,z+1,x,y+10,z+2,block.AIR)
        # mc.setBlocks(x+40,y+9,z+1,(x+length)+3,y+10,z+2,block.AIR)
        # #mc.setBlocks(x-2,y+9,z+1,x+length+1,y+10,z+2,block.AIR)
        for i in range (length):
            mc.setBlock(x+1+i,y+8,z+1,block.STONE)
            mc.setBlock(x+1+i,y+8,z+2,block.STONE)

    if plane == "z":
        #mc.setBlocks(x+1,y+9,z-2,x+2,y+10,z+length+1,block.AIR)
        for i in range (length):
            mc.setBlock(x+1,y+8,z+1+i,block.STONE)
            mc.setBlock(x+2,y+8,z+1+i,block.STONE)
        #mc.setBlocks(x1,y1,z1,x1+1,y1+8,z1+length,block.STONE)
        #mc.setBlocks(x1+1,y1,z1+1,x1,y1+7,z1+length,block.AIR)


def window(x,y,z,height,plane):
    if plane == "x":
        mc.setBlocks(x+3,y+height,z,x+3,y+height-2,z+2,block.AIR)
    if plane == "z":
        mc.setBlocks(x,y+height,z+3,x+2,y+height-2,z+3,block.AIR)

def door(x,y,z,length,plane,height):
    if plane == "x":
        mc.setBlocks(x,y,z,x+length,y+height,z+1,block.WOOD)
    if plane == "z":
        mc.setBlocks(x,y,z,x+2,y+height,z+length,block.WOOD)


#Djon
createTower(25,0,25,30)
window(25,0,25,25,"x")
window(25,0,33,25,"x")
window(25,0,29,25,"z")
window(33,0,29,25,"z")

createTower(0,0,0,15)
window(0,0,0,12,"x")
window(4,0,0,12,"x")
window(0,0,4,12,"z")
window(0,0,0,12,"z")
walls(10,0,5,40,"x",10)
door(20,0,5,20,"x",5)
pasarela(10,0,6,40,"x")

#Tower in same direcion
createTower(0,0,50,15)
window(0,0,58,12,"x")
window(4,0,58,12,"x")
window(0,0,50,12,"z")
window(0,0,54,12,"z")
walls(10,0,55,40,"x",10)
pasarela(10,0,52,40,"x")

createTower(50,0,0,15)
window(50,0,0,12,"x")
window(54,0,0,12,"x")
window(58,0,0,12,"z")
window(58,0,4,12,"z")
walls(5,0,10,40,"z",10)
pasarela(6,0,10,40,"z")

createTower(50,0,50,15)
window(50,0,58,12,"x")
window(54,0,58,12,"x")
window(58,0,50,12,"z")
window(58,0,54,12,"z")
walls(55,0,10,40,"z",10)
pasarela(52,0,10,40,"z")
