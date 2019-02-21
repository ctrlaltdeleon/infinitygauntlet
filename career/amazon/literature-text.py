"""
@author: acfromspace
"""

from collections import Counter


def retrieve_most(literature_text, excluded_words):
    maximum = 0
    solution = []
    # Make string into a list of strings
    list_literature_text = literature_text.split()
    # Iterate through list, transform into dictionary with only exclusive words
    list_literature_text = Counter([
        word for word in list_literature_text if word not in excluded_words]).most_common()
    # Create a dictionary
    dict_literature_text = dict(list_literature_text)
    # Only find the most used words
    for key, value in dict_literature_text.items():
        if value >= maximum:
            solution.append(key)
            maximum = value
    return " ".join(solution)


literature_text = "romeo oh romeo boi where art thou boi nice alright alright ok hello"
excluded_words = ["oh", "art", "thou"]
print("Most used words:", retrieve_most(literature_text, excluded_words))
