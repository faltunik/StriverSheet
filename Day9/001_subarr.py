# easy
#https://www.codingninjas.com/codestudio/problems/longest-subset-zero-sum_920321?topList=striver-sde-sheet-problems
# good attempt

from os import *
from sys import *
from collections import *
from math import *

# bruteforce
def LongestSubsetWithZeroSum(arr):
    # subarray are contiguous
    ans = 0
    n = len(arr)
    for i in range(n):
        j = i
        s = 0
        while n>j:
            s += arr[j]
            if s ==0: ans = max(ans, j-i+1)
            j +=1
    return ans

# so, what we can optimize?