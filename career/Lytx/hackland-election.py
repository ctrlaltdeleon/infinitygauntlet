"""
@author: acfromspace
"""

"""
DESCRIPTION:

There are N citizens voting in this year's Hackland election. 
Each voter writes the name of their chosen candidate on a ballot and places it in a ballot box. 
The candidate with the highes number of votes win the election. 
If two or more candidates have the same number of votes, then the tied candidates' names are ordered alphabetically and the last name wins.

Complete the election Winner function in your editor. It has 1 parameter:L an array of strings, votes, describing the votes in the ballot box. 
This function must review these votes and return a string representing the name of the winning candidate.

CONSTRAINTS:

1 <= N <= 10^4

INPUT FORMAT:

["an","array","of","strings"]

OUTPUT FORMAT:

Name of the person who has the max votes. 
If there are multiple people with same number of votes(max) then print the last name.

SAMPLE INPUT 1:

String[] votes = {"Alex", "Michael", "Harry", "Dave", "Michael", "Victor", "Harry", "Alex", "Mary", "Mary"};

SAMPLE OUTPUT 1:

Michael

DESCRIPTION 1: 

votes = {"Alex", "Michael", "Harry", "Dave", "Michael", "Victor", "Harry", "Alex", "Mary", "Mary"} 
Alex, Harry, Michael, and Mary are all tied for the highest number of votes. 
Because Michael is alphabetically last, we return his name as the winner.

SAMPLE INPUT 2:

String[] votes = { "victor", "veronica", "ryan", "dave", "maria", "farah", "farah", "ryan", "veronica" };

SAMPLE OUTPUT 2:

veronica

EXPLANATION 2:

votes = {"Victor", "Veronica", "Ryan", "Dave", "Maria", "Maria", "Farah", "Farah", "Ryan", "Veronica"} 
Veronica, Ryan, Maria, and Farah are all tied for the highest number of votes. 
Because Veronica is alphabetically last, we return her name as the winner.
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
