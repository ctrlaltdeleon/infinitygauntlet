"""
Make a function gerund_infinitive that, given a string ending in "ing",
returns the rest of the string prefixed with "to ". If the string
doesn't end in "ing", return "That's not a gerund!"

>>>> gerund_infinitive("building")
to build
>>>> gerund_infinitive("build")
That's not a gerund!
"""

def gerund_infinitive(string):
    # Add code here that returns the answer.
    if string[-3:] == "ing":
        return "to " + string[:-3]
    else:
        return "That's not a gerund!"

# Add more statements to test what your function does:
print(gerund_infinitive("building"))
print(gerund_infinitive("build"))

"""
to build
That's not a gerund!
"""