#https://www.codingninjas.com/codestudio/problems/unique-subsets_3625236?topList=striver-sde-sheet-problems&leftPanelTab=1

from typing import *

  

# bruteforce 
# gives TLE
def uniqueSubsets(n :int,arr :List[int]) -> List[List[int]]:
    # this looks like 
    # i can improve timecomplexity at cost of memory
    arr.sort()
    ans = []
    
    def help(i,s,ans):
        if i >=n:
            if s not in ans: 
                ans.append(s)
            return 
        help(i+1, s+[arr[i]], ans)
        help(i+1,s, ans)
        return 
    
    help(0,[], ans)
    return ans


# we will do it in night