def two_strings(s1, s2):
    return 'YES' if any(substring in s1 for substring in s2) else 'NO'

comparisons = int(input("Number of comparisons to be done: "))
for index in range(comparisons):
    s1 = input("String 1 in iteration %i: " % (index+1))
    s2 = input("String 2 in iteration %i: " % (index+1))
    print("Is there a commonality between the two_strings()?", two_strings(s1, s2))

"""
Number of comparisons to be done: 1
String 1 in iteration 1: hellothere
String 2 in iteration 1: whatareyoudoing
Is there a commonality between the two_strings()? YES
"""