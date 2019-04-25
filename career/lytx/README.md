# LYTX

## Round 1 (Phone Interview)

- 15 minutes.
- Behavioral questions, company culture, reason for applying.

## Round 2 (Coding Challenge)

- 1 hour.
- 2 easy, 1 hard. (respectively)
- **Verify Items.** Given four different arrays, determine the differences between two arrays to the other two arrays and increment a counter based on criteria.

```py
"""
@author: acfromspace
"""

"""
DESCRIPTION:

There are N citizens voting in this year's Hackland election.
Each voter writes the name of their chosen candidate on a ballot and places it in a ballot box.
The candidate with the highes number of votes win the election.
If two or more candidates have the same number of votes, then the tied candidates' names are ordered alphabetically and the last name wins.

Complete the election Winner function in your editor. It has 1 parameter:L an array of strings, votes, describing the votes in the ballot box.
This function must review these votes and return a string representing the name of the winning candidate.

CONSTRAINTS:

1 <= N <= 10^4

INPUT FORMAT:

["an","array","of","strings"]

OUTPUT FORMAT:

Name of the person who has the max votes.
If there are multiple people with same number of votes(max) then print the last name.

SAMPLE INPUT 1:

String[] votes = {"Alex", "Michael", "Harry", "Dave", "Michael", "Victor", "Harry", "Alex", "Mary", "Mary"};

SAMPLE OUTPUT 1:

Michael

DESCRIPTION 1:

votes = {"Alex", "Michael", "Harry", "Dave", "Michael", "Victor", "Harry", "Alex", "Mary", "Mary"}
Alex, Harry, Michael, and Mary are all tied for the highest number of votes.
Because Michael is alphabetically last, we return his name as the winner.

SAMPLE INPUT 2:

String[] votes = { "victor", "veronica", "ryan", "dave", "maria", "farah", "farah", "ryan", "veronica" };

SAMPLE OUTPUT 2:

veronica

EXPLANATION 2:

votes = {"Victor", "Veronica", "Ryan", "Dave", "Maria", "Maria", "Farah", "Farah", "Ryan", "Veronica"}
Veronica, Ryan, Maria, and Farah are all tied for the highest number of votes.
Because Veronica is alphabetically last, we return her name as the winner.
"""

from collections import Counter


def hackland_election(votes):
    # Find the most votes on a person and organize in a dict.
    tally = Counter(votes).most_common()
    # Returns the first most common given via when inputted, then syntactic output to solve the problem.
    return list([i[0] for i in tally])[0]


ballots = int(input("Number of HackLand Ballots: "))
votes = []
for index in range(ballots):
    votes.append(input("Give a name for ballot #%i: " % (index+1)))
print("hackland_election():", hackland_election(votes))

"""
Output:

Number of HackLand Ballots: 5
Give a name for ballot #1: ac
Give a name for ballot #2: jinsoul
Give a name for ballot #3: ac
Give a name for ballot #4: jinsoul
Give a name for ballot #5: jinsoul
hackland_election(): jinsoul
"""
```

- **HackLand Election.** Given an array of strings, determine the winner of an election dependent on amount of votes as well as placement of indexed votes.

