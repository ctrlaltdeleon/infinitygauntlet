"""
@author: acfromspace
"""

from collections import Counter


def hacklandElection(votes):

    # Find the most votes on a person and organize in a dict
    tally = Counter(votes).most_common()

    # returns the first most common given via when inputted, then syntactic output to solve the problem
    return list([i[0] for i in tally])[0]


if __name__ == "__main__":

    ballots = int(input("Number of HackLand Ballots: "))
    votes = []

    for counter in range(ballots):
        votes.append(input("Give a name for ballot #%i: " % (counter+1)))

    print("Solution:", hacklandElection(votes))
