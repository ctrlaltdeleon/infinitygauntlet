"""
@author: acfromspace
"""


class FizzBuzz:

    def output(self):
        for i in range(1, 101):
            string = ""
            if i % 3 == 0:
                string += "Fizz"
            if i % 5 == 0:
                string += "Buzz"
            print(i, string)


# create object from class solution
test_object = FizzBuzz()

test_object.output()
