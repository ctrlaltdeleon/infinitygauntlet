from collections import Counter

def check_magazine(magazine, note):
    if (Counter(note) - Counter(magazine)) != {}:
        return print("No")
    return print("Yes")

magazine = input("Insert words available in magazine: ").rstrip().split()
note = input("Insert ransom note: ").rstrip().split()
print("check_magazine():", check_magazine(magazine, note))

"""
Insert words available in magazine: hey this is god speaking
Insert ransom note: is you good
No
check_magazine(): None
"""