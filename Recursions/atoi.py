"""Problem: Implement the `myAtoi` function that converts a string 
to a 32-bit signed integer (similar to C/C++'s `atoi` function).
"""

### example:
# Input: s = "   -42"
# Output: -42

## EXAMPLE 2:
# Input: s = "4193 with words"
# Output: 4193

INT_MIN = -2**31
INT_MAX = 2**31 - 1


def helper(s,i,num,sign):
    if i >= len(s) or not s[i].isdigit():   ###BASE CASE: if we have reached the end of the string or the current character is not a digit, return the result
        return sign*num
    num = num*10 + int(s[i]) ## Update the number by shifting 
    #the previous digits to the left and adding the new digit
    if sign*num <= INT_MIN : return INT_MIN
    if sign*num >= INT_MAX : return INT_MAX 

    return helper(s,i+1,num,sign)

def myAtoi(s):
    i = 0
    while i < len(s) and s[i] == ' ':
        i += 1
    sign = 1 
    if i < len(s) and (s[i] == '+' or s[i] == '-'):
        sign = -1 if s[i] == '-'else 1
        i +=1
    ## recursive call
    return helper(s,i,0,sign)

    
if __name__ == "__main__":
    s = "  -12345"
    result = myAtoi(s)  ## OUTPUT: -12345
    print(f"Input: '{s}'")
    print(f"Output: {result}")