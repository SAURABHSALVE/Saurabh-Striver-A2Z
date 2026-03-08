def array_sum(arr):
    n = len(arr)
    if n ==0:
        return 0
    if n == 1:
        return arr[0]
    sum = 0 
    for i in range(n):
        sum +=arr[i]
    
    return sum 
print(array_sum([1]))
        