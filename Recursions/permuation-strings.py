def permutation(s):
    ans = ""
    helper(list(s),0,ans)
    return ans
def helper(s,idx,ans):
    if idx == len(s):
        print("".join(s))
        return
    for i in range(idx,len(s)):
        s[idx],s[i] = s[i],s[idx]
        helper(s,idx+1,ans)
        s[idx],s[i] = s[i],s[idx]
print(permutation("abc")) ## output: abc, acb, bac, bca, cba, cab

### python command to run is python Recursions/permuation-strings.py