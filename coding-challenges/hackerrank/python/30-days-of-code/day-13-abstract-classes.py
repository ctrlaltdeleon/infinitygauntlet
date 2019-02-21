"""
@author: acfromspace
"""

from abc import ABCMeta, abstractmethod


class Book(object, metaclass=ABCMeta):
    def __init__(self, title, author):
        self.title = title
        self.author = author

    @abstractmethod
    def display(self): pass


class MyBook(Book):

    def __init__(self, title, author, price):
        # super(Book, self).__init__()
        # though I like this syntax much more due to readability
        Book.__init__(self, title, author)
        self.price = price

    def display(self):
        print("Title: %s" % (title))
        print("Author: %s" % (author))
        # format to 2 decimal places
        print("Price: $%.2f" % (price))


title = input("Input title of book: ")
author = input("Input author of book: ")
price = float(input("Input price of book: "))
new_novel = MyBook(title, author, price)
new_novel.display()
