"""
Make a function aardvark that, given a string, returns 'aardvark'
if the string starts with an a.  Otherwise, return 'zebra'.

>>>> aardvark("arg")
aardvark
>>>> aardvark("Trinket")
zebra
"""

def aardvark(string):
    # Add code here that returns the answer.
    if string[0] == "a" or string[0] == "A":
        return "aardvark"
    else:
        return "zebra"

# Add print statements here to test what your code does:
print(aardvark("arg"))
print(aardvark("Trinket"))

"""
aardvark
zebra
"""