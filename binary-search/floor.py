def floor(arr,target):
    n = len(arr)
    low = 0 
    high = n -1 
    ans = -1 
    while low <= high:
        mid = (low + high)//2 
        
        if arr[mid] <= target:
            ans = mid 
            low = mid + 1
        else:
            high = mid - 1 
    return ans
print(floor([1,2,3,4,5,6,7],6))  # Output: 5 (index of 6)
    