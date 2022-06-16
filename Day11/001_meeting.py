#easy
#took more than 30 minute,
# not good

# first attempt wrong
def maximumActivities(start, finish):
    # Write your Code here.
    z = list(zip(start, finish))
    n = len(z)
    prev = [0,0]
    # 1 6 2 4 
    # 2 7 5 8 
    
    def help(i, prev):
        if i >=n: return 0
        if z[i][0] >=prev[1]:
            tmp = max(help(i+1, prev) , (help(i+1, z[i]) +1 ))
        else:
            tmp = help(i+1, prev) 
        return tmp
    
    return help(0, prev)


# sometimes, you don't need to find all ways to find optimized solution
def maximumActivities(start, finish):
    # Write your Code here.
    z = list(zip(start, finish))
    n = len(z)
    z.sort(key = lambda x: x[1])
    ans = 1
    prev = z[0]
    for i in z[1:]:
        if prev[1] <= i[0]:
            ans +=1
            prev = i
    return ans