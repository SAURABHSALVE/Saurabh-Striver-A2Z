# Class to hold solution logic
class Solution:
    # Function to find the maximum number of meetings
    def maxMeetings(self, start, end):
        # Store as (end_time, start_time, original_index)
        # Using 0-based indexing to match your expected output [0, 1, 3]
        meetings = [(end[i], start[i], i) for i in range(len(start))]

        # Sort meetings based on their end times (Greedy approach)
        meetings.sort()

        result = []
        last_end = -1

        # Iterate through the sorted meetings
        for e, s, idx in meetings:
            # If the start time is greater than the last meeting's end time
            if s > last_end:
                # Add the 0-based index to result
                result.append(idx)
                # Update the end time of the last scheduled meeting
                last_end = e
                
        return result


# Main driver code
if __name__ == "__main__":
    # Input data
    start = [1, 3, 0, 5]
    end   = [2, 4, 6, 7]

    # Initialize solution and get results
    sol = Solution()
    res = sol.maxMeetings(start, end)
    
    # Expected output: [0, 1, 3]
    print(res)
    
    
    ### command to run is  python greedy/Nmeeting.py
    
    
class Solution:
    # Function to find the maximum number of meetings that can
    # be performed in a meeting room.
    def maximumMeetings(self, start, end):
        # 1. Pair start and end times together
        # We store them as (end, start) because sorting tuples 
        # defaults to the first element.
        meetings = []
        for i in range(len(start)):
            meetings.append((end[i], start[i]))
        
        # 2. Sort meetings by their end times
        meetings.sort()
        
        count = 0
        last_end_time = -1
        
        # 3. Iterate through sorted meetings
        for current_end, current_start in meetings:
            # If the current meeting starts AFTER the last one ended
            if current_start > last_end_time:
                count += 1
                last_end_time = current_end
                
        return count