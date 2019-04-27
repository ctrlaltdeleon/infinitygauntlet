```py
"""
@author: acfromspace
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class DoublyNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def size(self):
        count = 0
        curr = self.head
        while curr is not None:
            curr = curr.next
            count += 1

    def add_first(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node

    def add_last(self, data):
        node = Node(data)
        if self.tail is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
            self.tail.next = None

    def reverse(self):
        curr = tail = self.head
        prev = None
        while curr is not None:
            self.head = curr
            curr = curr.next
            self.head.next = prev
            prev = self.head

    def showcase(self):
        curr = self.head
        while curr is not None:
            print(curr.data, end=" ")
            curr = curr.next


linked_list = LinkedList()
random_list = [10, 20, 275, 2, 5, 8, 64, 52]
for number in random_list:
    linked_list.add_first(number)
    linked_list.add_last(number*2)
linked_list.showcase()
print("\n")
linked_list.reverse()
linked_list.showcase()

"""
Output:

52 64 8 5 2 275 20 10 20 40 550 4 10 16 128 104

104 128 16 10 4 550 40 20 10 20 275 2 5 8 64 52
"""
```
