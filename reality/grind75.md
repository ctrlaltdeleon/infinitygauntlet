# Grind75

## Definitions

- What is DFS? (Depth-first search)
  - An algorithm that starts at the root node and explores as far as possible before backtracking to the next.
  - Think left to right.
- What is BFS? (Breadth-first search)
  - An algorithm that starts at the tree root and explores all nodes at the present depth prior to moving to the next depth.
  - Think top to bottom.
  - A queue is usually implemented.
- Difference between "sliding window" and "2 pointer"?
  - Sliding window takes into account everything in between 2 points.
  - 2 pointer only accounts the 2 points.
- How to sort a list of lists based on a specific index of the list?
  - cool_list = [[2, 'Dog'], [0, 'Bird'], [7, 'Cat']]
  - sorted(cool_list, key=lambda x:x[1])) => [[0, 'Bird'], [7, 'Cat'], [2, 'Dog']]
- Difference between `for i in j` VS `for i in range(len(j))`?
  - First goes through the value, second goes through the index.
- Why use tuples over lists in certain scenarios?
  - Tuples have set positions in the data structure, immutable.
  - Fast, less memory, and great for transferring known data.

## Methods

- `enumerate(iterable, start=0)`
  - `for index, element in enumerate(cool_list)`

## Problems

1. Two Sum
   1. Array, Hash Table
2. Valid Parentheses
   1. String, Stack
3. Merge Two Sorted Lists
   1. Linked List, Recursion
4. Best Time to Buy and Sell Stock
   1. Array, Dynamic Programming
5. Valid Palindrome
   1. Two Pointers, String
6. Invert Binary Tree
   1. Tree, DFS, BFS, Binary Tree
7. Valid Anagram
   1. Hash Table, String, Sorting
8. Binary Search
   1. Array, Binary Search
9. Flood Fill
   1. Array, DFS, BFS, Matrix
10. Maximum Subarray
    1. Array, Divide and Conquer, Dynamic Programming
11. Lowest Common Ancestor of a Binary Search Tree
    1. Tree, DFS, BST, Binary Tree
12. Balanced Binary Tree
    1. Tree, DFS, Binary Tree
13. Linked List Cycle
    1. Hash Table, Linked List, Two Pointers (Floyd's Tortoise and Hare)
    2. Space O(n), Time O(n) => Space O(n), Time O(1)
14. Implement Queue Using Stacks
    1. Stack, Design, Queue
15. First Bad Version
    1. Binary Search, Interactive, Function Call
16. Ransom Note
    1. Hash Table, String, Counting
    2. Solved on first try!
17. Insert Interval
    1. Array, Matrix
18. 01 Matrix
    1. Array, Dynamic Programming, BFS, Matrix
    2. Difficult!
19. K Closest Points to Origin
    1. Array, Math, Divide and Conquer, Geometry, Sorting, Heap (Priority Queue), Quickselect
    2. Solved on first try!
20. Longest Substring Without Repeating Characters
    1. Hash Table, String, Sliding Window
21. 3Sum
    1. Array, Two Pointers, Sorting
