from collections import Counter


"""
@author: acfromspace
"""


def retrieveMost(literatureText, wordsToExclude):

    maximum = 0
    solution = []

    # Make string into a list of strings
    indexLiterature = literatureText.split()

    # Iterate through list, transform into dictionary with only exclusive words
    indexLiterature = Counter([
        word for word in indexLiterature if word not in wordsToExclude]).most_common()

    # Create a dictionary
    dct = dict(indexLiterature)

    # Only find the most used words
    for key, value in dct.items():
        if value >= maximum:
            solution.append(key)
            maximum = value

    return " ".join(solution)


if __name__ == "__main__":

    literatureText = "romeo oh romeo boi where art thou boi nice alright alright ok hello"
    wordsToExclude = ["oh", "art", "thou"]

    print("Most used words:", retrieveMost(literatureText, wordsToExclude))
