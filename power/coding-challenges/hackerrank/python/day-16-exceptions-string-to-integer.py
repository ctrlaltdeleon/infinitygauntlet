def is_bad_string(S):
    try:
        print(int(S))
    except:
        print("Bad String")

S = input("Input: ").strip()
is_bad_string(S)

"""
Input: Yeehaw
Bad String

Input: 123
123
"""

"""
NOTE: Hackerrank has a weird time compiling, needs to be strict w/o comments and with exception handles
Accepted answer on Hackerrank:

S = input().strip()

try:
    print(int(S))
except:
    print("Bad String")
"""