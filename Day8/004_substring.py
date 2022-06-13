# https://www.codingninjas.com/codestudio/problems/number-of-distinct-substring_1465938?topList=striver-sde-sheet-problems



#bruteforce
def distinctSubstring(word):
    # Write your code here.
    ans = []
    n = len(word)
    d = {}
    for i in range(n):
        j = n
        while j>i:
            tmp = word[i:j]
            if d.get(tmp, True): ans.append(tmp)
            d[tmp] = False
            j -=1
    return len(ans)

# optimization
# memory is O(kn) is very bad
# how to optimize it?
# how to handle duplicate cases, we need memeory to handle duplitcates, so how to handle it?


# smaller optimization
def distinctSubstring(word):
    # Write your code here.
    ans = []
    n = len(word)
    d = {}
    for i in range(n):
        j = i+1
        s = word[i:j]
        while n>=j:
            tmp = s+word[j]
            if d.get(tmp, True): ans.append(tmp)
            d[tmp] = False
            j +=1
    return len(ans)
