"""
@author: acfromspace
"""


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def inorder(root):
    if root:
        # First recur on left child.
        inorder(root.left)
        # Then print the data of node.
        print(root.val),
        # Now recur on right child.
        inorder(root.right)


def postorder(root):
    if root:
        # First recur on left child.
        postorder(root.left)
        # The recur on right child.
        postorder(root.right)
        # Now print the data of node.
        print(root.val),


def preorder(root):
    if root:
        # First print the data of node.
        print(root.val),
        # Then recur on left child.
        preorder(root.left)
        # Finally recur on right child.
        preorder(root.right)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print("Preorder traversal of binary tree is:")
preorder(root)
print("\nInorder traversal of binary tree is:")
inorder(root)
print("\nPostorder traversal of binary tree is:")
postorder(root)
