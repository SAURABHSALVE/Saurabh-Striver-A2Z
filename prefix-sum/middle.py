def middle(arr):
    
    ### [1,2,3,4,5,6] return 
    total =  sum(arr)
    left_sum = 0 
    for i in range(len(arr)):
        
        if left_sum == total - left_sum - arr[i]:
            return i 
        else:
            left_sum += arr[i]
    
    return -1 

print(middle([1,-1,4]))