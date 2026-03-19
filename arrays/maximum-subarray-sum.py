def maximumSubArraySum(arr):
    maxi = float('-inf')
    sum = 0
    n = len(arr)
    for i in range(n):
        if sum <0:
            sum = 0
            sum+=arr[i]
        else:
            sum+=arr[i]
        maxi = max(maxi,sum)
    return maxi

# Example usage:
arr = [-2,1,-3,4,-1,2,1,-5,4]
print(maximumSubArraySum(arr))  # Output: 6 (subarray [4,-1,2,1])
