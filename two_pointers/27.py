nums = list(map(int,input().split()))
value = int(input())

def removeElement(numsvalue):
    k = 0

    for i in range(len(nums)):
        if nums[i] != value:
            nums[k] = nums[i]
            k +=1
    return k

print(removeElement(nums))