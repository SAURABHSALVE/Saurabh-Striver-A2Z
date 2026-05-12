class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.size = 0

    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        # If index is invalid, return -1
        if index < 0 or index >= self.size:
            return -1
        
        curr = self.head
        # Traverse to the specific index
        for _ in range(index):
            curr = curr.next
        return curr.val

    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        new_node = Node(val)
        if not self.head:
            self.head = new_node
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = new_node
        self.size += 1

    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        if index > self.size:
            return
        if index <= 0:
            self.addAtHead(val)
            return
        
        new_node = Node(val)
        curr = self.head
        # Iterate to the node just before the insertion point
        for _ in range(index - 1):
            curr = curr.next
        
        new_node.next = curr.next
        curr.next = new_node
        self.size += 1

    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        if index < 0 or index >= self.size:
            return
        
        curr = self.head
        # If we are deleting the head
        if index == 0:
            self.head = curr.next
        else:
            # Iterate to the node just before the one to delete
            for _ in range(index - 1):
                curr = curr.next
            # Skip the target node
            curr.next = curr.next.next
            
        self.size -= 1