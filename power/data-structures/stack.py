class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return print("is_empty():", self.items == [])

    def push(self, item):
        print("push():", item)
        self.items.append(item)

    def pop(self):
        return print("pop():", self.items.pop())

    def peek(self):
        return print("peek():", self.items[len(self.items)-1])

    def size(self):
        return print("size():", len(self.items))

    def showcase(self):
        return print("showcase():", self.items)

stack = Stack()
stack.is_empty()
stack.showcase()
stack.push(4)
stack.showcase()
stack.push('dog')
stack.showcase()
stack.peek()
stack.showcase()
stack.push(True)
stack.showcase()
stack.size()
stack.showcase()
stack.is_empty()
stack.showcase()
stack.push(8.4)
stack.showcase()
stack.pop()
stack.showcase()
stack.pop()
stack.showcase()
stack.size()
stack.showcase()

"""
is_empty(): True
showcase(): []
push(): 4
showcase(): [4]
push(): dog
showcase(): [4, 'dog']
peek(): dog
showcase(): [4, 'dog']
push(): True
showcase(): [4, 'dog', True]
size(): 3
showcase(): [4, 'dog', True]
is_empty(): False
showcase(): [4, 'dog', True]
push(): 8.4
showcase(): [4, 'dog', True, 8.4]
pop(): 8.4
showcase(): [4, 'dog', True]
pop(): True
showcase(): [4, 'dog']
size(): 2
showcase(): [4, 'dog']
"""