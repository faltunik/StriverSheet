
# solved
# medium
#  https://www.codingninjas.com/codestudio/problems/merge-k-sorted-arrays_975379?topList=striver-sde-sheet-problems

#bruteforce
# O(nlogn)
def mergeKSortedArrays(kArrays, k:int):
    arr = [j for i in kArrays for j in i]
    return sorted(arr)

# we can use heap
# O(nlogk)
import heapq
def mergeKSortedArrays(kArrays, k:int):
    h = []
    res = []
    heapq.heapify(h)
    for i in kArrays:
        for j in i:
            heapq.heappush(h, j)
    while h:
        tmp = heapq.heappop(h)
        res.append(tmp)
    return res
