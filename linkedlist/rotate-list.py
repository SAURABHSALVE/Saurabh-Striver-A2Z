class Solution(object):
    def rotateRight(self, head, k):
        if not head or not head.next or k == 0:
            return head
        
        # 1. Find length and the last node
        last = head
        length = 1
        while last.next:
            last = last.next
            length += 1
            
        # 2. Handle k
        k = k % length
        if k == 0: return head
        
        # 3. Make it circular
        last.next = head
        
        # 4. Find the new tail (length - k - 1) steps from head
        new_tail = head
        for _ in range(length - k - 1):
            new_tail = new_tail.next
            
        # 5. Break the circle
        new_head = new_tail.next
        new_tail.next = None
        
        return new_head