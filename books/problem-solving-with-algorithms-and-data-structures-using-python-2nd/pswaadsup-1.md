# PROBLEM SOLVING WITH ALGORITHMS AND DATA STRUCTURES USING PYTHON

## Introduction

### 1.1: Objective

~

### 1.2: Getting Started

~

### 1.3: What Is Computer Science?

- The study of finding solutions using computational structures.

### 1.4: What Is Programming?

- A method to implement our solutions.

### 1.5: Why Study Data Structures and Abstract Data Types?

- Abstract data types (ADT) is a logical description of how we view interface vs the implementation.
  - I use a car, but I don't know what goes on in the car, all I care for is that the car works which makes it an abstract data type.
- Implementation of ADTs are referred to as data structures.
- Data structures is a way to organize data.
- To manage the complexity of problems and the problem-solving process:
  - Focus on the "big" instead of the "small", data abstraction.
  - Levels of abstraction means creating an encapsulation.
- The users see one thing while developers see another.
- Since there are different ways to implement ADTs this gives flexibility to the developer without harming the user.
- The user can remain focused on the problem-solving process.

### 1.6: Why Study Algorithms?

- Algorithm is a type of solution.
- By considering different algorithms and different problems, when we see a similar problem arise, we know which weapon to use.
- We consider time and space complexities:
  - What if we only have 2 minutes to compute? (Time)
  - What if we give a problem 1000000 inputs? (Space)
- Worst case scenario is that we have a problem that can't be solved or where solutions do exist but require too much time or other resources to work reasonably.
- We find solutions and choose the correct one depending on the situation.

### 1.7: Review of Basic Python

- Python is a modern, easy-t-learn, object-oriented programming language.
- Built-in data types and easy-to-use control constructs.

### 1.8: Getting Started With Data

- Define a class to be a description of what the data will look like (the state) and what the data can do (the behavior).
- Classes are analogous to ADTs because a user of a class only sees the state and behavior.
- Data items are called objects in the object-oriented paradigm.
- An object is an instance of a class.

### 1.8.1: Built-In Atomic Data Types

- Atomic data types:
  - `int`
  - `float`
  - `bool`

### 1.8.2: Built-In Collection Data Types

- Collection data types:

```
lists           []
strings         ""
tuples          ()
sets            {}
dictionaries    {'':''}
```

### 1.8.2.1: Lists

- List is an ordered collection. (ArrayList in other languages)
- Table of operations to use on lists:

```
OPERATION       OPERATOR    EXPLANATION

indexing        [ ]         Access an element of a sequence
concatenation   +           Combine sequences together
repetition      \*          Concatenate a repeated number of times
membership      in          Ask whether an item is in a sequence
length          len         Ask the number of items in the sequence
slicing         [ : ]       Extract a part of a sequence
```

- Examples of operations:

```
EXAMPLE                 YIELDS

my_list = [1,2,3,4]
A = [my_list]\*3
print(A)                [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]
my_list[2]=45
print(A)                [[1, 2, 45, 4], [1, 2, 45, 4], [1, 2, 45, 4]]
```

- Table of methods to use on lists:

```
METHOD      USE                      EXPLANATION

append      a_list.append(item)      Adds a new item to the end of a list
insert      a_list.insert(i,item)    Inserts an item at the ith position in a list
pop         a_list.pop()             Removes and returns the last item in a list
pop         a_list.pop(i)            Removes and returns the ith item in a list
sort        a_list.sort()            Modifies a list to be sorted
reverse     a_list.reverse()         Modifies a list to be in reverse order
del         del a_list[i]            Deletes the item in the ith position
index       a_list.index(item)       Returns the index of the first occurrence of item
count       a_list.count(item)       Returns the number of occurrences of item
remove      a_list.remove(item)      Removes the first occurrence of item
```

- Examples of methods:

```
EXAMPLE                              YIELDS

my_list = [1024, 3, True, 6.5]
my_list.append(False)
print(my_list)                       [1024, 3, True, 6.5, False]
my_list.insert(2,4.5)
print(my_list)                       [1024, 3, 4.5, True, 6.5, False]
print(my_list.pop()) False
print(my_list)                       [1024, 3, 4.5, True, 6.5]
print(my_list.pop(1))                [1024, 4.5, True, 6.5]
print(my_list)                       [1024, 4.5, True, 6.5, False]
my_list.pop(2)
print(my_list)                       [1024, 4.5, 6.5]
my_list.sort()
print(my_list)                       [4.5, 6.5, 1024]
my_list.reverse()
print(my_list)                       [1024, 6.5, 4.5]
print(my_list.count(6.5))            1
print(my_list.index(4.5))            2
my_list.remove(6.5)
print(my_list)                       [1024, 4.5]
del my_list[0]
print(my_list)                       [4.5]
```

