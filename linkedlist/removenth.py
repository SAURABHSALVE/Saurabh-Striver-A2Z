class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        # 1. Create a dummy node to handle edge cases (like removing the head)
        dummy = ListNode(0)
        dummy.next = head
        
        fast = dummy
        slow = dummy
        
        # 2. Use a FOR loop to create the gap of size 'n'
        for i in range(n):
            fast = fast.next
            
        # 3. Use a WHILE loop to move the gap to the end of the list
        while fast.next:
            fast = fast.next
            slow = slow.next
            
        # 4. Skip the N-th node
        slow.next = slow.next.next
        
        # 5. Return the new head
        return dummy.next