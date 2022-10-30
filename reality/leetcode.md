# Leetcode

## Data Structures

- `[]`
  - `list.append(x)`
    - adds `x` to end
  - `list.extend(iterable)`
    - list + list = newlist
  - `list.insert(i, x)`
    - adds `x` at index
  - `list.remove(x)`
    - removes first occurrence of `x`
  - `list.pop([i])`
    - removes item at index
    - default is last item
  - `list.clear()`
  - `list.index(x, start, end)`
    - returns index of `x`'s first occurrence
    - `start` and `end` are optional and limits the search
  - `list.count(x)`
    - return number of times `x` appears
  - `list.sort()`
    - sorts items of the list in place
  - `list.reverse()`
    - reverse the items of the list in place
  - `list.copy()`
    - return a shallow copy of the list
- `q = deque(iterable)`
  - `q.append(x)`
  - `q.popleft()`

## Methods

- `enumerate(iterable, start=0)`
  - `for index, element in enumerate(cool_list)`

## Problems by Blind75

### Arrays & Hashing

- Contains Duplicate
  - use a set, for loop, return true if in set, else add to set
- ## Valid Anagram
- Two Sum
- Group Anagrams
- Top K Frequent Elements
- Product of Array Except Self
- Valid Sudoku
- Encode and Decode Strings
- Longest Consecutive Sequence
