# https://leetcode.com/problems/longest-repeating-character-replacement/ 
# s = "AABABBA"
# k = 1

k = int(input())
s = input()

def longestRepeatingCharacter(k,s):
    left = 0
    freq = {}
    max_freq = 0
    max_length = 0
    for i in range(len(s)):
        ch = s[i]
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1
        max_freq = max(max_freq,freq[ch])
        window_length = i - left + 1
        
        if window_length - max_freq > k:
            freq[s[left]] -= 1
            left += 1
        max_length = max(max_length,i - left + 1)
    return max_length

print(longestRepeatingCharacter(k,s))
        

