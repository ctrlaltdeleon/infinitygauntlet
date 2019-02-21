"""
@author: acfromspace
"""


class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber

    def printPerson(self):
        print("Name:", self.lastName + ",", self.firstName)
        print("ID:", self.idNumber)


class Student(Person):
    #   Class Constructor
    #
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    #   Write your constructor here
    def __init__(self, firstName, lastName, idNumber, testScores):
        # Better to obtain the superclass or the "parent" to reduce lines
        # Person.__init__(self, firstName, lastName, id)
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber
        self.testScores = testScores

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    #   Write your function here
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
# numScores = int(input("Input (numScores): "))  # not needed for Python
scores = list(map(int, input("Input list of scores: ").split()))
# Input values into the subclass
s = Student(firstName, lastName, idNum, scores)
# Controlled by superclass "person"
s.printPerson()
# Controlled by subclass "student"
print("Grade:", s.calculate())
