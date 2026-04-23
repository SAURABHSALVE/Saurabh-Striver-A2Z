class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        # Hash map to store the 'Next Greater Element' (NGE) for each number in nums2
        # Key: element, Value: its next greater element
        nge_map = {}
        stack = []

        # Step 1: Traverse nums2 from right to left
        # We go backwards because we need to know what's to the right of each element
        for i in range(len(nums2) - 1, -1, -1):
            current = nums2[i]
            
            # Step 2: Maintenance of the Monotonic Stack
            # While the top of the stack is smaller than or equal to the current element, 
            # it can't be the "next greater" for anything to the left. Pop it.
            while stack and stack[-1] <= current:
                stack.pop()
            
            # Step 3: Determine the NGE
            # If the stack is empty after popping, there is no greater element to the right.
            if not stack:
                nge_map[current] = -1
            else:
                # The top element is the first one to the right that survived the pop, 
                # meaning it is strictly greater than our current element.
                nge_map[current] = stack[-1]
            
            # Step 4: Push the current element onto the stack
            # It might be the "next greater" for elements sitting to its left.
            stack.append(current)

        # Step 5: Final construction
        # Use the map to answer the query for nums1 in O(1) time per element.
        return [nge_map[num] for num in nums1]