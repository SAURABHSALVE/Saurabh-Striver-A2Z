class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        # Step 1: Find the middle using slow and fast
        fast = head 
        slow = head 
        while fast and fast.next:
            fast = fast.next.next 
            slow = slow.next 

        # Step 2: Reverse the second half
        prev = None 
        # Use 'slow' as your 'curr' since it's already at the middle
        while slow:
            nxt = slow.next    # Save the next node
            slow.next = prev   # REVERSE: Point current node backward
            prev = slow        # Move prev forward
            slow = nxt         # Move slow forward
        
        # Step 3: Compare left (start) and right (reversed end)
        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            left = left.next 
            right = right.next 
            
        return True