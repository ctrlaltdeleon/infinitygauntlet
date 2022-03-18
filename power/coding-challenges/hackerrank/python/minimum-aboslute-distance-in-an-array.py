def minimum_absolute_difference(arr):
    arr.sort()
    return min([abs(arr[index+1] - arr[index]) for index in range(len(arr)-1)])

n = int(input("Input number of values: "))
arr = list(
    map(int, input("Values to be finding the minimum absolute difference: ").rstrip().split()))
print("minimum_absolute_difference():", minimum_absolute_difference(arr))

"""
Input number of values: 5
Values to be finding the minimum absolute difference: 2 4 10 20 30
minimum_absolute_difference(): 2
"""