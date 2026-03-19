def palindrome(arr):
    n = len(arr)
    
    loop = n//2
    
    for i in range(loop):
        if arr[i]!=arr[n-i-1]:
            return False
    
    return True 
# print(palindrome([1,2,3,2,1]))
print(palindrome([1,2,3,4,5])) ## not a palindrome
