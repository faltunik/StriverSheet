# https://www.codingninjas.com/codestudio/problems/longest-increasing-subsequence_630459?topList=striver-sde-sheet-problems

#first solution, passed:  5/9
# I almost waste 1hr in this stupid problem and this stupid solution
from sys import stdin
import sys 
sys.setrecursionlimit(10**7)
def longestIncreasingSubsequence(arr, n) :
    n = len(arr)
    memo = {}
    def help(i, l, s):
        if i>=n: return 0
        if memo.get((i,l), -1) != -1: return memo[(i,l)]
        c1 = help(i+1, arr[i], s) +1 if arr[i] >l else float('-inf')
        c2 = help(i+1,l, s) 
        memo[(i,l)] = max(c1,c2)
        return memo[(i,l)]
    return help(0, -100001, 0)

# i need to resolve this with better method,
# so this shouldn't be counted as a solution