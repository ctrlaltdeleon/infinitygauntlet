"""
@author: acfromspace
"""


def runnerup(arr):

    # # doesn't work for all cases and complexities go beyond

    # maximum = 0
    # runnerup = 0

    # for counter in arr:
    #     if counter > maximum:
    #         runnerup = maximum
    #         maximum = counter
    #     if counter > runnerup and counter != maximum:
    #         runnerup = counter

    # return runnerup

    # Always try sorting the set then apply the knowledge
    # We use sets because no duplicate elements are allowed
    # So be weary of duplicate data structures where duplicates matter

    runnerup = sorted(arr)[-2]

    return runnerup


if __name__ == '__main__':
    n = int(input("Number of elements: "))
    arr = set(map(int, input("Array elements: ").split()))

    print(runnerup(arr))
