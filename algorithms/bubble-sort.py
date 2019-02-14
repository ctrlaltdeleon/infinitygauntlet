def bubbleSort(arr):

    lastIndex = len(arr)
    earlyExit = False
    while lastIndex > 0 and not earlyExit:
        for index in range(lastIndex - 1):
            if arr[index] >= arr[index + 1]:
                arr[index], arr[index + 1] = arr[index + 1], arr[index]
                earlyExit = False
            else:
                earlyExit = True
        lastIndex -= 1
    print("Early Exit: ", earlyExit, " | ", len(arr) - lastIndex, " Passes")


testList = [9, 5, 1]

print(testList)
bubbleSort(testList)
print(testList, "\n\n")

print(testList)
bubbleSort(testList)
print(testList)
