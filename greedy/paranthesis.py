def paranethesis(s):
    low = 0 
    high = 0
    for i in s:
        if s[i] == '(':
            low +=1 
            high += 1 
        elif s[i] == ')':
            low -= 1 
            high -= 1
        elif s[i] == '*':
            low -= 1 
            high += 1
        if high < 0:
            return False
        if low < 0:
            low = 0 
    return low == 0
print(paranethesis("(*)")) ### answer is True
print(paranethesis("(*))")) ### answer is True
          
## added the code 