```py
"""
@author: acfromspace
"""

"""
DESCRIPTION:

Michael is a shop owner who keeps n list, L, of the name and sale price for each item in inventory.
The store employees record the name and sale price of every item sold.
Michael suspects his manager, Alex, of embezzling money and modifying the sale prices of some of the items.
Write a program that finds the number of times Alex recorded an incorrect sale price.

Complete the verify_items function provided in your editor so that it returns the number of incorrect sale prices recorded by Alex.

It has 4 parameters:
        orig_items: An array of strings, where each element is an item name.
        orig_prices: An array of floating point numbers, where each element contains the original (correct) price of the item in the corresponding index of orig_items.
        alex_items: An array of strings containing the name of the items with sales recorded by Alex.
        alex_prices: An array of floating point numbers, where each element contains the sale price recorded by Alex for the item in the corresponding index of alex_items.

NOTES:

Where required by the language, there may also be 2 additional integer parameters for passing the array sizes (N and M).

return an INT
orig_items = string array
orig_prices = float array
alex_items = string array
alex_prices = float array

INPUT FORMAT:

The locked stub code in your editor processes the following inputs and passes the necessary arguments to the verify_items function:
        The first line contains an integer, N, the size of the orig_items array. Each line i (where 0 ≤ i < N) of the N subsequent lines describes element i in orig_items.
        The next line contains an integer, N, the size of the orig_prices array. Each line i of the N subsequent lines describes element i in orig_prices.
        The next line contains an integer, M, the size of the items array. Each line j (where 0 ≤ j < M) of the M subsequent lines describes element j in items.
        The next line contains an integer, M, the size of the prices array. Each line j of the M subsequent lines contains the price of element j in items.

CONSTRAINTS:

1 ≤ N ≤ 105
1 ≤ M ≤ N
1.00 ≤ orig_prices, alex_prices ≤ 100000.00, where 0 ≤ i < N, and 0 ≤ j < M

OUTPUT FORMAT:

Return the number of items whose sale prices were incorrectly recorded by Alex.

SAMPLE INPUT 1:

4
rice
sugar
wheat
cheese
4
16.89
56.92
20.89
345.99
2
rice
cheese
2
18.99
400.89

SAMPLE OUTPUT 1:

2

EXPLANATION 1:

Sample Case 0: N = 4 , M = 2
orig_items = {"rice", "sugar", "wheat"," cheese"}
orig_prices = {16.89, 56.92, 20.89, 345.99}
alex_items = {"rice", "cheese"}
alex_prices = {18.99, 400.89}
The prices for rice and cheese do not match the original price list, so we return 2 (the number of incorrectly recorded sale prices).

SAMPLE INPUT 2:

3
chocolate
cheese
tomato
3
15.00
300.90
23.44
3
cheese
tomato
chocolate
3
300.90
23.44
10.00

SAMPLE OUTPUT 2:

1

EXPLANATION 2:

Sample Case 1: N = 3, M = 3
orig_items = {"chocolate", "cheese", "tomato"}
orig_prices = {15, 300.90, 23.44}
alex_items = {"chocolate", "cheese", "tomato"}
alex_prices = {15, 300.90, 10}
The price for tomato does not match the original price list, so we return 1 (the number of incorrectly recorded sale prices).
"""


def verify_items(orig_items, orig_prices, alex_items, alex_prices):
    incorrect = 0
    original = dict(zip(orig_items, orig_prices))
    alex = dict(zip(alex_items, alex_prices))
    for index in alex.items():
        if index not in original.items():
            incorrect += 1
    return incorrect


orig_items = []
orig_prices = []
alex_items = []
alex_prices = []
orig_count = int(input("Original count: "))
alex_count = int(input("Alex count: "))
for index in range(orig_count):
    orig_items.append(str(input("Input orig_items #%s: " % (index+1))))
    orig_prices.append(float(input("Input orig_prices #%d: " % (index+1))))
for index in range(alex_count):
    alex_items.append(str(input("Input alex_items #%s: " % (index+1))))
    alex_prices.append(float(input("Input alex_prices #%d: " % (index+1))))
print("verify_items():",
      verify_items(orig_items, orig_prices, alex_items, alex_prices))

"""
Output:

Original count: 3
Alex count: 3
Input orig_items #1: chocolate
Input orig_prices #1: 15.00
Input orig_items #2: cheese
Input orig_prices #2: 300.90
Input orig_items #3: tomato
Input orig_prices #3: 23.44
Input alex_items #1: cheese
Input alex_prices #1: 300.90
Input alex_items #2: tomato
Input alex_prices #2: 23.44
Input alex_items #3: chocolate
Input alex_prices #3: 10.00
verify_items(): 1
"""
```

- **Counting Groups.**
  - Did not finish so can not put further input.

## Round 3 (On-Site)

- Did not make it.
