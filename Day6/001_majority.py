from os import *
from sys import *
from collections import *
from math import *

def findMajorityElement(arr, n):
    dic = Counter(arr)
    tar = n//2
    for k in dic.keys():
        if dic[k] > tar:
            return k
    return -1



# failed to sovled using sort method