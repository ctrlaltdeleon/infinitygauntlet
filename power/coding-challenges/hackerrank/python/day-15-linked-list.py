class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def display(self, head):
        current = head
        while current:
            print(current.data, end=' ')
            current = current.next

    def insert(self, head, data):
        # Can do "NewNode = Node(data)" and then apply that to the insertion.
        # No head? Insert data.
        if head is None:
            head = Node(data)
            self.tail = head
        # Insert the data at the end
        else:
            # self.tail.next = self.tail = Node(data)
            # This goes from right to left in order.
            node = Node(data)
            self.tail.next = node
            self.tail = node
        return head

list_data = Solution()
T = int(input("Input number of elements to exist: "))
head = None
for i in range(T):
    data = int(input("Insert element #%i: " % (i+1)))
    head = list_data.insert(head, data)
list_data.display(head)

# Important to note that head(), tail(), next() are built-in functions in Python.

"""
Input number of elements to exist: 3
Insert element #1: 10
Insert element #2: 20
Insert element #3: 30
10 20 30 
"""