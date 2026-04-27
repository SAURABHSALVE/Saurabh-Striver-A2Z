def childrens(g,s):
    g.sort()
    s.sort()
    i = 0 
    j = 0 
    while i < len(g) and j < len(s):
        if g[i] <= s[j]:
            i+=1 
        j+=1 
    return i
print(childrens([1,2,3],[1,1]))
### command to run:  python greedy/assign-cookies.py