def binary(arr,target):
    low = 0 
    high = len(arr) -1 
    
    while low < high:
        mid = (low + high)// 2 
        
        if arr[mid] == target:
            return mid 
        elif arr[mid] > target:
            high = mid -1 
        elif arr[mid] < target:
            low = mid + 1 
print(binary([1,2,3,4,5,6],5))