- Range function is used with lists.
- Note that the second parameter usually is the end point. (Range doesn't touch it!)
- Range goes (start, end, increment/decrement).
- Examples of the range function:

```
EXAMPLE                 YIELDS

range(10)               range(0, 10)
list(range(10))         [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
range(5,10)             range(5, 10)
list(range(5,10))       [5, 6, 7, 8, 9]
list(range(5,10,2))     [5, 7, 9]
list(range(10,1,-1))    [10, 9, 8, 7, 6, 5, 4, 3, 2]
```

### 1.8.2.2: Strings

- Strings are collections of characters annotated by "".
- Examples of string manipulation:

```
EXAMPLE             YIELDS

"David"             "David"
my_name = "David"
my_name[3]          "i"
my_name \* 2        "my_namemy_name"
len(my_name)        5
```

- Since strings are sequences, they work as expected.
- More examples of string manipulation:

```
EXAMPLE              YIELDS

my_name              "David"
my_name.upper()      "DAVID"
my_name.center(10)   "  David   "
my_name.find('v')    2
my_name.split('v')   ["Da","id"]
```

- Split is useful for processing data by returning a list of strings.
- If no division is specified for split, whitespace is used.

```
METHOD      USE                      EXPLANATION

center      a_string.center(w)       Returns a string centered in a field of size w
count       a_string.count(item)     Returns the number of occurrences of item in the string
ljust       a_string.ljust(w)        Returns a string left-justified in a field of size w
lower       a_string.lower()         Returns a string in all lowercase
rjust       a_string.rjust(w)        Returns a string right-justified in a field of size w
find        a_string.find(item)      Returns the index of the first occurrence of item
split       a_string.split(schar)    Splits a string into substrings at schar
```

- Major difference between lists and strings is:
  - Lists can be modified
  - Strings can't be modified
- This is referred to as mutability.
  - Lists are mutable
  - Strings are immutable
- Examples of mutability among lists vs strings:

```
EXAMPLE          YIELDS

my_name          "David"
my_name[0]="X"   !ERROR!
```

### 1.8.2.3: Tuples

- Tuples are similar to lists in that they are sequences of data.
- Difference is that tuples are immutable, like a string.
- Sometimes you have to convert things to lists then revert back.
- So why use tuples?
  - If you want constant immutable data, like coordinates.

### 1.8.2.4: Sets

- A set is an unordered collection of zero or more immutable data objects.
- Sets don't allow duplicates and are separated by commas in curly braces.
- The set is mutable, you can remove or add, but you can not change.
- Example of creating a set.

```
EXAMPLE                          YIELDS

{3,6,"cat",4.5,False}            {False, 4.5, 3, 6, 'cat'}
my_set = {3,6,"cat",4.5,False}
my_set                           {False, 4.5, 3, 6, 'cat'}
```

- Examples of operations:

```
OPERATION       OPERATOR                EXPLANATION

membership      in                      Set membership
length          len                     Returns the cardinality of the set
|               a_set | otherset         Returns a new set with all elements from both sets
&               a_set & otherset         Returns a new set with only those elements common to both sets
-               a_set - otherset         Returns a new set with all items from the first set not in second
<=              a_set <= otherset        Asks whether all elements of the first set are in the second
```

- Sets have methods that should be familiar in a mathematical setting.
- Examples of methods:

```
METHOD          USE                              EXPLANATION

union           a_set.union(otherset)            Returns a new set with all elements from both sets
intersection    a_set.intersection(otherset)     Returns a new set with only those elements common to both sets
difference      a_set.difference(otherset)       Returns a new set with all items from first set not in second
issubset        a_set.issubset(otherset)         Asks whether all elements of one set are in the other
add             a_set.add(item)                  Adds item to the set
remove          a_set.remove(item)               Removes item from the set
pop             a_set.pop()                      Removes an arbitrary element from the set
clear           a_set.clear()                    Removes all elements from the set
```

- Examples of set usage:

```
EXAMPLE                          YIELD

my_set                           {False, 4.5, 3, 6, 'cat'}
your_set                         {99,3,100}
my_set.union(your_set)           {False, 4.5, 3, 100, 6, 'cat', 99}
my_set | your_set                {False, 4.5, 3, 100, 6, 'cat', 99}
my_set.intersection(your_set)    {3}
my_set & your_set                {3}
my_set.difference(your_set)      {False, 4.5, 6, 'cat'}
my_set - your_set                {False, 4.5, 6, 'cat'}
{3,100}.issubset(your_set)       True (Is {3,100} part of your_set?)
{3,100}<=your_set                True (Is {3,100} in your_set?)
my_set.add("house")
my_set                           {False, 4.5, 3, 6, 'house', 'cat'}
my_set.pop                       False
my_set                           {4.5, 3, 6, 'house', 'cat'}
my_set.clear()
my_set                           set()
```

### 1.8.2.5: Dictionaries

- Final Python collection is an unordered structure called a dictionary.
- Dictionaries are a pair of items which each consist of a key and a value.
- Example of a dictionary entry:

```
capitals {'Wisconsin': 'Madison', 'Iowa': 'DesMoines'}
```

- Examples of operators:

```
OPERATOR    USE              EXPLANATION

[]          my_dict[k]       Returns the value associated with k, otherwise its an error
in          key in a_dict    Returns True if key is in the dictionary, False otherwise
del         del a_dict[key]  Removes the entry from the dictionary
```

- Examples of methods:

```
METHOD      USE                  EXPLANATION

keys        a_dict.keys()        Returns the keys of the dictionary in a dict_keys object
values      a_dict.values()      Returns the values of the dictionary in a dict_values object
items       a_dict.items()       Returns the key-value pairs in a dict_items object
get         a_dict.get(k)        Returns the value associated with k, None otherwise
get         a_dict.get(k,alt)    Returns the value associated with k, alt otherwise
```

### 1.9: Input and Output

- Software and users need to have some sort of dialogue in order to best benefit the user and this is where input and output comes into play.
- For example:

```
a_name = input("This is a prompt that takes in the input: ")
```

- It's important to note the input will be a string representing the exact characters that were entered after the prompt.
- To interpret as another type, the variable must be enclosed in a specific function.
- For example:

```
float_name = float(a_name)
double_name = double(a_name)
```

### 1.9.1: String Formatting

- It's possible to change both the separator and end argument.
- The separator is usually a white space unless specified.
- Examples of string formatting:

```
EXAMPLE                             YIELD

print("Hello","World",sep="**_")    Hello_**World
print("Hello","World",end"**_")     Hello World_**
```

- To put more control over the output, Python provides formatted strings.
- To use formatted strings, a "%" operator is used called the format operator.
- Examples of format operators:

```
EXAMPLE                                          YIELD

print(a_name, "is", age, "years old.")           banana, 24
print("%s is %d years old." % (a_name, age))     banana, 24.00
```

- This is useful if certain variables aren't formatted correctly or if for the specific output needs to be a certain way.
- Examples of different ways to format:

```
CHARACTER       OUTPUT FORMAT

i               Integer
d               Double
u               Unsigned integer
f               Floating point as m.ddddd
e               Floating point as m.ddddde+/-xx
E               Floating point as m.dddddE+/-xx
g               Use "%e" for exponents < -4 || > 5, otherwise use %f
c               Single character
s               String, or any data object that can be converted to a string by using the str function
%               Insert a literal % character
```

- Examples of modifiers:

```
MODIFIER    EXAMPLE     DESCRIPTION

number      %20d        Put the value in a field width of 20
-           %-20d 	Put the value in a field 20 characters wide, left-justified
*           %+20d 	Put the value in a field 20 characters wide, right-justified
0           %020d       Put the value in a field 20 characters wide, fill in with leading zeros
.           %20.2f      Put the value in a field 20 characters wide with 2 characters to the right of the decimal point
(name)      %(name)d    Get the value from the supplied dictionary using name as the key
```

- More examples of string formatting:

```
EXAMPLE                                                 YIELD

price = 24
item = "banana"
print("The %s costs %d cents"%(item,price))             The banana costs 24 cents
print("The %+10s costs %5.2f cents"%(item,price))       The     banana costs 24.00 cents
print("The %+10s costs %10.2f cents"%(item,price))      The     banana costs      24.00 cents
item_dict = {"item":"banana","cost":24}
print("The %(item)s costs %(cost)7.1f cents"%item_dict)  The banana costs    24.0 cents

(%(item)s = get the "item" and format to string)
(%(cost)7.1f = get the "cost" and width of 7, w/ 1 decimal due to float)
```

- In addition to these format modifiers, Python strings also include a format method that can be used in conjunction with a new Formatter class to implement complex string formatting.

### 1.10: Control Structures

- Algorithms require 2 important control structures:
  - Iteration.
  - Selection.
- Iteration comes in terms such as `while` and `for` statements.
- While is a general purpose iterative structure that checks to see if the condition is True or False.
- Example of a `while` statement:

```py
while counter <= 5 and not done:
    print("hello")

"hello"
"hello"
"hello"
"hello"
"hello"
```

- `For` is a structure used for collections of sequences.
- An easy way to remember this is that if we know the number of iterations we use `for`, otherwise we use `while`.
- Especially in evolving data structures, this is very relevant.
- `For` is very useful for iteration on each character of a string.
- Example of a `for` statement:

```py
for item in range(5):
    print(item**2)

0
1
4
9
16
```

- Example of iteration:

```py
word_list = ['cat','dog','rabbit']
letter_list = [ ]
for a_word in word_list:
    for a_letter in a_word:
        letter_list.append(a_letter)

print(letter_list)
['c', 'a', 't', 'd', 'o', 'g', 'r', 'a', 'b', 'b', 'i', 't']
```

- Selection statements allow programmers to ask questions and based on the result, perform different actions.
- These statements are usually provided as `if else` and `if`.
- For nested statements `elif` can be used in the stead.
- Example of selection being used:

```py
word_list = ['cat','dog','rabbit']
letter_list = [ ]
for a_word in word_list:
    for a_letter in a_word:
        if a_letter not in letter_list:
        letter_list.append(a_letter)

print(letter_list)
['c', 'a', 't', 'd', 'o', 'g', 'r', 'b', 'i']
```

- Lists have an alternative method for creation that uses iteration and selection constructs known as list comprehension.
- Example of before using list comprehension:

```py
squared_list = []
for x in range(1,11):
   squared_list.append(x*x)

print(squared_list)
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

- Example of now using list comprehension:

```py
squared_list = [x*x for x in range(1,11)]

print(squared_list)
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

- Even then, one could allow selection criteria so that certain items get added to the data structure.
- Examples of using list comprehension with selection:

```py
squared_list = [x*x for x in range(1,11) if x%2 != 0]

print(squared_list)
[1, 9, 25, 49, 81]
```

```py
comprehension = [ch.upper() for ch in 'comprehension' if ch not in 'aeiou']

print(comprehension)
['C', 'M', 'P', 'R', 'H', 'N', 'S', 'N']
```

```py
print([ch for ch in "".join(['cat','dog','rabbit'])])

['c', 'a', 't', 'd', 'o', 'g', 'r', 'a', 'b', 'b', 'i', 't']
```

- Iteration uses `for` and `while`.
- Selection uses `if`.

### 1.11: Exception Handling

- Two types of errors in programming.
  - Syntax.
    - Human error.
  - Logic.
    - Wrong conclusion (dividing by zero, out of scope variable).
    - Logic errors eventually create runtime errors (exceptions).
- Runtime errors are called exceptions.
- When an exception occurs, that means the error has been "raised".
  - One can handle the "raised" error with a `try` statement.
  - If the `try` statement can't complete, an `except` block catches the exception and prints relevant information to the user such as `"Sorry, information not allowed."`
- One could put in a built in "raised" error using the `raise` statement.
  - If you are asking for user input, but selectively want positive integers, you can `raise` a `RuntimeError("Positive integers only!")`.

### 1.12: Defining Functions

- Creating functions require 3 things.
  - Name.
  - Parameters.
  - Body.

```py
def square(n):
	return n**2
```

- Shakespeare program.

```py
import random

def generateString(inputString):
	alphabet = "abcdefghijklmnopqrstuvwxyz"
	res = ""
	for indexLoop in range(inputString):
		res = res + alphabet[random.randrange(27)]
	return res

def compareString():

def scoreString(goal, inputString):

solution = "me thinks its a weasel"

```

`http://interactivepython.org/runestone/static/pythonds/Introduction/DefiningFunctions.html`

#### BOOKMARK
