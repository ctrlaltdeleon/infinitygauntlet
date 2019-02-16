# Standard O(n^2) complexity solution
def bubbleSort1(data):
    for i in range(len(data)-1, 0, -1):
        for j in range(i):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
    return data


def bubbleSort2(data):
    # This version is more efficient than standard due to checking if sorted or not

    # lastIndex is here to keep check of amount of passes, not needed for bubble sort
    lastIndex = len(data) - 1
    # Checks last step to see if it was the last needed step
    isSorted = False

    while lastIndex > 0 and not isSorted:
        for i in range(lastIndex):
            if data[i] > data[i + 1]:
                data[i], data[i + 1] = data[i + 1], data[i]
                isSorted = False
            else:
                isSorted = True
        lastIndex -= 1

    print("Early Exit: ", isSorted, " | ", len(data) - lastIndex, " Passes")


def bubbleSort3(data):
    isSorted = False
    while not isSorted:
        isSorted = True
        for i in range(len(data)-1):
            if data[i] > data[i+1]:
                data[i], data[i+1] = data[i+1], data[i]
                isSorted = False
    return data


testList = [9, 5, 1, 3, 6, -2, -8]
print(testList)
bubbleSort1(testList)
print(testList, "\n")

testList = [9, 5, 1, 3, 6, -2, -8]
print(testList)
bubbleSort2(testList)
print(testList, "\n")

testList = [9, 5, 1, 3, 6, -2, -8]
print(testList)
bubbleSort3(testList)
print(testList)
