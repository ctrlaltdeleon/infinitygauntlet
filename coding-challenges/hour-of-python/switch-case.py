"""
@author: acfromspace
"""

# Make a function switch_case that, given a string,
# returns the string with uppercase letters in lowercase
# and vice-versa. Include punction and other non-cased
# characters unchanged.
#
# >>>> switch_case("Arg!")
# aRG!
# >>>> switch_case("TrInKeT")
# tRiNkEt


def switch_case(string):
    # Add code here that returns the answer.
    new = ""
    for letter in string:
        new += letter.lower() if letter.isupper() else letter.upper()
    return new


# Add print statements to check what your code does:
print(switch_case("Arg!"))
print(switch_case("TrInKeT"))
