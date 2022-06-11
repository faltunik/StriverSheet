# https://www.codingninjas.com/codestudio/problems/subset-sum-equal-to-k_1550954


# recursive solution
def subsetSumToK(n, k, arr):
    
    # normal dp problem
    # comparing with knapsack
    # k = weight
    # arr  = arr
    # so we can break it into subproblems, every subproblem will have 
    dp = [[-1 for i in range(k+1)] for i in range(n+1)]                
    
    def help(i,s):
        if i<=0 or s==k:
            if s ==k: return True
            else: return False
        if dp[i][s] != -1 : return dp[i][s]
        c1 = False
        c2 = help(i-1, s) if dp[i-1][s] == -1  else dp[i-1][s] 
        if s + arr[i-1] <=k: c1 = help(i-1, s+arr[i-1]) if dp[i-1][s + arr[i-1]] == -1  else dp[i-1][s + arr[i-1]] 
        tmp = c1 or c2
        dp[i][s] =  tmp
        return dp[i][s]
    
    return help(n, 0)



# dp solution
# wrong, will improve someday
def subsetSumToK(n, k, arr):
    
    # normal dp problem
    # comparing with knapsack
    # k = weight
    # arr  = arr
    # so we can break it into subproblems, every subproblem will have 
    
    dp = [[-1 for i in range(k+1)] for i in range(n+1)]
    # if k ==0
    for i in range(n+1):
        dp[i][0] = True
    # for n ==0:
    for i in range(1,k+1):
        dp[0][1] = False
        
    for i in range(1, n+1):
        for j in range(1,k+1):
            if arr[i-1] <=j:
                dp[i][j] = dp[i-1][j] or dp[i][j-arr[i-1]]
            else:
                dp[i][j] = dp[i-1][j] 
    return dp[n][k]