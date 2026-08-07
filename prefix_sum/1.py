#https://leetcode.com/problems/two-sum/
# nums = [3,2,4]
# target = 6

nums = list(map(int,input().split(",")))
target = int(input())

def twoSum(nums,target):
    freq = {}
    
    for i in range(len(nums)):
        num = nums[i]
        need = target - num
        
        if need in freq:
            return [freq[need],i]     
        
        freq[num] = i
        # {3:0}, {2:1}
        
    