"""
@author: acfromspace
"""


class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return print("is_empty():", self.items == [])

    def enqueue(self, item):
        print("enqueue():", item)
        self.items.insert(0, item)

    def dequeue(self):
        return print("dequeue():", self.items.pop())

    def size(self):
        return print("size():", len(self.items))

    def showcase(self):
        return print("showcase():", self.items)


queue = Queue()
queue.is_empty()
queue.showcase()
queue.enqueue('hello')
queue.showcase()
queue.enqueue('dog')
queue.showcase()
queue.enqueue(5)
queue.showcase()
queue.size()
queue.showcase()
queue.dequeue()
queue.showcase()

"""
Output:

is_empty(): True
showcase(): []
enqueue(): hello
showcase(): ['hello']
enqueue(): dog
showcase(): ['dog', 'hello']
enqueue(): 5
showcase(): [5, 'dog', 'hello']
size(): 3
showcase(): [5, 'dog', 'hello']
dequeue(): hello
showcase(): [5, 'dog']
"""
