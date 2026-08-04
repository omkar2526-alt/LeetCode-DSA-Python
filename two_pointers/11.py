# height = [1, 8, 6, 2, 5, 4, 8, 3, 7]

height = list(map(int,input().split(",")))

def container_with_most_water(height):

    left = 0
    right = len(height) - 1
    width = abs(right-left)
    max_area = 0

    while right>left:
        width = abs(right-left)
        area = width * min(height[left],height[right])
        
        if area > max_area:
            max_area = area 
        
        if height[left] <= height[right]:
            left += 1
            
        else:
            right -=1

    return (max_area)  
    
print(container_with_most_water(height))