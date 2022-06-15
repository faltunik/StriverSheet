# https://www.codingninjas.com/codestudio/problems/find-minimum-number-of-coins_975277?topList=striver-sde-sheet-problems


denominations = [1, 2, 5, 10, 20, 50, 100, 500, 1000]
n = len(denominations)


def findMinimumCoins(amount):
    k = n-1
    c = 0
    while amount and k>=0:
        if k>=0 and amount < denominations[k]:
            k -=1
        else:
            amount -= denominations[k]
            c +=1
    return c
        

# followup
# improve time complexity