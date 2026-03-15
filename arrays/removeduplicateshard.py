def remove_duplicates_twice(arr):

    n = len(arr)

    if n <= 2:
        return n

    i = 2

    for j in range(2, n):

        if arr[j] != arr[i-2]:
            
            arr[i] = arr[j]
            i = i + 1
           

    return i


arr = [1,1,1,2,2,3]

k = remove_duplicates_twice(arr)

print("Length:", k)
print("Array:", arr[:k])