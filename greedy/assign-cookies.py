def childrens(g, s):
    g.sort()
    s.sort()
    l = 0  # Pointer for children
    r = 0  # Pointer for cookies
    
    while l < len(g) and r < len(s):
        # If the current cookie is large enough for the current child
        if s[r] >= g[l]: 
            l += 1  # Move to the next child (this one is satisfied)
        
        r += 1  # Always move to the next cookie
    return l 

print(childrens([1,3,3,4,5],[1,1,2,2,3,4]))