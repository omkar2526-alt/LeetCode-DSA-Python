# https://leetcode.com/problems/valid-anagram/  

# s = "anagram"
# t = "nagaram"

s = input()
t = input()

#  BY USING HASH MAP
def validAnagram(s,t):
    freq = {}
    res = True
    
    if len(s) != len(t):
        res = False
    
    for i in s:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    
    for word in t:
        if word not in freq:
            res = False
            break
        
        freq[word] -= 1
        
        if freq[word] < 0:
            res = False
            break
    
    return res

print(validAnagram(s,t))


# WITHOUT USING HASH MAP

def valid_anagram(s,t):
    
    res = True
    
    if len(s) != len(t):
        res = False
        
    if sorted(s) != sorted(t):
        res = False
    
    return res
    
    
print(valid_anagram(s,t))
        
            