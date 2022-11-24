from random import randint
from functools import reduce


class Product:
    def __init__(self, mass, cost):
        self.mass = mass
        self.cost = cost

def randomProduct(count):
    arr = []
    for i in range (count):
        arr.append(Product(randint(0, 20), randint(0, 100)))
    return arr


def deleteNulDif(arr):
    
    for i in range(len(arr))[::-1]:
        if arr[i] < 0:
            arr.pop(i)
    return arr

def maxCost(dif, productList):
    c = dif[0] + productList[0].cost
    if len(dif) == 1:
        return c
    elif len(dif) > 1:
        for i in range (len(dif) - 1):
            c = max(c, dif[i+1] + productList[i+1].cost)
    return c

def f(currentMas: float, productList: list) -> float:
    if currentMas < 0:
        return -1
    if currentMas >= 0 and currentMas < productList[0].mass:
        return 0
    dif = [None] * len(productList)
    dif = list(map(lambda x: currentMas - x.mass, productList))
    dif = list(filter(lambda x: x >= 0, dif))
    dif = list(map(lambda x, y: int(f(x, productList) + y.cost), dif, productList))
    dif = max(dif)

    return dif

def SearchMaxCost(targetMass: int, productList : list) -> list:
    countProduct = len(productList) + 1
    targetMass += 1
    sizeW = []
    for i in range (countProduct - 1):
        sizeW.append(productList[i].mass)
    sizeW.append(targetMass)
       

    newTable = [0] * targetMass

    for k1 in range(1, countProduct):
        for s in range(sizeW[k1 - 1], sizeW[k1]):
                ans = []
                for k in range(1, k1 + 1):
                    ans.append(newTable[s-productList[k-1].mass] + 
                               productList[k - 1].cost)
                newTable[s] = max(ans)
   
    return newTable

def FindProductIndex(k: int, s: int, newTable: list, prList : list, ans: list):

    while (newTable[s] != 0):
        for i in range(k):
            if (newTable[s] == newTable[s - prList[i].mass] + prList[i].cost):
                s -= prList[i].mass
                ans[i] += 1
                break

def PackBack(targetSize: int, countProduct: int, productList: list) -> list:
    productList.sort(key= lambda pr: pr.mass)

    table = SearchMaxCost(targetSize, productList)
    ans = [0] * countProduct
    print(table)

    FindProductIndex(len(productList), targetSize, table, productList, ans)
    summ = 0
    for i in range(len(ans)):
        a = productList[i].cost * ans[i]
        print(i+1, ": count -", ans[i], ", cost -", a)
        summ += a
    
    print(summ)

def main():
    s = 24
    arr = [Product(5, 9), Product(7, 13), Product(11, 21)]

    PackBack(s, len(arr), arr)




main()
    
#def SearchMaxCost(targetMass: int, productList : list) -> list:
#        countProduct = len(productList) + 1
#        targetMass += 1
#        sizeW = []
#        for i in range (1, countProduct - 1):
#            sizeW.append(productList[i].mass)
#        sizeW.append(targetMass)

#        newTable = [0] * countProduct
#        newTable[0] = [0] * sizeW[0]
#        for i in range(1, len(newTable)):
#            newTable[i] = [0] * sizeW[i-1]

#        for k1 in range(1, countProduct):
#            for s in range(1, sizeW[k1 - 1]):
#                if s >= productList[k1 - 1].mass:
#                    ans = []
#                    for k in range(1, k1 + 1):
#                        ans.append(newTable[k1][s-productList[k-1].mass] + productList[k-1].cost)
#                    newTable[k1][s] = max(ans)
#                else:     
#                    newTable[k1][s] = newTable[k1-1][s]
#        return newTable


    #newTable = [0] * countProduct
    #for i in range(len(newTable)):
    #    newTable[i] = [0] * targetMass

    #for i in range(countProduct):
    #    newTable[i][0] = 0
    #for i in range(targetMass):
    #    newTable[0][i] = 0

   

#def FindProductIndex(k: int, s: int, newTable: list, prList : list, ans: list):
#    if newTable[k][s] == 0: 
#        return
#    for i in range(k):
#        print(newTable[k][s - prList[i].mass] + prList[i].cost, " == ", newTable[k][s])
#        if (newTable[k][s] == newTable[k][s - prList[i].mass] + prList[i].cost):
#            FindProductIndex(k, s - prList[i].mass, newTable, prList, ans)
#            ans.append(i)
        
#def FindProductIndex(k: int, s: int, newTable: list, prList : list, ans: list):

#    while (newTable[k][s] != 0):
#        for i in range(k):
#            #print(newTable[k][s - prList[i].mass] + prList[i].cost, " == ", newTable[k][s])
#            if (newTable[k][s] == newTable[k][s - prList[i].mass] + prList[i].cost):
#                s -= prList[i].mass
#                ans[i] += 1
#                #ans.append(i)
#                break



       
