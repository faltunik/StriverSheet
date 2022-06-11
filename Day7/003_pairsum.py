# easy
# https://www.codingninjas.com/codestudio/problems/pair-sum_697295



from os import *
from sys import *
from collections import *
from math import *


# gives wrong answer
def pairSum(arr, s):
    # Write your code here.
    ans = []
    dic = {}
    arr.sort()
    for i in arr:
        if dic.get(i, False):
            ans.append([dic.get(i), i])
        else:
            dic[s-i] = i
    ans.sort(key= lambda x: x[0])
    return ans

# new idea
# I can store count of each elemetn in dictionary
# then I can travel though arr,
# if I found s-arr[i] in dictionary, I can add [i, s-arr[i]]*count of i to ans



# passed 6/8 test cases
# failed test case
# n = 247 and s= 4
# -1 3 8 6 -7 -1 -2 -9 -1 1 5 -8 8 -4 6 4 4 1 -9 9 0 7 -9 -4 -3 4 -6 -5 -4 8 0 3 5 -5 5 3 -9 -5 -5 0 7 4 -6 -7 -5 5 -6 8 6 0 9 9 0 -7 -8 -1 7 -4 -3 -3 -8 1 4 8 1 8 3 -8 -4 -3 0 6 -7 7 -7 0 8 1 6 -8 -2 0 9 -5 3 -1 -3 -3 7 4 0 -2 3 0 -4 5 -5 -8 -6 2 -5 -6 -3 -7 4 4 6 -5 5 5 -4 0 -9 -3 3 0 -9 0 -4 7 0 -1 -9 1 -9 3 6 9 6 1 -2 0 -8 8 -5 4 2 0 0 -2 0 -1 -3 3 4 3 -4 1 0 -9 -4 -9 9 -7 1 1 0 6 -9 -4 9 4 -5 0 0 4 2 7 -2 1 7 -8 0 -4 -2 0 -9 -2 -7 -8 6 -4 -4 9 0 0 -5 -4 0 8 -8 4 -5 0 -2 -8 -2 6 8 -9 9 -5 -1 3 -2 -1 -1 -1 -4 4 2 -9 -4 -1 4 -4 0 -1 7 9 4 -6 5 -3 2 -5 -5 4 2 -3 6 6 2 0 4 -3 0 -4 0 0 4 1 -5 7 -4 -7 6 

from os import *
from sys import *
from collections import *
from math import *

def pairSum(arr, s):
    # Write your code here.
    d = Counter(arr)
    ans = []
    arr.sort()
    for i in arr:
        key = s-i 
        c = d.get(key, 0)
        toadd = [[i,s-i] for _ in range(c)]
        del d[i]
        ans.extend(toadd)
    ans.sort()
    return ans