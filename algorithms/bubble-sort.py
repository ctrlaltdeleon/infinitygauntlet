# This version is more efficient than standard due to checking if sorted or not


def bubbleSort(data):

    lastIndex = len(data) - 1
    # Checks last step to see if it was the last needed step
    earlyExit = False

    while lastIndex > 0 and not earlyExit:
        for index in range(lastIndex):
            if data[index] > data[index + 1]:
                data[index], data[index + 1] = data[index + 1], data[index]
                earlyExit = False
            else:
                earlyExit = True
        lastIndex -= 1

    print("Early Exit: ", earlyExit, " | ", len(data) - lastIndex, " Passes")


testList = [9, 5, 1]

print(testList)
bubbleSort(testList)
print(testList, "\n")

print(testList)
bubbleSort(testList)
print(testList)
