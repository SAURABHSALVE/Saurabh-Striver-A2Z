class Dequeue:
    def __init__(self):
        self.items = []
    def insert_front(self, item):
        self.items.insert(0, item)
    def insert_rear(self, item):
        self.items.append(item)
    def delete_front(self):
        if not self.items:
            return "Queue is empty"
        return self.items.pop(0)
    def delete_rear(self):
        if not self.items:
            return "Queue is empty"
        return self.items.pop()
d = Dequeue()
d.insert_rear(10)
d.insert_rear(20)
d.insert_front(5)
print(d.delete_front())  # Output: 5
print(d.delete_rear())   # Output: 20
print(d.delete_front())  # Output: 10
print(d.delete_front())  # Output: "Queue is empty"
