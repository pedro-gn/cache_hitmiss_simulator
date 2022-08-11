from operator import index
from re import I
from cache import *
from Decoders import *
from ram import *

trace1 = open("traces/trace3.txt","r")
trace1 = trace1.readlines()


#maping 0-directly   1-2associative    2-4associative    3-fullyassociative



def processor(mapping,cacheSize,blockSize,trace):
    cacheHit = 0
    cacheMiss = 0
    cache = createCache(cacheSize)
    ram = createRam()
    iterates = 0

    if mapping == 0 : #direct mapping
        for access in trace:
            iterates += 1
            blockOffset,index,tag,op = DMDecoder(access,blockSize,cacheSize)
            cacheLine = searchCache(index,tag,cache,mapping)

            if cacheLine[0] == 1 and cacheLine[1] == tag :       #cache hit
                cacheHit += 1
            else:                                                #cache miss
                cacheMiss += 1
                if cacheLine[2] == 1:  #write-back
                    writeRam(cacheLine,index,ram)
                
                data = searchRam(index,tag,blockSize,ram) #get block on ram
                writeBlockOnCache(data,tag,index,cache,mapping) #load it on cache
            


    elif mapping == 1 : #2 ways associative
        cache = cacheChunker(cache,2) #divide cache in sets of 2
        for access in trace:
            iterates += 1
            blockOffset,setIndex,tag,op,index = ADecoder(access,blockSize,cacheSize,2)
            cacheSet = searchCache(index,tag,cache,mapping,setIndex) #get the corresponding set in cache 

            hitLine = None # if == None the line is not on the cache set and need to search in ram for it

            for line in cacheSet : 
                if line[1] == tag and line[0] == 1 : #cacheHit
                    cacheHit += 1
                    hitLine = line


            if hitLine == None : #cacheMiss
                cacheMiss += 1
                subLine = None
                lineIndex = None
                for i,line in enumerate(cacheSet) : #find first line with reference bit = 0
                    if line[4] == 0 :
                        subLine = line
                        lineIndex = i
                        break
                if subLine[2] == 1 : #write-back
                    writeRam(subLine,index,ram,setIndex)

                data = searchRam(index,tag,blockSize,ram,setIndex)
                writeBlockOnCache(data,tag,index,cache,mapping,setIndex,lineIndex)





    elif mapping == 2 : #4 ways associative
        cache = cacheChunker(cache,4) #divide cache in sets of 4
        for access in trace:
            iterates += 1
            blockOffset,setIndex,tag,op,index = ADecoder(access,blockSize,cacheSize,4)
            cacheSet = searchCache(index,tag,cache,mapping,setIndex) #get the corresponding set in cache 

            hitLine = None # if == None the line is not on the cache set and need to search in ram for it

            for line in cacheSet : 
                if line[1] == tag and line[0] == 1 : #cacheHit
                    cacheHit += 1
                    hitLine = line


            if hitLine == None : #cacheMiss
                cacheMiss += 1
                subLine = None
                lineIndex = None
                for i, line in enumerate(cacheSet) : #find first line with reference bit = 0
                    if line[4] == 0 :
                        subLine = line
                        lineIndex = i
                        break
                if subLine[2] == 1 : #write-back
                    writeRam(subLine,index,ram,setIndex)

                data = searchRam(index,tag,blockSize,ram,setIndex)
                writeBlockOnCache(data,tag,index,cache,mapping,setIndex,lineIndex)



    else :
        for access in trace:
            iterates += 1
            blockOffset,index,tag,tagWithIndex,op = TADecoder(access,blockSize,cacheSize)

            hit = 0
            lineIndex = None
            for i, line in enumerate(cache) :
                if line[0] == 1 and line[1] == tag :
                    cacheHit += 1
                    hit = 1
                    break
                else :      
                    if line[4] == 0:
                        subLine = line
                        lineIndex = i


            if hit == 0 :  #cache miss
                cacheMiss += 1
                if subLine[2] == 1:             
                    writeRam(subLine,index,ram)
                data = searchRam(index,tagWithIndex,blockSize,ram)
                writeBlockOnCache(data,tag,lineIndex,cache,mapping)

    return [ 
        cacheHit,
        cacheMiss
    ]







