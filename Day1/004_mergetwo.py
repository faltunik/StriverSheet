# questions statement
# problem statement: https://www.codingninjas.com/codestudio/problems/ninja-and-sorted-arrays_1214628?topList=striver-sde-sheet-problems

def mergetwo(arr1, arr2, m,n):
    s, e = 0, m
    for num in arr2:
        tmp = help(s,e,arr1,num)
        arr1.insert(tmp,num)
        s,e = tmp, m+1
    return arr1[:m+n]


def help(s,e,arr,n):
    m = (s+e)//2
    while s<=e:
        if arr[m] <= n <= arr[m+1]:
            return m+1
        elif arr[m] > n:
            e = m-1
        else:
            s = m+1
    return -1

if __name__ == '__main__':
    t = int(input('enter nu of test cases: '))
    for _ in range(t):
        m,n = list(map(int, input.split()))
        arr1 = list(map(int, input.split()))
        arr2 = list(map(int, input.split()))
        print(mergetwo(arr1, arr2, m,n))


# got tle and I am not sure about solution
# first attempt: failed (5June)
