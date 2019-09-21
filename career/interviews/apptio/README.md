# APPTIO

## Round 1 (Online)

**Environment:** 30 minutes with no person.

**Type:** Behavioral and technical.

**Notes:**

- CCAT assessment.

## Round 2 (Phone)

**Environment:** 20 minutes with Recruiter.

**Type:** Behavioral.

**Notes:**

- "What do you want from working here?"
- "Are you open to relocation?"
- "Show your eagerness to learn!"

## Round 3 (Online & Phone)

**Environment:** 1 hour with Hiring Manager.

**Type:** Behavioral and technical.

**Notes:**

- "What have you been doing the past year?"
- "Can you reverse a string without any shortcuts?"

```py
def reverseString(string):
    solution = ""
    for character in string[::-1]:
        solution += character
    return solution

def reverseRecursion(string):
    return string if len(string) <= 1 else reverseRecursion(string[1:]) + string[0]

"""
Output:

reverseRecursion(hello)
    = reverseRecursion(ello) + h           # The recursive step
    = reverseRecursion(llo) + e + h
    = reverseRecursion(lo) + l + e + h
    = reverseRecursion(o) + l + l + e + h  # Base case
    = o + l + l + e + h
    = olleh
"""
```

- "Can you do an iterative solution to a factorial function?"

```py
def factorial(number):
    solution = 1
    for index in range(1,number+1):
        solution *= index
    return solution
```

- "Can you do a recursive solution to a factorial function?"

```py
def factorialRecursion(number):
    return number if number <= 1 else number * factorialRecursion(number-1)
```

- "Can you make an object oriented design for a deck of cards?"

```py
# https://medium.com/@anthonytapias/build-a-deck-of-cards-with-oo-python-c41913a744d3
```

## Round 4 (On site)

**Environment:** ?

**Type:** ?

**Notes:**

- Did not make it.
