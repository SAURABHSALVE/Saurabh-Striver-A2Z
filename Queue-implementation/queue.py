### QUEUE
class Queue:
  def __init__(self):
    self.items = []
  
  def isEmpty(self):
    return len(self.items) == 0
  
  def insert(self,data):
    self.items.append(data)
  
  def delete(self):
    ## underflow or not 

    if (self.isEmpty()):
      print("queue is empty")
    
    else:
      return self.items.pop(0)
q = Queue()
q.insert(10)
q.insert(20)
q.insert(30)
print(q.delete())
print(q.delete()) 
print(q.delete())
print(q.delete())  
