def alternating_characters(s):
    deletions = 0
    for index, character in enumerate(s[:-1]):
        if s[index+1] == character:
            deletions += 1
    return deletions

q = int(input("Input number of strings: "))
for q_itr in range(q):
    s = input("Input string %i: " % (q_itr+1))
    print("alternating_characters():", alternating_characters(s))

"""
Input number of strings: 2
Input string 1: hello
alternating_characters(): 1
Input string 2: yeehaw
alternating_characters(): 1
"""