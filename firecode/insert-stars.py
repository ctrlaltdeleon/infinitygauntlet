"""
@author: acfromspace
"""


def insert_star_between_pairs(a_string):
    # No string? No stars
    if a_string is None:
        return None
    # Just one character? Can't insert stars
    elif len(a_string) <= 1:
        return a_string
    # Check index and the index+2, if the same, insert the star
    # Reason why we do recursion is what if there's two stars together? Endless loop!
    # Therefore we check the new string away from the stars
    elif a_string[0:1] == a_string[1:2]:
        return a_string[0:1] + "*" + insert_star_between_pairs(a_string[1:len(a_string)])

    return a_string[0:1] + insert_star_between_pairs(a_string[1:len(a_string)])


a_string = "abbba"
print(insert_star_between_pairs(a_string))
