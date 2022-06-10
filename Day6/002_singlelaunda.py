# https://www.codingninjas.com/codestudio/problems/unique-element-in-sorted-array_1112654?topList=striver-sde-sheet-problems
def uniqueElement(arr, n):
    s1 = sum(arr)
    s2 = sum(list(set(arr)))
    return 2*s2 -s1

    