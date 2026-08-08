# https://leetcode.com/problems/top-k-frequent-elements/ 
# nums = [1,1,1,2,2,3]
# k = 2

nums = list(map(int,input().split(",")))
k = int(input())

def topFrequentElements(k,nums):
    freq = {}

    for i in range(len(nums)):
        if nums[i] in freq:
            freq[nums[i]] += 1
        else:    
            freq[nums[i]] = 1
        

    sorted_items = sorted(freq.items(), key=lambda x: x[1], reverse=True)

    result = []

    for i in range(k):
        result.append(sorted_items[i][0])
        
    return result

print(topFrequentElements())