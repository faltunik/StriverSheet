from os import *
from sys import *
from collections import *
from math import *

from sys import stdin,setrecursionlimit
setrecursionlimit(10**7)

def sort012(arr, n) :
    dic = Counter(arr)
    val = 0
    rem = dic.get(0,0)
    for i in range(len(arr)):
        while rem==0:
            val = val+1
            rem = dic.get(val, 0)
        arr[i] = val
        rem -=1
    return arr

    


#taking inpit using fast I/O
def takeInput() :
	n = int(input().strip())

	if n == 0 :
		return list(), 0

	arr = list(map(int, stdin.readline().strip().split(" ")))

	return arr, n



def printAnswer(arr, n) :
    
    for i in range(n) :
        
        print(arr[i],end=" ")
        
    print()
    
#main

t = int(input().strip())
for i in range(t) :

    arr, n= takeInput()
    sort012(arr, n)
    printAnswer(arr, n)



# https://www.codingninjas.com/codestudio/problems/stocks-are-profitable_893405?topList=striver-sde-sheet-problems
# 1st attmept: failed to realize that if rem comes zero, it will change value only once, thus, we got this error
# 2nd attempt: Realizes it, and solved  (6June)
# so, first code had bugs and time taken is very bad for easy problem: 15-20+ minutes