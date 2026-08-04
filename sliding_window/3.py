s = input()

def lengthOfLongestSubString(s):
    left = 0
    seen = set()
    count = 0
    for i in range(len(s)):
        while s[i] in seen:
            seen.remove(s[left])
            left += 1
        seen.add(s[left])
        count = max(count,len(seen))
    return count

print(lengthOfLongestSubString(s))