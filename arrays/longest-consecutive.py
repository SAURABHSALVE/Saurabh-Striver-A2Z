class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Convert list to a set for O(1) lookups
        num_set = set(nums)
        longest = 0
        
        for num in num_set:
            # Check if this number is the START of a sequence.
            # It's a start if the number right before it doesn't exist.
            if (num - 1) not in num_set:
                curr_length = 1
                
                # Keep checking for the next consecutive numbers
                while (num + curr_length) in num_set:
                    curr_length += 1
                    
                # Update the longest sequence found so far
                longest = max(longest, curr_length)
                
        return longest 



def longest(arr):
    if len(arr) == 0:
        return 0 

    longest = 1 
    mini = float('inf')
    cnt = 0
    for i in range(len(arr)):
        if arr[i] - 1 == mini:
            cnt +=1 
            mini = arr[i]
        elif arr[i]!=mini:
            cnt = 1 
            mini = arr[i]
        longest = max(longest, cnt)
    return longest 

