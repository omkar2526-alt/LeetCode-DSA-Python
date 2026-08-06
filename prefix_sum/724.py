# https://leetcode.com/problems/find-pivot-index/

nums = list(map(int,input().split(",")))

def pivotIndex(nums):
    left_sum = 0
    total_sum = 0
    right_sum = 0
    res = 0
    
    for i in range(len(nums)):
        total_sum += nums[i]
    
    for i in range(len(nums)):
        right_sum = total_sum - left_sum - nums[i]
        
        if left_sum == right_sum:
            res = i
            break
        left_sum += nums[i]
    
    return res

print(pivotIndex(nums))