"""
Created 3/6/2018

@author: acfromspace
"""

import re

rows, cols = map(int, input().split())

list_holder, sentence = [], ""

# puts all characters into list_holder
for counter1 in range(rows):
    list_holder.append(input())

# zip links the data structures that are being argued into 1 data structure, placement intact
for counter2 in zip(*list_holder):
    sentence += "".join(counter2)
    
# prints sentence without the specified characters
# re.sub(pattern, repl, string, count=0, flags=0)
# re = regular expression
# sub = subtract
# pattern = what's taken out (r"" = raw string notation)
# [^] = all the characters that are NOT in the set will be matched
# []+ = catches all repetitions, not just the first case
# \b = beginning/ending whitespace or a non-alphanumeric, non-underscore Unicode character
# repl = replaces what's taken out with what's passed
# string = the string being scanned
# No 4th/5th argument
print(re.sub(r"\b[^a-zA-Z0-9]+\b", " ", sentence))