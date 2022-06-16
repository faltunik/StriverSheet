# https://www.codingninjas.com/codestudio/problems/0-1-knapsack_1072980?topList=striver-sde-sheet-problems

# so, I tried different problems but failed
# so tried this knapsack 

# medium


def maxProfit(values, weights, n, w):
    
    dp = [[-1 for i in range(w+1)] for i in range(n+1)]
    def help(i,w):
        if i<=0 or w<=0:
            return 0
        if dp[i][w] != -1: return dp[i][w]
        l = help(i-1, w)
        r = float('-inf')
        if weights[i-1] <=w:
            r = help(i-1, w-weights[i-1]) + values[i-1]
        dp[i][w] = max(l,r)
        return dp[i][w]
        
    return help(n,w)