

def reverseRecursion(text):
    return text if len(text) <= 1 else reverseRecursion(text[1:]) + text[0]


string = "hello"
print("reverseRecursion():", reverseRecursion(string))

"""
Output:

reverseRecursion(hello)
    = reverseRecursion(ello) + h           # The recursive step
    = reverseRecursion(llo) + e + h
    = reverseRecursion(lo) + l + e + h
    = reverseRecursion(o) + l + l + e + h  # Base case
    = o + l + l + e + h
    = olleh
"""
