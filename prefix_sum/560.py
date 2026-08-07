# https://leetcode.com/problems/subarray-sum-equals-k/ 

# nums = [1,1,1]
# k = 2

nums = list(map(int,input().split()))
k = int(input())

def subArraySum(nums,k):
    count = 0
    curr_sum = 0
    prefix_count = {0:1}
    
    for num in nums:
        curr_sum += num
        need = curr_sum - k
        
        if need in prefix_count:
            count += prefix_count[need]
        
        prefix_count[curr_sum] += prefix_count.get(curr_sum,0) + 1
        
    return count

print(subArraySum(nums,k))