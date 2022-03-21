class TreeNode:
    def __init__(self, data, left_child=None, right_child=None):
        self.data = data
        self.left_child = left_child
        self.right_child = right_child

class BinaryTree:
    def __init__(self, root_node=None):
        self.root = root_node

    def number_of_leaves(self, root):
        # No root? No leaves.
        if root == None:
            return 0
        # No children? Just 1 leaf, the root.
        if root.left_child == None and root.right_child == None:
            return 1
        else:
            # Do recursion until all trees are obtained.
            return self.number_of_leaves(root.left_child) + self.number_of_leaves(root.right_child)