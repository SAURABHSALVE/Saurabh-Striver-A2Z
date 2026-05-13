class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return None # LeetCode expects None, not -1, if no cycle exists
        
        slow = head
        fast = head
        
        # Phase 1: Find the meeting point
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                # Phase 2: Find the cycle start
                fast = head # Reset one pointer to the start
                while slow != fast:
                    slow = slow.next
                    fast = fast.next # Move BOTH 1 step at a time
                
                return slow # This is now the start of the cycle
                
        return None # No cycle found