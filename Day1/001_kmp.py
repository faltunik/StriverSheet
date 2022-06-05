def findPattern(s:str, p:str):
    return p in s

if __name__ == '__main__':
    t = int(input('enter nu of test cases: '))
    print('t is ', {t})
    for _ in range(t):
        p, s = input('Enter Both string: ').split()
        print(findPattern(s,p))


# so I failed to solve this problem as I wast not able to understand how to read input
# result
# 1st attempt: Failed (5June)

