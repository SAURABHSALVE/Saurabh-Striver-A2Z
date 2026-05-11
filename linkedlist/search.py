'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    def searchKey(self, head, key):
        #Code here
        
        node = head
        while node:
            if node.data == key:
                return True 
            node = node.next
        return False
            