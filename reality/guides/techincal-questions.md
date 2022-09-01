# Technical Questions

## What is the difference between "arguments" and "parameters" when dealing with functions?

- Arguments are what is given to a function such as "Andrew".
- Parameters are what a function takes such as "name".
- Parameters are what are expected, arguments are what it is.

## Why use Object Oriented Programming?

- Encapsulation.
  - Reduce complexity + increase resuability.
  - Charmander is hungry. You can `feed()` Charmander, but you can't change how hungry the Charmander is directly because that's private properties.
- Inheritance.
  - Eliminate redundant code.
  - Charizard inherits Charmander's traits and moves, no need to recreate.
- Polymorphism.
  - Refactor ugly switch/case statements.
  - Charizard can use `flamethrower()` like Charmander, but a different version called `fireBlast()`.

## Difference between DFS and BFS?

- What is DFS? (Depth-first search)
  - An algorithm that starts at the root node and explores as far as possible before backtracking to the next.
  - Think left to right.
- What is BFS? (Breadth-first search)
  - An algorithm that starts at the tree root and explores all nodes at the present depth prior to moving to the next depth.
  - Think top to bottom.
  - A queue is usually implemented.

## Difference between "sliding window" and "2 pointer"?

- Difference between "sliding window" and "2 pointer"?
  - Sliding window takes into account everything in between 2 points.
  - 2 pointer only accounts the 2 points.

## How to sort a list of lists based on a specific index of the list?

- cool_list = [[2, 'Dog'], [0, 'Bird'], [7, 'Cat']]
- sorted(cool_list, key=lambda x:x[1])) => [[0, 'Bird'], [7, 'Cat'], [2, 'Dog']]

## Difference between `for i in j` VS `for i in range(len(j))`?

- First goes through the value, second goes through the index.

## Why use tuples over lists in certain scenarios?

- Tuples have set positions in the data structure, immutable.
- Fast, less memory, and great for transferring known data.
