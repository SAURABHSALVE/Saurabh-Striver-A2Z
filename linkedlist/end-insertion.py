'''    
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    def insertAtEnd(self, head, x):
        #code here 
        temp = Node(x)
        if head is None:
            return temp 
        node = head 
        while node.next:
            node = node.next 
        node.next = temp 
        
        return head