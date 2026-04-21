class MinStack(object):

    def __init__(self):
        # Stores all elements
        self.stack = []
        # Stores the minimum value at each stack level
        self.min_stack = []

    def push(self, val):
        self.stack.append(val)
        # If min_stack is empty, current val is the min
        # Otherwise, the new min is the smaller of val and the current top min
        if not self.min_stack:
            self.min_stack.append(val)
        else:
            current_min = self.min_stack[-1]
            self.min_stack.append(min(val, current_min))

    def pop(self):
        self.stack.pop()
        self.min_stack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        # Now returns in O(1) time
        return self.min_stack[-1]
    
    
    
    
#     class MinStack(object):

#     def __init__(self):
#         self.s = []
        

#     def push(self, val):
#         """
#         :type val: int
#         :rtype: None
#         """
#         self.s.append(val)
        

#     def pop(self):
#         """
#         :rtype: None
#         """
#         self.s.pop()
        

#     def top(self):
#         """
#         :rtype: int
#         """
#         return self.s[-1]
        

#     def getMin(self):
#         """
#         :rtype: int
#         """
#         return min(self.s)
        


# # Your MinStack object will be instantiated and called as such:
# # obj = MinStack()
# # obj.push(val)
# # obj.pop()
# # param_3 = obj.top()
# # param_4 = obj.getMin()
