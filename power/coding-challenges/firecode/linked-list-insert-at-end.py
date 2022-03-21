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

    def insert_at_end(self, data):
        node = Node()
        node.set_data(data)
        if self.head == None:
            self.head = node
        else:
            curr = self.head
            while curr.next != None:
                curr = curr.next
            curr.next = node

    def showcase(self):
        curr = self.head
        print("Linked List: ")
        while curr is not None:
            print(curr.data, end=" ")
            curr = curr.next

test = SinglyLinkedList()
test.insert_at_end(5)
test.insert_at_end(6)
test.insert_at_end(1)
test.showcase()

"""
Linked List: 
5 6 1
"""