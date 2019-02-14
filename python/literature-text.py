from collections import Counter


def retrieveMost(literatureText, wordsToExclude):

    newList = []

    indexLiterature = literatureText.split()

    newList = " ".join(
        [word for word in indexLiterature if word not in wordsToExclude])

    # dictionary
    tally = Counter(newList.split()).most_common()

    # need to find most occurrences of all words, not just 1
    return tally[0][0]


if __name__ == "__main__":

    literatureText = "romeo oh romeo boi where art thou boi"
    wordsToExclude = ["oh", "art", "thou"]

    print(retrieveMost(literatureText, wordsToExclude))
