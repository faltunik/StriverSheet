# medium/easy
# https://www.codingninjas.com/codestudio/problems/ninja-and-sorted-arrays_1214628?topList=striver-sde-sheet-problems


from os import *
from sys import *
from collections import *
from math import *
import bisect



#burteforce
def ninjaAndSortedArrays(arr1,arr2,m,n):
    arr1 = arr1[:m]
    for i in arr2:
        j = bisect.bisect(arr1, i)
        arr1.insert(j, i)
    return arr1



#better appraoch
def ninjaAndSortedArrays(arr1,arr2,m,n):
    arr1 = arr1[:m]
    i = j =0
    while i <len(arr1) and j<len(arr2):
        while i <len(arr1) and arr1[i] < arr2[j]:
            i +=1
        if i>=len(arr1):
            break
        arr1.insert(i, arr2[j])
        i +=1
        j +=1
    # now possibilities are
    arr1.extend(arr2[j:])
    return arr1