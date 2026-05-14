class Solution(object):
    def reverseBetween(self, head, left, right):
        if not head or left == right:
            return head
        
        # 1. Use a dummy node to handle 'left=1' case easily
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        
        # 2. Move 'prev' to the node exactly before the reversal starts
        for _ in range(left - 1):
            prev = prev.next
            
        # 3. 'curr' is the first node of the segment to be reversed
        curr = prev.next
        
        # 4. Perform the "Reach and Pull" (right - left) times
        for _ in range(right - left):
            temp = curr.next        # Reach: grab the node to move
            curr.next = temp.next   # Skip over the grabbed node
            temp.next = prev.next   # Point the grabbed node to the current start
            prev.next = temp        # Pull: connect prev to the moved node
            
        return dummy.next