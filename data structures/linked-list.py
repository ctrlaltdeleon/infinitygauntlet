class Node:
    def __init__(self, data):
        self.val = data
        self.next = None


class DoublyNode:
    def __init__(self, data):
        self.val = data
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

    def addFirst(self, newNodeData):
        newNode = Node(newNodeData)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head = newNode

    def addLast(self, newNodeData):
        newNode = Node(newNodeData)
        if self.tail is None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
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
            print(curr.val, end=" ")
            curr = curr.next


newLL = LinkedList()
randList = [11, 13, 275, 2, 5, 8, 64, 52]
for num in randList:
    newLL.addFirst(num)
    newLL.addLast(num*2)

newLL.showcase()
print("\n\n")
newLL.reverse()
newLL.showcase()
