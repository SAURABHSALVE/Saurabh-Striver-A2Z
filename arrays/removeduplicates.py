def remove(arr):
    i = 0
    n = len
    for j in range(1,n):
        if arr[i] != arr[j]:
            i+=1
        arr[i] = arr[j]
    return i+1
print(remove([1,1,2,2,3,4,5]))

        