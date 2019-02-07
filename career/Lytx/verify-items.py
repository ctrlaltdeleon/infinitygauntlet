"""
@author: acfromspace
"""

"""
DESCRIPTION:

Michael is a shop owner who keeps n list, L, of the name and sale price for each item in inventory. 
The store employees record the name and sale price of every item sold. 
Michael suspects his manager, Alex, of embezzling money and modifying the sale prices of some of the items. 
Write a program that finds the number of times Alex recorded an incorrect sale price.
 
Complete the verifyItems function provided in your editor so that it returns the number of incorrect sale prices recorded by Alex. 

It has 4 parameters:
        origItems: An array of strings, where each element is an item name.
        origPrices: An array of floating point numbers, where each element contains the original (correct) price of the item in the corresponding index of origItems.
        items: An array of strings containing the name of the items with sales recorded by Alex.
        prices: An array of floating point numbers, where each element contains the sale price recorded by Alex for the item in the corresponding index of items.
 
NOTES:

Where required by the language, there may also be 2 additional integer parameters for passing the array sizes (N and M).

return an INT
origItems = string array
origPrices = float array
items = string array
prices = float array
 
INPUT FORMAT:

The locked stub code in your editor processes the following inputs and passes the necessary arguments to the verifyItems function:
        The first line contains an integer, N, the size of the origItems array. Each line i (where 0 ≤ i < N) of the N subsequent lines describes element i in origItems.
        The next line contains an integer, N, the size of the origPrices array. Each line i of the N subsequent lines describes element i in origPrices.
        The next line contains an integer, M, the size of the items array. Each line j (where 0 ≤ j < M) of the M subsequent lines describes element j in items.
        The next line contains an integer, M, the size of the prices array. Each line j of the M subsequent lines contains the price of element j in items.
 
CONSTRAINTS:

1 ≤ N ≤ 105
1 ≤ M ≤ N
1.00 ≤ origPricesi, pricesj ≤ 100000.00, where 0 ≤ i < N, and 0 ≤ j < M
 
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
origItems = {"rice", "sugar", "wheat"," cheese"}
origPrices = {16.89, 56.92, 20.89, 345.99}
items = {"rice", "cheese"}
prices = {18.99, 400.89}
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
origItems = {"chocolate", "cheese", "tomato"}
origPrices = {15, 300.90, 23.44}
items = {"chocolate", "cheese", "tomato"}
prices = {15, 300.90, 10}
The price for tomato does not match the original price list, so we return 1 (the number of incorrectly recorded sale prices).
"""

# function without the main function, fully works for Python3


def verifyItems(origItems, origPrices, items, prices):
    # Write your code here

    incorrect = 0

    original = dict(zip(origItems, origPrices))
    alex = dict(zip(items, prices))

    # this only compares values though, not taking into account
    for counter in alex.items():
        if counter not in original.items():
            incorrect += 1

    return incorrect


if __name__ == "__main__":

    # unsure if this works, computer needs to restart Python3 libaries not loading
    origItems = []
    origPrices = []
    alexItems = []
    alexPrices = []

    originalCount = int(input("Original count: "))
    alexCount = int(input("Alex count: "))

    for _ in range(originalCount):
        origItems.append(str(input("Input origItems #%s: " % (_+1))))
        origPrices.append(float(input("Input origPrices #%d: " % (_+1))))

    for _ in range(alexCount):
        alexItems.append(str(input("Input alexItems #%s: " % (_+1))))
        alexPrices.append(float(input("Input alexPrices #%d: " % (_+1))))

    print("Amount incorrect made by Alex: ",
          verifyItems(origItems, origPrices, alexItems, alexPrices))
