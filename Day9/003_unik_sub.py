# https://www.codingninjas.com/codestudio/problems/longest-unique-substring_630418?topList=striver-sde-sheet-problems
# medium


from os import *
from sys import *
from collections import *
from math import *

def uniqueSubstrings(s) :
    # Write your code here.
    #print(s)
    ans = ""
    n = len(s)
    for i in range(n):
        tmp = ""
        j = i
        while j<n:
            if s[j] in tmp:
                break
            tmp+= s[j]
            ans = max(ans, tmp, key=len)
            j +=1
    return len(ans)


# optimization
# store directly length