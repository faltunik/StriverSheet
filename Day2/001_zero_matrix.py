from os import *
from sys import *
from collections import *
from math import *

from typing import List

def setZeros(matrix: List[List[int]]) -> None:
    # so first we will check whether row=0 has zeros or not
    r = any(matrix[0][i]==0 for i in range(0, len(matrix[0])))
    # then we will check wehther col =0 has zeros or not
    c = any(matrix[i][0]==0 for i in range(0, len(matrix)))
    
    # now we will travel in matrix and if we found any number equal to zero(a[i][j]), then we will make a[i][0] = Zero and a[0][j] equal to zero
    # Then we will travel again in matrix and if we found 
    # then for a[i][j] if either a[i][0] or a[0][j] is equal to 
    # zero, we will put it's value zero
    # then we if get any r = True, then we will set first zero equal to zero
    # if we get c = True, we will set first coloumn = 0
    
    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[0])):
            if matrix[i][j] ==0:
                matrix[0][j] = 0
                matrix[i][0] = 0
    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[0])):
            if matrix[0][j] ==0 or matrix[i][0] ==0:
                matrix[i][j] =0
    if r:
        for j in range(len(matrix[0])):
            matrix[0][j] = 0
    if c:
        for i in range(len(matrix)):
            matrix[i][0] = 0
    return matrix


# easy problem: https://www.codingninjas.com/codestudio/problems/set-matrix-zeros_3846774?topList=striver-sde-sheet-problems

# to be honest, I was able to solve because I had already solved the problem in leetcode just a week ago and without that
# i would have failed miserably 
# Second attempt= passed(6June) but it's kind of cheating, because you had already memorized the solution week ago
