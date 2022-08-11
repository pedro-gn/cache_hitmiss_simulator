from math import ceil
from main import processor
from tabulate import tabulate
import matplotlib.pyplot as plt
#abre os arquivos
trace1 = open("traces/trace1.txt","r")
trace2 = open("traces/trace2.txt","r")
trace3 = open("traces/trace3.txt","r")

trace1 = trace1.readlines()
trace2 = trace2.readlines()
trace3 = trace3.readlines()


cacheSizes = [16,32,64,128,256]
blockSizes = [1,2,4,8]


print("---------------------------------------------------------")
print("            ------ MAPEAMENTO DIRETO ------")
print("---------------------------------------------------------")

print("------------------------TRACE1---------------------------")
table = [["Cache Size","Block Size","Hit","Miss","HitTax"]]
data = []
for cSize in cacheSizes :
    for bSize in blockSizes :
        hit,miss = processor(0,cSize,bSize,trace1)
        hitTax = ceil((hit/len(trace1)) * 100)
        table.append([cSize,bSize,hit,miss,hitTax])
        data.append(hitTax)
print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))


print("------------------------TRACE2---------------------------")
table = [["Cache Size","Block Size","Hit","Miss","HitTax"]]
for cSize in cacheSizes :
    for bSize in blockSizes :
        hit,miss = processor(0,cSize,bSize,trace2)
        hitTax = ceil((hit/len(trace1)) * 100)
        table.append([cSize,bSize,hit,miss,hitTax])
print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))


print("------------------------TRACE3---------------------------")
table = [["Cache Size","Block Size","Hit","Miss","HitTax"]]
for cSize in cacheSizes :
    for bSize in blockSizes :
        hit,miss = processor(0,cSize,bSize,trace3)
        hitTax = ceil((hit/len(trace1)) * 100)
        table.append([cSize,bSize,hit,miss,hitTax])
print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))

print("---------------------------------------------------------")
print("         ------ MAPEAMENTO ASSOCIATIVO 2 VIAS ------     ")
print("---------------------------------------------------------")

print("------------------------TRACE1---------------------------")
table = [["Cache Size","Block Size","Hit","Miss","HitTax"]]
for cSize in cacheSizes :
    for bSize in blockSizes :
        hit,miss = processor(1,cSize,bSize,trace1)
        hitTax = ceil((hit/len(trace1)) * 100)
        table.append([cSize,bSize,hit,miss,hitTax])
print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))

print("------------------------TRACE2---------------------------")
table = [["Cache Size","Block Size","Hit","Miss","HitTax"]]
for cSize in cacheSizes :
    for bSize in blockSizes :
        hit,miss = processor(1,cSize,bSize,trace2)
        hitTax = ceil((hit/len(trace1)) * 100)
        table.append([cSize,bSize,hit,miss,hitTax])
print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))


print("------------------------TRACE3---------------------------")
table = [["Cache Size","Block Size","Hit","Miss","HitTax"]]
for cSize in cacheSizes :
    for bSize in blockSizes :
        hit,miss = processor(1,cSize,bSize,trace3)
        hitTax = ceil((hit/len(trace1)) * 100)
        table.append([cSize,bSize,hit,miss,hitTax])
print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))

print("---------------------------------------------------------")
print("         ------ MAPEAMENTO ASSOCIATIVO 4 VIAS ------     ")
print("---------------------------------------------------------")

print("------------------------TRACE1---------------------------")
table = [["Cache Size","Block Size","Hit","Miss","HitTax"]]
for cSize in cacheSizes :
    for bSize in blockSizes :
        hit,miss = processor(2,cSize,bSize,trace1)
        hitTax = ceil((hit/len(trace1)) * 100)
        table.append([cSize,bSize,hit,miss,hitTax])
print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))

print("------------------------TRACE2---------------------------")
table = [["Cache Size","Block Size","Hit","Miss","HitTax"]]
for cSize in cacheSizes :
    for bSize in blockSizes :
        hit,miss = processor(2,cSize,bSize,trace2)
        hitTax = ceil((hit/len(trace1)) * 100)
        table.append([cSize,bSize,hit,miss,hitTax])
print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))


print("------------------------TRACE3---------------------------")
table = [["Cache Size","Block Size","Hit","Miss","HitTax"]]
for cSize in cacheSizes :
    for bSize in blockSizes :
        hit,miss = processor(2,cSize,bSize,trace3)
        hitTax = ceil((hit/len(trace1)) * 100)
        table.append([cSize,bSize,hit,miss,hitTax])
print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))

print("---------------------------------------------------------")
print("      ------ MAPEAMENTO TOTALMENTE ASSOCIATIVO ------    ")
print("---------------------------------------------------------")

print("------------------------TRACE1---------------------------")
table = [["Cache Size","Block Size","Hit","Miss","HitTax"]]
for cSize in cacheSizes :
    for bSize in blockSizes :
        hit,miss = processor(3,cSize,bSize,trace1)
        hitTax = ceil((hit/len(trace1)) * 100)
        table.append([cSize,bSize,hit,miss,hitTax])
print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))

print("------------------------TRACE2---------------------------")
table = [["Cache Size","Block Size","Hit","Miss","HitTax"]]
for cSize in cacheSizes :
    for bSize in blockSizes :
        hit,miss = processor(3,cSize,bSize,trace2)
        hitTax = ceil((hit/len(trace1)) * 100)
        table.append([cSize,bSize,hit,miss,hitTax])
print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))


print("------------------------TRACE3---------------------------")
table = [["Cache Size","Block Size","Hit","Miss","HitTax"]]
for cSize in cacheSizes :
    for bSize in blockSizes :
        hit,miss = processor(3,cSize,bSize,trace3)
        hitTax = ceil((hit/len(trace1)) * 100)
        table.append([cSize,bSize,hit,miss,hitTax])
print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))