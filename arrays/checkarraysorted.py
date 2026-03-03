# def checkarray(arr):
#     n = len(arr)
#     for i in range(n):
#         for j in range(i + 1,n):
#             if arr[j] < arr[i]:
#                 return False
    
#     return True 
# print(checkarray([12,3,4,5]))
            
        
def checkarray(arr):
    n = len(arr)
    for i in range(1,n):
        if arr[i] < arr[i-1]:
            return False
    return True
print(checkarray([1,2,3,4,5]))
