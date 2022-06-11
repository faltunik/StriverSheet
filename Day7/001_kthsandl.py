# https://www.codingninjas.com/codestudio/problems/kth-smallest-and-largest-element-of-array_1115488

import heapq

# bruteforce
# nlogn
def kthSmallLarge(arr, n, k):
    arr.sort()
    s = arr[k-1]
    l = arr[n-k]
    return s,l

# i am sure, I can improve it's time complexity 
# using heap, I can create max and min heap


