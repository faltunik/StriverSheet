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


# I didn't comeup with this solution, but it is best beginners solution ever
class Solution:
    def minPathSum(self, grid):
        n = len(grid)
        m = len(grid[0])
        for i in range(1,n):
            grid[i][0] = grid[i-1][0] + grid[i][0]
        for j in range(1, m):
            grid[0][j] = grid[0][j-1] + grid[0][j]
        
        for i in range(1,n):
            for j in range(1, m):
                grid[i][j] = grid[i][j] + min(grid[i-1][j], grid[i][j-1])
        return grid[n-1][m-1]
                