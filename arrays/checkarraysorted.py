def checkarray(arr):
    n = len(arr)
    
    for i in range(1, n):
        if arr[i] < arr[i-1]:
            return False
            
    return True

print(checkarray([1,2,3,4]))