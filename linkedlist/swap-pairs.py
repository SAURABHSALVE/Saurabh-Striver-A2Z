class Solution(object):
    def swapPairs(self, head):
        # Dummy node is our best friend for swapping
        dummy = ListNode(0)
        dummy.next = head
        point = dummy
        
        while point.next and point.next.next:
            # Identify the two nodes to swap
            first = point.next
            second = point.next.next
            
            # Swapping the arrows
            first.next = second.next
            second.next = first
            point.next = second
            
            # Move the pointer two nodes ahead for the next pair
            point = first
            
        return dummy.next
print(Solution.swapPairs([1,2,3,4]))