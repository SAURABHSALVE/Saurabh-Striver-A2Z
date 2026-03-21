def maximum_subarray_sum(arr):
    maxi = float('-inf')
    sum = 0
    for i in range(len(arr)):
        if sum <0:
            sum = 0
            sum += arr[i]
        else:
            sum += arr[i]
        maxi = max(maxi,sum)
    return maxi 
# Example usage:
arr = [-2,1,-3,4,-1,2,1,-5,4]
print(maximum_subarray_sum(arr))  # Output: 6 (subarray [4,-1,2,1])

## command to run the code
# python maximum-subarray-sum.py