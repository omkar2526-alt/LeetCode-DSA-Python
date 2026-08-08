# https://leetcode.com/problems/group-anagrams/ 

# strs = ["eat","tea","tan","ate","nat","bat"]

strs = list(map(input().split(",")))

def groupAnagrams(strs):
    freq = {}
    
    for word in strs:
        key = "".join(sorted(word))
        
        if key not in freq:
            freq[key] = []
        
        freq[key].append(word)
        
    return list(freq.values())
    
print(groupAnagrams(strs))