class Node:
    def __init__(self):
        self.data = None
        self.next = None

    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data

    def set_next(self, next):
        self.next = next

    def get_next(self):
        return self.next

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def set_head(self, head):
        self.head = head

    def insert_at_front(self, data):
        node = Node()
        node.set_data(data)
        if self.head == None:
            self.head = node
        else:
            node.set_next(self.head)
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
print("\n")
test.reverse()
test.showcase()

"""
Linked List: 
11 3 5 

Linked List:
5 3 11

Linked List:
11 3 5
"""