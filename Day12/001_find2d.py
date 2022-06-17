# easy
# https://www.codingninjas.com/codestudio/problems/search-in-a-2d-matrix_980531?topList=striver-sde-sheet-problems


# first appraoch
# TLE

def findTargetInMatrix(mat, m, n, k):
    i = 0
    j = m
    r = float('inf')
    # first loop: logm
    while j>i:
        mid = (i+j)//2
        if mat[mid][0]>k:
            j = mid-1
        elif mat[mid][-1] <k:
            i = mid+1
        else:
            r = mid
            break
    if r == float('inf'): return False
    s = 0
    e = n  
    # second loop: logn  
    while e>s:
        c = (s+e)//2
        if mat[r][c] ==k:
            return True
        elif mat[r][c] >k:
            e = mid-1
        else:
            s = mid+1                   
    return False
# total: logm + logn = log(m+n)



#passed all test cases
# bruteforce
def findTargetInMatrix(mat, m, n, k):
    for i in range(m):
        for j in range(n):
            if mat[i][j] == k:
                return True
            break
    return False

#