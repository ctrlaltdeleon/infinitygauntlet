"""
@author: acfromspace
"""


class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

    def showcase(self):
        return self.items


stack = Stack()
print(stack.is_empty())
stack.push(4)
stack.push('dog')
print(stack.peek())
stack.push(True)
print(stack.size())
print(stack.is_empty())
stack.push(8.4)
print(stack.pop())
print(stack.pop())
print(stack.size())
