# /number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/
# arr = [2, 2, 2, 2, 5, 5, 5, 8]
# k = 3
# threshold = 4

arr = list(map(int,input().split(",")))
k = int(input())
threshold = int(input())

def num_of_subarrays(arr,k,threshold):
    
    
    window_sum =0
    count = 0


    for i in range(k):
        window_sum += arr[i]
        
        
    if window_sum >= k * threshold:
        count += 1

    for i in range(k,len(arr)):
        window_sum += arr[i] - arr[i-k]
        
        
        if window_sum >= k* threshold:
            count += 1
            
    return (count)
    
print(num_of_subarrays(arr,k,threshold))
