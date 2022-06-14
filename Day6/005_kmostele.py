# https://www.codingninjas.com/codestudio/problems/k-most-frequent-elements_3167808?topList=striver-sde-sheet-problems

# bruteforce

from typing import List
from collections import Counter


def KMostFrequent(n: int, k: int, arr: List[int]) -> List[int]:
    dic = Counter(arr)
    # now I wanna sort the arr by values
    c = 0
    ans = []
    for key in sorted(dic, key=dic.get, reverse=True):
        ans.append(key)
        c +=1
        if c>=k:
            return sorted(ans)
    return sorted(ans)


# optimize