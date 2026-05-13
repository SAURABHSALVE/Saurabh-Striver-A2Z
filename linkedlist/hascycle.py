class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # If the list is empty or only has one node, it can't have a cycle
        if not head or not head.next:
            return False
            
        slow = head
        fast = head
        
        # We move fast by 2 steps, so we must check fast and fast.next
        while fast and fast.next:
            slow = slow.next          # Move 1 step
            fast = fast.next.next     # Move 2 steps
            
            # If they meet, we found a loop!
            if slow == fast:
                return True
                
        # If the loop ends, fast reached the end, so no cycle exists
        return False