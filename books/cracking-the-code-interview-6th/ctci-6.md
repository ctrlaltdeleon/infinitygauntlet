# CRACKING THE CODING INTERVIEW

## 6: Big O

### Slowest to Fastest (Operations VS. Elements)

- `O(n!)`
- `O(2^n)`
- `O(n^2)`
- `O(n log n)`
- `O(n)`
- `O(log n)`
- `O(1)`

### Big O, Big Omega, and Big Theta

- O describes an upper bound. "This is the fastest it could be".
- Omega describes a lower bound. "This is the slowest it could be".
- Theta describes both. "It's around this speed".

### Best VS Worst VS Expected, Cases

- Quicksort for example:
- Note that quicksort has various implementations.
  - Best:
    - All elements are equal, no need to shuffle.
    - It's already sorted, but needs to run through the data.
    - `O(n)`.
  - Worst:
    - Pivot chosen is the biggest element.
    - `O(n^2)`.
  - Expected:
    - Pivot chosen is a near average element.
    - `O(n log n)`.
- Barely discuss time complexity, because it's not a useful concept.
- It's essentially because anything could be `O(1)`.

### Time Complexity

- How fast the program processes.

### Space Complexity

- Array of size `n`? `O(n)` space.
- 2d array of size `n x n`? `O(n^2)` space.

### Drop the Constants

- Usually constants are comparisons such as `if`.
- Pay attention to the `for`.

### Drop the Non-Dominant Terms

- Take the biggest `n` into consideration.
- `O(n^2 + n) --> O(n^2)`.

### Multi-Part Algorithms, Add VS Multiply

- Add: `O(n)`

```py
for index in array:
    print("nice")
for index in array:
    print("good")
```

- Multiply: `O(n^2)`

```py
for index in array:
    for index in array:
        print("nice","good")
```

### Amortized Time

- Describes that a worst case happens every now and then.
- An `ArrayList` for example doubles its space when `insert()` to full data.
- That becomes `O(n)`, because we need to recreate.
- An `ArrayList` for `insert()` to non-full data is `O(1)`.

### O(log n) Runtimes

- When performing an action, the data size is reduced each iteration.
- Number of elements gets halved each time? `O(log n)`!
- Binary search is `O(log n)`!

### Recursive Runtimes

- `O(2^n)` since it calls upon itself.
- Treat it as `O(branches^depth)`!
- Space complexity is `O(n)`! Since it can only exist as `O(n)` at any time.

### Examples and Exercises

- Usually is hard at first, but once the patterns appear, quite easy.
- Notice the requirements of `if` statements within `for` statements.
- Take a look at this function:

```py
def print_something(list_a, list_b):
    for index in len(list_a):
        for index in len(list_b):
            print("something")
```

- This can be easily mistaken for `O(n^2)`, but it's actually `O(ab)`.
- Then we have this part of a function:

```py
for (int x = 2; x * x <= n; x++)
```

- One could infer that it's `O(n)`, but it's actually `O(sqrt(n))`!
- Think of it as balancing equations!
- Then we have the fibonacci sequence here:

```py
def fib(n):
    if (n <= 0)
        return 0
    if (n == 1)
        return 1
    return fib(n-1) + fib(n-2)
```

- Notice the return statement as it creates recursive calls.
- `O(2^N)` due to it being a single vs double call that multiplies.

```py
def allFib(n):
    for index in range(n):
        print(index+1, ":", fib(index))


def fib(n):
    if (n <= 0):
        return 0
    if (n == 1):
        return 1
    return fib(n-1) + fib(n-2)
```

- People mistake this as `O(n2^n)`.
- This is actually `O(2^n+1)` because `n` does change.

```py
import functools

@functools.lru_cache(maxsize=None)
def fib(num):
    if num < 2:
        return num
    else:
        return fib(num-1) + fib(num-2)
```

- This technique is called "memoization" which is useful for recursive functions.
- What memoization does is preserve a cache so that the function doesn't have to recompute previous values, it's already there.
- We're doing constant amount of work, so `O(n)` times.

```py
def product(a, b):
    sum_numbers = 0
    for index in range(b):
        sum_numbers += a
    return sum_numbers
```

- `O(b)`, since the `for` loop cycles through `b`.

```py
def power(a, b):
    if (b < 0):
        return 0
    elif (b == 0):
        return 1
    else:
        return a * power(a, b-1)
```

- `O(b)`, since the recursive code iterates through `b` calls only.

#### BOOKMARK PAGE 66
