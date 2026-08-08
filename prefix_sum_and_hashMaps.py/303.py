# https://leetcode.com/problems/range-sum-query-immutable/
# nums = [-2, 0, 3, -5, 2, -1]

# obj = NumArray(nums)

# print(obj.sumRange(0, 2))  # 1
# print(obj.sumRange(2, 5))  # -1
# print(obj.sumRange(0, 5))  # -3

nums = list(map(int,input().split(",")))
left = int(input())
right = int(input())

def rangeSumQuery(nums):
    prefix = []
    sum = 0
    for i in range(len(nums)):
        sum += nums[i]
        prefix.append(sum)
        
    return prefix



def sumRange(prefix,left,right):
    if left == 0:
        return prefix[right]
    return prefix[right] - prefix[left-1]

prefix = rangeSumQuery(nums)

print(sumRange(prefix,left,right))
        