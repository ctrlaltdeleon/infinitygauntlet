"""
@author: acfromspace
"""

if __name__ == '__main__':

    amount = int(input("Amount of students: "))
    python_students = []
    secondhighest = 0

    for _ in range(amount):
        python_students.append([input("Name: "), float(input("Score: "))])

    # sorts highest value to lowest value according to [1] spot
    python_students.sort(key=lambda x: float(x[1]), reverse=True)

    # find the secondlowest value only then break or else it'll keep looking for lower values
    for counter in range(amount-1, -1, -1):
        if python_students[counter][1] > python_students[-1][1]:
            secondhighest = python_students[counter][1]
            break
    # print all names associated with "secondlowest"
    for counter in range(amount-1, -1, -1):
        if python_students[counter][1] == secondhighest:
            print(python_students[counter][0])

# Simpler solution in specifics to the sorts

#     amount = int(input())
#     students = []

#     for counter in range(amount):
#         students.append([input(), float(input())])

# Make a list of all the score values and sort them
#     scores = list(set([students[x][1] for x in range(amount)]))
#     scores.sort()

# Create a list of students with the second lowest score
#     students = [x[0] for x in students if x[1] == scores[1]]
#     students.sort()

#     for counter in students:
#         print(counter)
