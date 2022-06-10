# https://www.codingninjas.com/codestudio/problems/job-sequencing-problem_1169460?topList=striver-sde-sheet-problems

# passed 10/11 test cases
def jobScheduling(jobs):
    t = 0
    p = 0
    n = len(jobs)

    jobs.sort()
    dp = [[-1 for i in range(n+1)] for i in range(n+1)]
    def help(i,c):
        if i>=n: return 0
        if dp[i][c] != -1: return dp[i][c]
        if jobs[i][0] >c:
            l = help(i+1, c+1) + jobs[i][1]
            r = help(i+1, c)
            tmp = max(l,r)
        else:
            tmp = help(i+1,c)
        dp[i][c] = tmp
        return dp[i][c]
    return help(0,0)