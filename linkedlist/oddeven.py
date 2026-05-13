class Solution(object):
    def oddEvenList(self, head):
        # If the list is empty or has only one node, just return it
        if not head or not head.next:
            return head
        
        odd = head          # The 1st node
        even = head.next     # The 2nd node
        even_head = even     # We need to remember where the even list starts!
        
        # We loop as long as there are even nodes to process
        while even and even.next:
            # 1. Connect current odd node to the next odd node (skip the even one)
            odd.next = even.next
            odd = odd.next
            
            # 2. Connect current even node to the next even node (skip the odd one)
            even.next = odd.next
            even = even.next
            
        # 3. Final step: Connect the end of the odd list to the start of the even list
        odd.next = even_head
        
        return head