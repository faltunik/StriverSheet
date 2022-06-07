# https://practice.geeksforgeeks.org/problems/maximum-sum-increasing-subsequence4749/1/

from functools import lru_cache


# gices TLE
# means, dp table is not working properly
class Solution:
    def maxSumIS(self, rack, n):
        # code here
        c = sum(rack)
        dp = [[[-1 for _ in range(c+1)] for _ in range(c+1)]
              for _ in range(n+1)]

        def help(i, s, d):
            if i >= n:
                return d
            if dp[i][s][d] != -1:
                return dp[i][s][d]

            if rack[i] > s:
                tmp = max(help(i+1, rack[i], d+rack[i]), help(i+1, s, d))
            else:
                tmp = help(i+1, s, d)
            dp[i][s][d] = tmp
            return dp[i][s][d]

        return help(0, 0, 0)


# this problem require DP solution, 
# i only know recursion + table
# 1st attempt: Failed(7June)
