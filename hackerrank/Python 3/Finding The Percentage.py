"""
@author: acfromspace
"""


def lastAverage(student_marks, query_name):

    return print("Average: %.2f" % (sum(student_marks[query_name])/len(student_marks[query_name])))


if __name__ == '__main__':

    n = int(input("Input amount of students: "))

    student_marks = {}

    for _ in range(n):
        name, * \
            line = input(
                "Input name of student and following scores with spaces in between: ").split()
        scores = list(map(float, line))
        student_marks[name] = scores

    query_name = input("Input name of student to find average of: ")

    lastAverage(student_marks, query_name)
