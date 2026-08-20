nums1 = list(map(int,input().split()))
nums2 = list(map(int,input().split()))

def intersectionII(nums1,nums2):
    count = {}

    for i in nums1:
        count[i] = count.get(i,0) + 1
    
    result = []
    for i in nums2:
        if i in count:
            if count[i] > 0:
                result.append(i)
                count[i] -= 1
    return result

print(intersectionII(nums1,nums2))