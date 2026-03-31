def removeelement(arr,val):
    k = 0 
    for i in range(len(arr)):
        if arr[i] != val:
            arr[k] = arr[i]
            k += 1
    return k
## examples 
print(removeelement([3,2,2,3],3))
print(removeelement([0,1,2,2,3,0,4,2],2))

