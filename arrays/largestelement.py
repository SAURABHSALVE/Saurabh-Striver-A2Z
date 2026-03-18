def secondlargest(arr):
    n = len(arr)
    largest = float('-inf')
    second = float('-inf')
    for i in range(n):
        if arr[i] > largest:
            second = largest
            largest = arr[i]
        elif arr[i] > second and arr[i] != largest:
            second = arr[i]
    return second 
            
  
print(secondlargest([1,2,3,4,5]))
            
                
                