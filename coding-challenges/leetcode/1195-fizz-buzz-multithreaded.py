"""
@author: acfromspace
"""

"""
Notes:

Implement a multi-threaded version of FizzBuzz with four threads.
"""

import threading


class FizzBuzz(object):
    def __init__(self, n):
        self.n = n + 1
        self.f = threading.Semaphore(0)
        self.b = threading.Semaphore(0)
        self.fb = threading.Semaphore(0)
        self.nn = threading.Semaphore(1)
        self.cur = 1

    def fizz(self, printFizz: 'Callable[[], None]') -> None:
        for index in range(1, self.n):
            if index % 3 == 0 and index % 5:
                self.f.acquire()
                printFizz()
                self.cur += 1
                if self.cur % 5 == 0:
                    self.b.release()
                else:
                    self.nn.release()

    def buzz(self, printBuzz: 'Callable[[], None]') -> None:
        for index in range(1, self.n):
            if index % 5 == 0 and index % 3:
                self.b.acquire()
                printBuzz()
                self.cur += 1
                if self.cur % 3 == 0:
                    self.f.release()
                else:
                    self.nn.release()

    def fizzbuzz(self, printFizzBuzz: 'Callable[[], None]') -> None:
        for index in range(1, self.n):
            if index % 5 == 0 and index % 3 == 0:
                self.fb.acquire()
                printFizzBuzz()
                self.cur += 1
                self.nn.release()

    def number(self, printNumber: 'Callable[[int], None]') -> None:
        for index in range(1, self.n):
            if index % 5 and index % 3:
                self.nn.acquire()
                printNumber(index)
                self.cur += 1
                if self.cur % 3 == 0 and self.cur % 5 == 0:
                    self.fb.release()
                elif self.cur % 3 == 0:
                    self.f.release()
                elif self.cur % 5 == 0:
                    self.b.release()
                else:
                    self.nn.release()


"""
Time complexity: O(?). Multi-threading lol.

Space complexity: O(?). Multi-threading lol. 
"""
