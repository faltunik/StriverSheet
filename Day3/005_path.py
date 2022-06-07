import sys
sys.setrecursionlimit(10**7)

def minSumPath(grid):
    N = len(grid)
    M = len(grid[0])
    dp = [[-1 for i in range(M+1)] for i in range(N+1)]
    def help(i,j, c):
        if i== N-1 and j == M-1:return c + grid[i][j]
        if dp[i][j] != -1: return dp[i][j]
        r = help(i,j+1, c) if j<M-1 else float('inf')
        d = help(i+1,j, c) if i<N-1 else float('inf')
        dp[i][j] = min(r,d) + grid[i][j]
        return dp[i][j]
    return help(0,0,0)


# follow-up
# try to solve using real dp approach