"""
Make a function that returns 'apples' if given a string,
'oranges' if given an integer, and 'bananas' if given
anything else.

>>>> fruit_labeler(4)
oranges
"""

def fruit_labeler(thing):
    if type(thing) == type(""):
        return "apples"
    elif type(thing) == type(1):
        return "oranges"
    else:
        return "bananas"

print(fruit_labeler(4))
print(fruit_labeler("joji"))
print(fruit_labeler(2.2))

"""
oranges
apples
bananas
"""