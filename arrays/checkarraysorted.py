# def checkarray(arr):

#     n = len(arr)

#     for i in range(1, n):
        

#         if arr[i] < arr[i-1]:
#             return False

#     return True


# print(checkarray([1,2,3,4,5]))







def checksorted(arr):
    n = len(arr)
    for i in range(1, n):
        # If we find an element smaller than the one before it, it's not sorted
        if arr[i] < arr[i-1]:
            return False 
    # If the loop finishes without returning False, the list is sorted
    return True

print(checksorted([1, 2, 3, 2, 5])) # Returns False
print(checksorted([1, 2, 3, 4, 5])) # Returns True