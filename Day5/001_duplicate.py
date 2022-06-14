from os import *
from sys import *
from collections import *
from math import *


# passed two 10/11 cases
def findDuplicate(arr:list, n:int):
    # Write your code here.
    a = list(set(arr))
    n = sum(arr) - sum(a)
    d = len(arr) - len(a)
    return round(n/d)

# passed 10/11 cases
from os import *
from sys import *
from collections import *
from math import *

def findDuplicate(arr:list, n:int):
    # Write your code here.
    arr.sort()
    for i in range(1,len(arr)):
        if arr[i-1] == arr[i]:
            break
    return arr[i]

# https://www.codingninjas.com/codestudio/problems/find-duplicate-in-array_1112602?topList=striver-sde-sheet-problems
# i know, that I haven't passed all test cases but still
