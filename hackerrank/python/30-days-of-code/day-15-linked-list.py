"""
@author: acfromspace
"""


class Node:

    def __init__(self, data):
        # creation of the linked list
        self.data = data
        self.next = None


class Solution:

    def display(self, head):
        current = head
        while current:
            print(current.data, end=' ')
            current = current.next

    def insert(self, head, data):
        # can do "NewNode = Node(data)" and then apply that to the insertion
        # no head? insert data
        if head is None:
            head = Node(data)
            self.tail = head
        # insert the data at the end
        else:
            node = Node(data)
            self.tail.next = node
            self.tail = node
        return head


mylist = Solution()
T = int(input("Input number of elements to exist: "))
head = None

for i in range(T):
    data = int(input("Insert element #%i: " % (i+1)))
    head = mylist.insert(head, data)

mylist.display(head)
