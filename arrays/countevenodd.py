def evenodd(arr):
    n = len(arr)
    even = 0 
    odd = 0 
    for i in range(n):
        if arr[i]%2== 0:
            even +=1
        else:
            odd +=1 
        
    return [even,odd]
print(evenodd([1,2,4,5]))