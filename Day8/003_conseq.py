# https://www.codingninjas.com/codestudio/problems/longest-consecutive-sequence_759408?topList=striver-sde-sheet-problems
# result


# first attempt
# wrong attempt
from os import *
from sys import *
from collections import *
from math import *
import heapq

def lengthOfLongestConsecutiveSequence(arr, n):
    arr.sort()
    i = 0
    ans = 0
    for j in range(n):
        if i>=n: return ans
        l = j+1-i
        tmp = [i+k for k in range(j+1)]
        if arr[i:j+1]== tmp:
            ans = max(l, ans)
        else:
            i +=1
    return ans



# let's start with bruteforce solution
def lengthOfLongestConsecutiveSequence(arr, n):
    # Write your code here
    arr.sort()
    prev = arr[0]
    ans = 1
    tmp = 1
    for i in arr[1:]:
        if i == prev:
            continue
        if i-prev ==1:
            tmp +=1           
        else:
            ans = max(ans, tmp)
            tmp =1
        prev = i
    ans = max(ans, tmp)
    return ans


# now we will look for optimization
# our solution is nlogn + n +k = nlogn and memory is O(1)
# requirment = time = O(n) and memory = O(n)
# so we can can utilize  memory to instead of sorting the array
# guiding que
# what data structure we can use?
# Hint: Can you use heap


def lengthOfLongestConsecutiveSequence(arr, n):
    heapq.heapify(arr)   
    prev = heapq.heappop(arr)
    ans = 1
    c = 1
    while arr:
        tmp = heapq.heappop(arr)
        if tmp-prev == 1:
            c+=1
        elif tmp-prev >1:
            c=1
        ans = max(ans, c)
        prev = tmp
    return ans