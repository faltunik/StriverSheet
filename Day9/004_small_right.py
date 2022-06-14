# https://www.codingninjas.com/codestudio/problems/next-smaller-element_1112581?topList=striver-sde-sheet-problems
# medium

def nextSmallerElement(arr,n):
    # Write your code here.
    stack = []
    ans = []
    for i in arr[::-1]:
        while stack and i<=stack[-1]:
            stack.pop()
        if not stack: ans.append(-1)
        else: ans.append(stack[-1])
        stack.append(i)
    return ans[::-1]