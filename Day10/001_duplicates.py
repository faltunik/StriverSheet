# easy
# https://www.codingninjas.com/codestudio/problems/remove-duplicates-from-sorted-array_1102307?topList=striver-sde-sheet-problems



# bruteforce- O(n)
def removeDuplicates(arr,n):
    # Write your code here.
    c = 1
    prev = arr[0]
    for i in arr[1:]:
        if i ==prev:
            continue
        c +=1
        prev = i
    return c

# since length of arrisalready given,so we can improve time complexity of our solution
# arr is sorted as well
# so, maybe, we can do binary search
# but I don't understand how binary searcg will help?