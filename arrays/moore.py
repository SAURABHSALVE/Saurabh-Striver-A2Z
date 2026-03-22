def majorityElement(arr):

    n = len(arr)
    candidate = -1
    count = 0

    # Find a candidate
    for num in arr:
        if count == 0:
            candidate = num
            count = 1
        elif num == candidate:
            count += 1
        else:
            count -= 1

    # Validate the candidate
    count = 0
    for num in arr:
        if num == candidate:
            count += 1

    # If count is greater than n / 2, return 
    # the candidate; otherwise, return -1
    if count > n // 2:
        return candidate
    else:
        return -1

if __name__ == "__main__":
    
    arr = [1, 1, 2, 1, 3, 5, 1]
    print(majorityElement(arr))  # Output: 1