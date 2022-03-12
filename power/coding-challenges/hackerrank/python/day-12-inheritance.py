"""
@author: acfromspace
"""

class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber

    def print_person(self):
        print("Name:", self.lastName + ",", self.firstName)
        print("ID:", self.idNumber)


class Student(Person):
    def __init__(self, firstName, lastName, idNumber, testScores):
        # Better to obtain the superclass or the "parent" to reduce lines.
        # Person.__init__(self, firstName, lastName, id)
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber
        self.testScores = testScores

    def calculate(self):
        solution = mean(scores)
        if solution >= 90:
            return "O"
        elif solution >= 80:
            return "E"
        elif solution >= 70:
            return "A"
        elif solution >= 55:
            return "P"
        elif solution >= 40:
            return "D"
        else:
            return "T"


from statistics import mean
line = input("""Input (firstName,lastName,idNum) split by ",": """).split(",")
firstName = line[0]
lastName = line[1]
idNum = line[2]
scores = list(map(int, input("Input list of scores: ").split()))
s = Student(firstName, lastName, idNum, scores)
s.print_person()
print("Grade:", s.calculate())
