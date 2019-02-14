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

        return count

    def addFirst(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node

    def addLast(self, data):
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


ll = LinkedList()

randList = [10, 20, 275, 2, 5, 8, 64, 52]
for num in randList:
    ll.addFirst(num)
    ll.addLast(num*2)
ll.showcase()
print("\n")
ll.reverse()
ll.showcase()
