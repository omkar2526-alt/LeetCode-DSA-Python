# nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
# k = 2

nums = list(map(int,input().split(",")))
k = int(input())

def MaxConsecutiveOnesIII(nums,k):
    left = 0
    max_length = 0
    zero_count = 0
    
    for i in range(len(nums)):
        if nums[i] == 0:
            zero_count += 1
        
        while zero_count > k :
            if nums[i] == 0 :
                zero_count -= 1
            left += 1
        
        window_length = i - left + 1
        max_length = max(max_length,window_length)
                
    return max_length

print(MaxConsecutiveOnesIII(nums,k))