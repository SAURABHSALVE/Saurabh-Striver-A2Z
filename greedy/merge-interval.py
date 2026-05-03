def merge(intervals):
    if not intervals:
        return []

    # 1. Sort by the start time
    intervals.sort(key=lambda x: x[0])
    
    ans = []
    i = 0 
    n = len(intervals)
    
    while i < n:
        start = intervals[i][0]
        end = intervals[i][1]  # FIX: Initialize 'end' with the current interval's end
        
        j = i + 1
        # FIX: Check if the NEXT interval (j) starts before the current 'end'
        while j < n and intervals[j][0] <= end:
            # FIX: Update 'end' using the overlapping interval's end
            end = max(end, intervals[j][1])
            j += 1 
        
        ans.append([start, end])
        i = j  # Move 'i' to the next non-overlapping interval
        
    return ans

# Test case
print(merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
# Expected Output: [[1, 6], [8, 10], [15, 18]]