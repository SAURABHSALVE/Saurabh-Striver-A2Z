def smallest(arr):
    n = len(arr)

    if n == 0:
        return None
    if n < 2:
        return None

    mini = float('inf')
    second = float('inf')

    for i in range(n):
        if arr[i] < mini:
            second = mini
            mini = arr[i]
        elif arr[i] < second and arr[i] != mini:
            second = arr[i]

    if second == float('inf'):
        return None

    return second


print(smallest([4]))