# https://www.codingninjas.com/codestudio/problems/kth-largest-element-in-the-unsorted-array_893030?topList=striver-sde-sheet-problems
from sys import stdin, stdout
import heapq


def kthLargest(arr, size, k):
    # Write your code here.
    # what if len(arr) <k
    if len(arr) <=k: return max(arr)
    h = arr[:k]
    heapq.heapify(h)
    for i in arr[k:]:
        if h[0] < i:
            heapq.heappushpop(h, i)
    return h[0]
    