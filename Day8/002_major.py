# https://www.codingninjas.com/codestudio/problems/majority-element-ii_893027?topList=striver-sde-sheet-problems


#bruteforce
from os import *
from sys import *
from collections import *
from math import *

def majorityElementII(arr):
    n = len(arr)
    mn = len(arr)//3+1
    d = Counter(arr)
    ans = []
    for key in d:
        if d[key] >= mn: ans.append(key)
    return ans


# optimal
# as of now, I am not able to find how to optimize it
# It is not optimized version, but one pass solution
def majorityElementII(arr):
    n = len(arr)
    mn = len(arr)//3+1
    d = {}
    ans = []
    for key in arr:
        if key in d:
            d[key] += 1
            if d[key] >=mn:
                ans.append(key)
        else:
            d[key] = 1