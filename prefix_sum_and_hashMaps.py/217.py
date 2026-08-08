# https://leetcode.com/problems/contains-duplicate/

nums = list(map(int,input().split(",")))

def containDuplicates(nums):
    num = set(nums)
    
    if len(nums) != len(num):
        return True
     
    return False

print(containDuplicates(nums))