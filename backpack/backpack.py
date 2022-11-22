from random import randint
from functools import *


class Product:
    def __init__(self, mass, cost):
        self.mass = mass
        self.cost = cost
    @property
    @classmethod
    def getItemMass(self) -> float:
        return self.mass
    @classmethod
    @getItemMass.setter
    def setItemMas(self, mass1: float) -> None:
        self.mass = mass1




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
    #for i in range(len(productList)):
    #    dif[i] = currentMas - productList[i].mass
    dif = list(map(lambda x: currentMas - x.mass, productList))
    #dif = deleteNulDif(dif)
    dif = list(filter(lambda x: x >= 0, dif))
    #for i in range(len(dif)):
    #    dif[i] = f(dif[i], productList)
    dif = list(map(lambda x, y: int(f(x, productList) + y.cost), dif, productList))
    #dif = maxCost(dif, productList)
    dif = max(dif)

    return dif
    
def SearchMaxCost(targetMass: int,productList : list) -> list:
    countProduct = len(productList) + 1
    targetMass += 1
    newTable = [None] * countProduct
    for i in range(len(newTable)):
        newTable[i] = [None] * targetMass
    for i in range(countProduct):
        newTable[i][0] = 0
    for i in range(targetMass):
        newTable[0][i] = 0
    for k in range(1,countProduct):
        for s in range(1, targetMass):
            if s >= productList[k - 1].mass:
                newTable[k][s] = max(newTable[k-1][s], newTable[k-1][s-productList[k-1].mass] + productList[k - 1].cost)
            else:
                newTable[k][s] = newTable[k-1][s]
    return newTable

def FindProductIndex(k: int, s: int, newTable: list, prList : list, ans: list):
    if newTable[k][s] == 0: 
        return
    if (newTable[k][s] == newTable[k-1][s]):
        FindProductIndex(k - 1, s, newTable, prList, ans)
    else:
        FindProductIndex(k - 1, s - prList[k - 1].mass, newTable, prList, ans)
        ans.append(k - 1)


def main():
    s = 20
    arr = [Product(5, 9), Product(7, 13), Product(11, 21)]
    #arr = [Product(3, 1), Product(4, 6), Product(5, 4), Product(8, 7), Product(9, 6) ]
    #arr = sorted(arr, key = lambda pr: pr.mass)
    arr.sort(key= lambda pr: pr.mass)
    table = SearchMaxCost(s, arr)
    ans = []
    FindProductIndex(len(arr), s - 1, table, arr, ans)
    for i in range(len(arr) + 1):
        print(table[i])

    #for i in arr:
    #    print(i.mass, " ", i.cost)
    #print(f(200, arr))


main()

       
