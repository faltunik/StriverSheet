# https://www.codingninjas.com/codestudio/problems/merge-intervals_699917?topList=striver-sde-sheet-problems

from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)
        prev = intervals[0]
        previd = 0
        i =1
        while i<len(intervals):
            if intervals[i][0] <= prev[1]:
                intervals[previd] = [prev[0], max(intervals[i][1],prev[1])] 
                prev = intervals[previd]
                intervals.pop(i)
            else:
                prev = intervals[i]
                previd = i
                i +=1
        return intervals


# this gets submitted in leetcode but not in coding nija
# plus it is a bruteforce solution, since I am running out of time, I will