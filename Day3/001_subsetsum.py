#https://www.codingninjas.com/codestudio/problems/subset-sum_3843086?topList=striver-sde-sheet-problems&leftPanelTab=0
from typing import List

def subsetSum(num: List[int]) -> List[int]:
    # Write your code here.
    # so order doesn't matter
    # this is simple recursion questions
    ans = []
    n = len(num)
    def help(i,s, ans):
        if i >=n:
            ans.append(s)
            return
        help(i+1, s+num[i], ans)
        help(i+1,s, ans)
        return 
    help(0,0,ans)
    return sorted(ans)