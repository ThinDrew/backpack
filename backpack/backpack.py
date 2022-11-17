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

def f(currentMas, productList):
    if currentMas < 0:
        return -1
    if currentMas >= 0 and currentMas < productList[0].mass:
        return 0
    dif = [None] * len(productList)
    for i in range(len(productList)):
        dif[i] = currentMas - productList[i].mass
    dif = deleteNulDif(dif)
    #map(lambda x,y: f(x,y), dif, productList)
    for i in range(len(dif)):
        dif[i] = f(dif[i], productList)
    dif = maxCost(dif, productList)
    return dif
     

def main():
    arr = [Product(5, 9), Product(7, 13), Product(11, 21)]
    arr = sorted(arr, key = lambda pr: pr.mass)
    for i in arr:
        print(i.mass, " ", i.cost)
    print(f(12, arr))

main()
