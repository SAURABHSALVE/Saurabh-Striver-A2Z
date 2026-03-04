def maximum(arr):
    n = len(arr)
    maxi = arr[0]
    for i in range(n):
        if arr[i] > maxi:
            maxi = arr[i]
    
    second = arr[0]
    for i in range(n):
        if arr[i] > second and arr[i]!=maxi:
            second = arr[i]
    
    return second
print(maximum([1,2,4,4,5]))