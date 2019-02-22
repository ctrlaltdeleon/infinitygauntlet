"""
@author: acfromspace
"""

import sys


class Solution:
    def __init__(self):
        self.stack = []
        self.queue = []

    def push_character(self, ch):
        self.stack.append(ch)

    def enqueue_character(self, ch):
        self.queue.insert(0, ch)

    def pop_character(self):
        return self.stack.pop()

    def dequeue_character(self):
        return self.queue.pop()


s = input("Input a string to see if it's a palindrome: ")
obj = Solution()
l = len(s)
for i in range(l):
    obj.push_character(s[i])
    obj.enqueue_character(s[i])
isPalindrome = True

'''
Pop the top character from stack
Dequeue the first character from queue
Compare both the characters
'''

for i in range(l // 2):
    if obj.pop_character() != obj.dequeue_character():
        isPalindrome = False
        break
if isPalindrome:
    print("The word, "+s+", is a palindrome.")
else:
    print("The word, "+s+", is not a palindrome.")
