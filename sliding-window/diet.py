"""
Problem Statement: Diet Plan Performance
A dieter consumes calories[i] calories on the i-th day. For every consecutive sequence of k days, they evaluate their performance:

Calculate the Total Calories for that window of k days.

If Total < lower: They lose 1 point (-1).

If Total > upper: They gain 1 point (+1).

Otherwise: 0 points.

You need to return the total points the dieter has at the end of all possible k day windows."""


class Solution:
    def dietPlanPerformance(self, calories, k, lower, upper):
        i = 0
        j = 0
        curr_sum = 0
        total_points = 0
        
        while j < len(calories):
            # 1. Add logic: Increase the current window sum
            curr_sum += calories[j]
            
            # If window hasn't reached size K yet
            if j - i + 1 < k:
                j += 1
                
            # If window is exactly size K
            elif j - i + 1 == k:
                # 2. Update Points logic (Evaluate the current window)
                if curr_sum < lower:
                    total_points -= 1
                elif curr_sum > upper:
                    total_points += 1
                
                # 3. Subtract logic: Remove the leftmost element before sliding
                curr_sum -= calories[i]
                
                # 4. Slide the window
                i += 1
                j += 1
                
        return total_points

# --- SAMPLE CALLING (Driver Code) ---

# Creating an instance of the class
sol = Solution()

# Case 1: Standard case
cal1 = [1, 2, 3, 4, 5]
k1, lower1, upper1 = 1, 3, 3
print(f"Test Case 1: {sol.dietPlanPerformance(cal1, k1, lower1, upper1)}") 
# Window size 1: [1], [2], [3], [4], [5]
# Sums: 1(<3), 2(<3), 3(==), 4(>3), 5(>3)
# Points: -1, -1, 0, +1, +1 = 0

# Case 2: Multi-day window
cal2 = [6, 5, 0, 0]
k2, lower2, upper2 = 2, 1, 5
print(f"Test Case 2: {sol.dietPlanPerformance(cal2, k2, lower2, upper2)}")
# Window size 2: [6,5], [5,0], [0,0]
# Sums: 11(>5), 5(==), 0(<1)
# Points: +1, 0, -1 = 0