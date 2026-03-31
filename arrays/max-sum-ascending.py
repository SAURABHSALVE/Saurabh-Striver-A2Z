def maxascsum(arr):
    if not arr:
        return 0 
    max_sum = arr[0]
    current_sum = arr[0]
    
    for i in range(1,len(arr)):
        if arr[i] > arr[i-1]:
            current_sum += arr[i]
        else:
            current_sum = arr[i]
        max_sum = max(max_sum, current_sum)
        
            
    return max_sum

## examples
print(maxascsum([1, 2, 3, 4, 5]))
print(maxascsum([1, 2, 3, 2, 5]))

        