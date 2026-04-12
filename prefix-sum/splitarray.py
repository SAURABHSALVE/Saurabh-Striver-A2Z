def split(nums):
    
    # 1. Pre-calculate the total sum
    total = sum(nums)
    left_sum = 0 
    splits = 0 
    
    
    # 2. Iterate until n-2 (cannot split at the very last index)
    for i in range(len(nums)):
        left_sum += nums[i] 
        # Right_sum is whatever is left over
        right_sum = total - left_sum
        
        # 3. Check the condition
        if left_sum >= right_sum:
            splits +=1 
    return splits 
print(split([1,2,3,4,5,6]))