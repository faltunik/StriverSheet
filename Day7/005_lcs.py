# https://www.codingninjas.com/codestudio/problems/longest-common-subsequence_624879
from sys import stdin

# def lcs(s, t) :
# 	#Your code goes here
#     m = len(s)
#     n = len(t)
#     dp = [[-1 for _ in range(n+1)] for _ in  range(m+1)]
    
#     # if s == ""
#     for i in range(n):
#         dp[0][i] = 0
#     # if t == ""
#     for i in range(m):
#         dp[i][0] = 0
    
#     for i in range(1, m+1):
#         for j in range(1, n+1):
#             if s[i-1] == t[j-1]:
#                 dp[i][j] = dp[i-1][j-1] + 1
#             else:
#                 dp[i][j] = max(dp[i-1][j], dp[i][j-1])
#     return dp[m][n]


# I had already solved this problem, for this week, I am counting them, but from next week, I will not count those questions, this is personal promize


dp1 =  [[-1]*(5+1)]*(7+1)
dp2 = [[-1 for _ in range(5+1)] for _ in  range(7+1)]
print(dp1 == dp2)
