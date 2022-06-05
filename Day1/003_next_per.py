def nextPermutation(self, nums):
    print('num is ', nums)
    print('sorted nums is ', sorted(nums, reverse=True) )
    if nums == sorted(nums, reverse=True): return sorted(nums)
    j = len(nums)-1
    while j>=1:
        if nums[j]<=nums[j-1]:
            j -=1
        if nums[j] >nums[j-1]:
            nums[j], nums[j-1] = nums[j-1], nums[j]
            #now we wanna maintain the increaing order
            # mainly we wanna sort the nums[j:] part
            # how to sort?
            nums[:j+1].extend(sorted([nums[j+1:]]))
            break
    return nums


# first attempt: failed(5June)