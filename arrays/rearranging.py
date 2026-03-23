def rearrange(arr):
    
    i,j = 0,1
    res = [0] *len(arr)
    for num in arr:
        if num > 0:
            res[i] = num
            i+=2
        else:
            res[j] = num
            j+=2
    return res

# Example usage:
arr = [1, -2, 3, -4, 5, -6]
print(rearrange(arr))  # Output: [1, -2, 3, -4, 5, -6] (positive and negative numbers are rearranged alternately)
## command to run the code:
# python rearranging.py

