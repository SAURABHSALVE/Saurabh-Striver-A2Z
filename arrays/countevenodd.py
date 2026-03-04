def countevenodd(arr):
    even = 0
    odd = 0
    for i in range(len(arr)):
        if arr[i] %2== 0:
            even +=1 
        else:
            odd +=1 
        
    
    return [even,odd]
print(countevenodd([1,2,3,4,5]))