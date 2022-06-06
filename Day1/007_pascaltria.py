from os import *
from sys import *
from collections import *
from math import *

def printPascal(n:int):
    res = [[1]]
    for i in range(1,n):
        tmp = [0] + res[i-1] + [0]
        fans = []
        for i in range(1,len(tmp)):
            fans.append(tmp[i-1]+tmp[i])
        res.append(fans)
    return res
    