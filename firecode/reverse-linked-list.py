"""
@author: acfromspace
"""


class Node:
    def __init__(self):
        self.data = None
        self.next = None

    def setData(self, data):
        self.data = data

    def getData(self):
        return self.data

    def setNext(self, next):
        self.next = next

    def getNext(self):
        return self.next


class SinglyLinkedList:
    # constructor
    def __init__(self):
        self.head = None

    # method for setting the head of the Linked List
    def setHead(self, head):
        self.head = head

    # Method for inserting a new node at the start of a Linked List
    def insert_at_front(self, data):
        node = Node()
        node.setData(data)
        if self.head == None:
            self.head = node
        else:
            node.setNext(self.head)
            self.head = node

    def reverse(self):
        curr = self.head
        prev = None
        while curr is not None:
            self.head = curr
            curr = curr.next
            self.head.next = prev
            prev = self.head

    def showcase(self):
        curr = self.head
        print("Linked List: ")
        while curr is not None:
            print(curr.data, end=" ")
            curr = curr.next


test = SinglyLinkedList()
test.insert_at_front(5)
test.insert_at_front(3)
test.insert_at_front(11)
test.showcase()
print("\n")
test.reverse()
test.showcase()
