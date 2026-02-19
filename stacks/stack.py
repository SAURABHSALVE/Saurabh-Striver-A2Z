class Stack:
    def __init__(self):
        self.stack = []
    
    def isEmpty(self):
        return len(self.stack) == 0
    def push(self, data):
        self.stack.append(data)
    def pop(self):
        if self.isEmpty():
            print("Stack is empty")
        else:
            return self.stack.pop()
    def traverse(self):
        for item in self.stack:
            print(item)
    
s = Stack()
s.push(10)
s.push(20)
s.push(30)
s.pop()
s.traverse()