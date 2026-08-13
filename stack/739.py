
# https://leetcode.com/problems/daily-temperatures/

# temperatures = [73,74,75,71,69,72,76,73]

temperatures = list(map(int,input().split()))

def dailyTemperatures(temperatures):
    n = len(temperatures)
    ans = [0] * n
    stack = []
    
    for i in range(len(n)):
        while stack and temperatures[stack[-1]] < temperatures[i]:
            temp = stack.pop()
            ans[temp] = i - temp
        stack.append(i)
        
    return ans
    
print(dailyTemperatures(temperatures))