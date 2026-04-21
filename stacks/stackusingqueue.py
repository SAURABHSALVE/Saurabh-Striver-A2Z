from collections import deque

class MyStack(object):

    def __init__(self):
        # Initialize an empty deque to act as our queue
        self.q = deque()

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        # A simple append to the right end of the queue
        self.q.append(x)

    def pop(self):
        """
        :rtype: int
        """
        # Rotate the queue: move all elements except the last one to the back
        # This makes the last-pushed element the next one to be dequeued (FIFO)
        for i in range(len(self.q) - 1):
            self.q.append(self.q.popleft())
        
        # Now the front of the queue is the "top" of our stack
        return self.q.popleft()

    def top(self):
        """
        :rtype: int
        """
        # Return the last element added without removing it
        return self.q[-1]

    def empty(self):
        """
        :rtype: bool
        """
        # Return True if the queue is empty, False otherwise
        return len(self.q) == 0
