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


def hackland_election(votes):
    # Find the most votes on a person and organize in a dict.
    # Create a class `Counter` using `votes` as the object and using the method `most_common()` to sort the tally.
    tally = Counter(votes).most_common()
    # Returns the first most common given via when inputted, then syntactic output to solve the problem.
    return list([i[0] for i in tally])[0]


ballots = int(input("Number of HackLand Ballots: "))
votes = []
for index in range(ballots):
    votes.append(input("Give a name for ballot #%i: " % (index+1)))
print("hackland_election():", hackland_election(votes))

"""
Output:

Number of HackLand Ballots: 5
Give a name for ballot #1: ac
Give a name for ballot #2: jinsoul
Give a name for ballot #3: ac
Give a name for ballot #4: jinsoul
Give a name for ballot #5: jinsoul
hackland_election(): jinsoul
"""
