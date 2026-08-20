nums = list(map(int,input().split()))

def moveZero(nums):
    n= len(nums)
    l = 0
    for i in range(n):
        if nums[i] == 0:
            continue
        nums[l],nums[i] = nums[i],nums[l]
        l += 1
        
    return nums