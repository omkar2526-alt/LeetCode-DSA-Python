# https://leetcode.com/problems/minimum-size-subarray-sum/
# target = 7
# nums = [2, 3, 1, 2, 4, 3]


nums = list(map(int,input().split(",")))
target = int(input())

def minSubArrayLen(nums,target):
    left = 0
    min_length = float("inf")
    window_sum = 0
    res = 0
    for i in range(len(nums)):
        window_sum += nums[i]
        
        while window_sum >= target:
            window_length = i - left + 1
            min_length = min(min_length,window_length)
            window_sum -= nums[left]
            left += 1
    
    if min_length == float("inf"):
        res = 0
    else:
        res = min_length
        
    return min_length

print(minSubArrayLen(nums,target))  