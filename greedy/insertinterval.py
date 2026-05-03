class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        res = []
        i = 0 
        n = len(intervals)
        
        # 1. Add all intervals that end before the newInterval starts
        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1 
            
        # 2. Merge overlapping intervals into newInterval
        while i < n and intervals[i][0] <= newInterval[1]:
            # Update the start and end of the newInterval based on overlaps
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1 
        
        # Add the final merged version of newInterval
        res.append(newInterval)
        
        # 3. Add all remaining intervals that start after newInterval ends
        while i < n:
            res.append(intervals[i])
            i += 1 
            
        return res

# Main driver code
if __name__ == "__main__":
    # Input data
    intervals = [[1,3],[6,9]]
    newInterval = [2,5]

    # Initialize solution and get results
    sol = Solution()
    res = sol.insert(intervals, newInterval)
    
    # Expected output: [[1,5],[6,9]]
    print(res)
    
    
    ### command to run is  python greedy/insertinterval.py
    