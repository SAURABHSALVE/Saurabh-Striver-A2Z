def lowerbound(arr,x):
    low = 0 
    high = len(arr)-1 
    n = len(arr)
    ans = n 
    while low <= high:
        
        mid = (low + high)//2 
        
        if arr[mid]>=x:
            ans = mid 
            high = mid -1 
        else:
            low = mid + 1 
    return ans
print(lowerbound([1,2,3,4,5],4))
            
    