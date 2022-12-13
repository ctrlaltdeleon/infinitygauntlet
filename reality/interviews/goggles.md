- SWE II L3 $190,837 (salary: 132,600, stock: 37,853, bonus: 20,384)

- 2:45-3:30 THURSDAY
- greg
- code review on class advertisement and class account, separated the functions apart on handleClick(), considered technical debt when having vague values as constants, implemented getRandomSample(itr: NodeIterator, sampleSize: int) > List[Node], getting a random series of nodes each time

- 3:45-4:30 THURSDAY
- evan?
- given an array, need to work back and connect to indexes and see if it goes to end of file, input is [6, 2, 0, 5, -1, -1, 4], output is [[1,2,0,6,4][3,5]], trick was to turn input to a hashmap

- 11:30-12:15 FRIDAY
- goutham
- // Square grid. top-left is the source, bottom-right is the destination. there are some blocks. movement can be right or down.
  // What is the minimum number of additional blocks to be placed so that no path exists from source to destination ?
  // Find a path which all points pass through and how would you do that?

0 0 0 0 1
0 1 0 1 0
0 1 0 1 0
0 1 0 0 0
1 0 0 0 0

= 1 block

0 0 0 0 1
0 1 0 1 0
0 1 0 1 0
0 1 0 0 [0]
1 0 0 [0] 0

0 0 0 0 1
0 1 0 1 0
0 1 0 1 0
0 0 1 0 0
0 0 0 0 0

// maximum number 2 blocks
// other answers include 1 or 0 blocks
// source block [0, 0]
// destination block [len(maze) - 1, len(maze) - 1]

def minimumNumberOfAdditionalBlocks(maze: List[int]) -> int:
