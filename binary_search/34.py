# nums = [5,7,7,8,8,10],
# target = 8

def searchRange(nums,target):
    first = -1
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            first = mid
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
        
    left = 0
    right = len(nums) - 1
    second = -1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            second = mid
            left  = mid + 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return [first,second]