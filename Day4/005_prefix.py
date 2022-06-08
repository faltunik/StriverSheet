def longestCommonPrefix(arr, n):
    # this is famous  leetcode easy  problem
    res = ""
    l = list(zip(*arr)) 
    for ele in l:
        if len(set(ele)) ==1:
            res += ele[0]
        else:
            return res
    return res

# https://www.codingninjas.com/codestudio/problems/count-inversions_615?topList=striver-sde-sheet-problems
# at first, I made a mistake, that is instead of writing res += ele[0], I simply wrote res + ele[0], I forget to write =, I will call this dubness error
