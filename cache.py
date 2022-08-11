import random

def createCache(cacheSize):

    #[0,0,0,[0],0]       [0] = valid bit     [1] = tag     [2] = write-back    [3] = data        [4] = reference bit 

    cache = [[0,0,0,[0],0] for _ in range(cacheSize)]

    return cache


def searchCache(index,tag,cache,mapping, setIndex = None):

    #search on cache for corresponding line or set

    if mapping == 0:
        return cache[ int(index,2) ]

    elif mapping == 1 or mapping == 2:
        return cache[ int(setIndex,2) ]
    else :
        return



def  writeBlockOnCache(data,tag,index,cache,mapping,setIndex = None, lineIndex = None):

    if mapping == 0: #direct maping
        cache[ int(index,2) ][0] = 1         #valid bit
        cache[ int(index,2) ][1] = tag       #tag
        cache[ int(index,2) ][3] = data      #data

    elif mapping == 1 or mapping == 2 :   #associative 
        for i, line in enumerate( cache[ int( setIndex,2) ]) :
            cache[ int( setIndex,2 ) ][i][4] = 0     #set lines on the same set reference bit to 0

        cache[ int( setIndex,2) ][lineIndex][0] = 1     #valid bit
        cache[ int( setIndex,2) ][lineIndex][1] = tag   #tag
        cache[ int( setIndex,2) ][lineIndex][3] = data  #data
        cache[ int( setIndex,2) ][lineIndex][4] = 1     #set the last wrote line reference bit to 1
 
    else :   #Fully associative

        #index parameter is a int an indicate where the line is on cache

        #set other lines reference bit to 0
        for i, line in enumerate(cache) :
            cache[i][4] = 0
        
        cache[index][0] = 1
        cache[index][1] = tag
        cache[index][3] = data
        cache[index][4] = 1



#divide cache in sets of a given size 
def cacheChunker(cache, size):
    return [cache[pos:pos + size] for pos in range(0, len(cache), size)]

