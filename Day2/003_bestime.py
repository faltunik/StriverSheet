from os import *
from sys import *
from collections import *
from math import *

# brutforce
def maximumProfit(prices):
    # Write your code here.
    if prices == sorted(prices): return prices[-1] -prices[0]
    if prices == sorted(prices, reverse=  True): return 0
    ans = 0
    for i in range(len(prices)-1):
        tmp = max(prices[i+1:])
        if tmp >prices[i]:
            ans = max(ans, tmp-prices[i])
    return ans


# so I was able to solve it using brutforce approach
# so follow up will be to optimize
# optimization
# create array containing max value at right of that index


# 1st attempt: passed(6June) # but takes 15+ min for brutforce, so not good


# https://www.codingninjas.com/codestudio/problems/stocks-are-profitable_893405?topList=striver-sde-sheet-problems

