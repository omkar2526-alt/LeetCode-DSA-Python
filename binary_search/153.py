# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

# nums = [3,4,5,1,2]

nums = list(map(int,input().split()))
 

def findMin(nums): 
    left = 0
    right = len(nums) - 1

    while left < right :
        mid = (left + right) // 2
        
        if nums[mid] > nums[right]:
            left = mid + 1
        
        else:
            right = mid
        
    return (nums[right])

print(findMin(nums))