g = list(map(int,input().split()))
s = list(map(int,input().split()))


def assignCookie(g,s):
    i = 0
    leng = len(g)
    count = 0

    g.sort()
    s.sort()
        
    count = 0

    for j in range(len(s)):
        if leng > count and s[j] >= g[count]:
            count += 1
                    
    return count
    

print(assignCookie(g,s))