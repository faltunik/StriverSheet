from os import *
from sys import *
from collections import *
from math import *

from typing import List

def setZeros(matrix: List[List[int]]) -> None:
    # this looks like a dfs and bfs problems
    m1 = len(matrix)//2
    m2 = len(matrix[0])//2
    start = [(m1,m2)]
    ivisited = {}
    jvisited = {}
    while start:
        i,j = start.pop()
        if i in ivisited or j in jvisited:
            continue
        if matrix[i][j] !=0:
            ivisited[i] = True
            jvisited[j] = True
            for c,d in ((i-1,j-1), (i, j-1), (i+1,j-1), (i-1,j), (i,j+1), (i-1, j+1), (i,j+1), (i+1, j+1)):
                if 0<=c<len(matrix) and 0<=d<len(matrix[0]):
                    start.append((c,d))
                
        
           
        else:
            # changing the rows value
            for k in range(len(matrix[0])):
                matrix[i][k] = 0
            # changing the col val
            for k in range(len(matrix)):
                matrix[k][j] = 0
            ivisited[i] = True
            jvisited[j] = True
            for c,d in ((i-1,j-1), (i+1,j-1), (i-1, j+1), (i+1, j+1)):
                start.append(c,d)
    return matrix



if __name__ == '__main__':
    t = int(input('enter nu of test cases: '))
    print('t is ', {t})
    for _ in range(t):
        r,c = list(map(int, input.split()))
        matrix = []
        for _ in range(r):
            tmp = list(map(int, input.split()))
            matrix.append(tmp)
    
    print(setZeros(matrix))

# result: Failed (5June)
# I need to improve My thinking process

            