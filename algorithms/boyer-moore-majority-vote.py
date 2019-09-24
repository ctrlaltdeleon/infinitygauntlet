"""
@author: acfromspace
"""


def boyer_moore_majority_vote(data):
    counter = 0
    for index in data:
        if counter == 0:
            most = index
        counter += (1 if most == index else -1)
        # If more than half the elements are a common element, return the answer.
        if counter > len(data)/2:
            return most
    return most


data = [1, 2, 3, 2, 2, 3, 1, 1, 1, 2, 1]
print("boyer_moore_majority_vote():", boyer_moore_majority_vote(data))
