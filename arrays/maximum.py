def maximum(arr):
    if len(arr) < 2:
        return None

    maxi = float('-inf')
    secondmax = float('-inf')

    for i in range(len(arr)):
        if arr[i] > maxi:
            secondmax = maxi
            maxi = arr[i]
        elif arr[i] > secondmax and arr[i] != maxi:
            secondmax = arr[i]

    if secondmax == float('-inf'):
        return None

    return secondmax
print(maximum([1,3,4,5,6]))
        