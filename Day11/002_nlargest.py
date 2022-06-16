# https://www.codingninjas.com/codestudio/problems/k-max-sum-combinations_975322?topList=striver-sde-sheet-problems


#Easy
# TLE
import heapq
def kMaxSumCombination(a, b, n, k):
    ans = []
    for i in a:
        for j in b:
            tmp = i+j
            ans.append(tmp)
    heapq.heapify(ans)
    res = heapq.nlargest(k, ans)
    return res
            
