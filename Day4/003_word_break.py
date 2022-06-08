#https://www.codingninjas.com/codestudio/problems/word-break_1094901?topList=striver-sde-sheet-problems

def wordBreak(arr, n, target):
    # Write your code here.
    memo = [[-1 for i in range(len(target)+1)] for i in range(len(target)+1)]
    def help(i,j):
        if i>j: return True
        if memo[i][j] !=-1: return memo[i][j]
        if target[i:j] in arr:
            memo[i][j] = True
            return memo[i][j]
        ans = False       
        for k in range(i, j):
            tmp = help(i,k) and help(k,j)
            ans = tmp or ans
        memo[i][j] = ans
        return memo[i][j]
    
    return help(0, len(target))


# I had already solved this problem on leetcode, given the experience, I still took 45 minute
# to solve this problem.
# first used dictionary but it was giving me a TLE
# then I used 2d matrix to store the result