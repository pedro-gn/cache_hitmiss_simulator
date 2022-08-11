import random


def createRam():
    ram = [0] * (2 **16)

    for i,x in enumerate(ram):
        ram[i] = random.randint(1,200000)
    return ram


def writeRam(cacheLine,index,ram,setIndex = None):
    if setIndex is None :
        blockStartIndex = int( (cacheLine[1]  + index), 2 )    #blockStart = tag + index      blockEnd = blockStart + blockSize
    
    else:
        blockStartIndex = int( (cacheLine[1]  + setIndex), 2 )  #blockStart = tag + setIndex


    for data in cacheLine[3]:
        ram[blockStartIndex] = data
        blockStartIndex += 1
    

def searchRam(index,tag,blockSize,ram,setIndex = None):

    if setIndex is None :
        blockStartIndex = int( (tag  + index), 2 ) 
    
    else:
        blockStartIndex = int( (tag  + setIndex), 2 )

    data = []
    for i in range(blockSize):
        data.append( ram[blockStartIndex] )
        blockStartIndex +=1
    return data