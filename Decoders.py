import math

#DIRECT MAPPING DECODER
def DMDecoder(access,blockSize,cacheSize):

    #acha a quantidade de bits para o indice e offset do bloco
    blockOffsetBits = int(math.log(blockSize,2))
    indexBits = int(math.log(cacheSize,2))

    #separa os bits de offset , indice , tag do endereco , e operacao (read or write)
    blockOffset = access[ (18 - blockOffsetBits) : 18]
    index = access[(18- blockOffsetBits - indexBits) : (18 - blockOffsetBits)]
    tag = access[2 : (18- blockOffsetBits - indexBits)]
    op = access[0]
    return [ 
        blockOffset,
        index,
        tag,
        op,
    ]


#FULLY ASSOCIATIVE DECODER
def TADecoder(access,blockSize,cacheSize):

    #acha a quantidade de bits para o indice e offset do bloco
    blockOffsetBits = int(math.log(blockSize,2))
    indexBits = int(math.log(cacheSize,2))

    #separa os bits de offset , indice , tag do endereco , e operacao (read or write)
    blockOffset = access[ (18 - blockOffsetBits) : 18]
    index = access[(18- blockOffsetBits - indexBits) : (18 - blockOffsetBits)]
    tag = access[2 : (18- blockOffsetBits)]
    tagWithIndex = access[2 : (18- blockOffsetBits - indexBits)]
    op = access[0]
    return [ 
        blockOffset,
        index,
        tag,
        tagWithIndex,
        op,
    ]

#ASSOCIATIVE DECODER
def ADecoder(access,blockSize,cacheSize,ways):

    blockOffsetBits = int(math.log(blockSize,2))
    indexBits = int(math.log(cacheSize,2))
    setBits = int(math.log((cacheSize/ways),2)) 

    #separa os bits de offset , indice , set index , tag do endereco , e operacao (read or write)
    blockOffset = access[ (18 - blockOffsetBits) : 18]
    index = access[(18 - blockOffsetBits - indexBits) : (18 - blockOffsetBits)]
    setIndex = access[ (18 - blockOffsetBits - setBits) : ( 18 - blockOffsetBits )]
    tag = access[2 : (18 - blockOffsetBits - setBits )]
    op = access[0]

    return [
        blockOffset,
        setIndex,
        tag,
        op,
        index,
    ]


