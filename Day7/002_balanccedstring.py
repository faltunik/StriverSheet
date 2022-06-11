#https://www.codingninjas.com/codestudio/problems/valid-parenthesis_795104

def isValidParenthesis(expression):
    d = {
        "(": ")",
        "{" : "}",
        "[" : "]"
    }
    stack = []
    for i in expression:
        if i in d:
            stack.append(i)
        else:
            if not stack: return False
            if d[stack[-1]] != i: return False
            stack.pop()
    return stack ==[]


# i had already solved this problem in leetcode, so I shouldn't count this.