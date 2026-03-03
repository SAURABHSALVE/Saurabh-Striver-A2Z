def secondlargestarray(arr):
    
    n = len(arr)
    max = arr[0]
    for i in range(1,n):
        if arr[i] > max:
            max = arr[i]
    
    secondmax = arr[0]
    for i in range(1,n):
        if arr[i] > secondmax and arr[i] != max:
            secondmax = arr[i]
        
    
    return secondmax 

print(secondlargestarray([1,2,3,4,5]))
        