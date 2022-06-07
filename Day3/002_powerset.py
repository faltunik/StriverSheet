def pwset(v):
    # Write your code here
    # Return a 2-D list containing all subsets
    num = sorted(list(set(v)))
    n = len(num)
    ans = []
    def help(i,s, ans):
        if i >=n:
            ans.append(s)
            return
        help(i+1, s+[num[i]], ans)
        help(i+1,s, ans)
        return 
    help(0,[], ans)
    return ans


# this solution getting submitted in leetcode
# but not in code ninja
# https://www.codingninjas.com/codestudio/problems/power-set_1062667?topList=striver-sde-sheet-problems


# get submitted in codninja, no idea I just removed set and sort from the solution
def pwset(v):
    # Write your code here
    # Return a 2-D list containing all subsets
    num = sorted(v)
    n = len(num)
    ans = []
    def help(i,s, ans):
        if i >=n:
            ans.append(s)
            return
        help(i+1, s+[num[i]], ans)
        help(i+1,s, ans)
        return 
    help(0,[], ans)
    return ans