"""
@author: acfromspace
"""

"""
Notes:

Find the most common word from a paragraph that can't be a banned word.
"""

from collections import Counter


class Solution:
    def most_common_word(self, paragraph: str, banned: [str]) -> str:
        unbanned = []

        for character in "!?',;.":
            paragraph = paragraph.replace(character, " ")

        paragraph_list = paragraph.lower().split()

        for word in paragraph_list:
            if word not in banned:
                unbanned.append(word)

        # Get the `most_common` element, which holds a key value, which then we need the key.
        return Counter(unbanned).most_common(1)[0][0]


test = Solution()
paragraph = "kraq and jeff are talking about the problems with kraq jeff JEFF KRAQ are"
banned = "jeff kraq"
print("most_common_word():", test.most_common_word(paragraph, banned))

"""
Time complexity: O(p+b). "p" is the size of the `paragraph` and "b" is the size of `banned`.

Space complexity: O(p+b). To store the `paragraph_list` and the `banned` data structures.
"""
