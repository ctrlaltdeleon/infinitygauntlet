class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def showcase(self):
        return self.items


q = Queue()

print(q.isEmpty())
q.enqueue('hello')
q.enqueue('dog')
q.enqueue(3)
print(q.dequeue())
print(q.showcase())
