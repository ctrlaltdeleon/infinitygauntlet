"""
@author: acfromspace
"""

# Make a function commafy that, given a list of three or more things,
# returns a list with commas.
#
# >>>> commafy(["trinket", "learning", "fun"])
# trinket, learning, and fun
# >>>> commafy(["lions", "tigers", "bears"])
# lions, tigers, and bears


def commafy(list):
    # Add code here that returns the answer.
    return ", ".join(list[:-1]) + ", and " + list[-1]


# Add print statements here to test what your code does:
print(commafy(["trinket", "learning", "fun"]))
print(commafy(["lions", "tigers", "bears"]))
