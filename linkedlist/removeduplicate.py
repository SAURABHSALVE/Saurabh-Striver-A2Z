class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # If the list is empty or has one node, no duplicates possible
        if not head:
            return head
        
        curr = head
        
        # We need to check curr.next because we are comparing curr with its neighbor
        while curr and curr.next:
            if curr.val == curr.next.val:
                # FOUND A DUPLICATE! 
                # Skip the next node by pointing to the one after it
                curr.next = curr.next.next
            else:
                # NO DUPLICATE: Just move forward
                curr = curr.next
                
        return head