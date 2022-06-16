#https://www.codingninjas.com/codestudio/problems/roman-number-to-integer_981308?topList=striver-sde-sheet-problems
# easy


def romanToInt(s):
    dic = {
        "I":1,
        "V":5,
        "X":10,
        "L":50,
        "C":100,
        "D":500,
        "M":1000,       
    }
    ans = 0
    prev = 0
    for i in s[::-1]:
        if dic[i] <prev:
            ans -= dic[i]
        else:
            ans += dic[i]
        prev = dic[i]
    return ans