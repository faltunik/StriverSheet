from os import *
from sys import *
from collections import *
from math import *

from sys import stdin, stdout, setrecursionlimit



#Example 1
# here we are tryinh to create arra and a target element using the input

def findTriplets(arr, N, K):
    pass

def takeInput():
    N = int(stdin.readline()) 
    arr = list(map(int, stdin.readline().strip().split(" ")))
    K = int(stdin.readline())
    return N, arr,K


tc = int(input())
while tc > 0:
    N, arr,K = takeInput()
    ans = findTriplets(arr, N,K)

    if len(ans) == 0:
        stdout.write("-1\n")

    else:
        for i in ans:
            i.sort()
            stdout.write(str(i[0]) + " " + str(i[1]) + " " + str(i[2]) + "\n")

    tc -= 1
