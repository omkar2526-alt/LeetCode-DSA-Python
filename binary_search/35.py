

# ,https://leetcode.com/problems/search-insert-position/

# nums = [-1,0,3,5,9,12]
# target = 9

nums = list(map(int,input().split()))
target = int(input())

def search_insert(nums,target):
    left = 0
    right = len(nums)-1
    res = -1

    while right > left:
        mid = (left + right) // 2
        
        if nums[mid] == target:
            return mid
        
        elif nums[mid] > target :
            right = mid - 1
        else:
            left = mid + 1
            
    return left

print(search_insert(nums,target))