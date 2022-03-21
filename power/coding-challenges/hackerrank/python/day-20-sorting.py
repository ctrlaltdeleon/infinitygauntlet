n = int(input("Input number of integers to input: ").strip())
a = list(map(int, input(
    "Input integers elements with spaces in between: ").strip().split(' ')))
data = len(a) - 1
swaps = 0
while data > 0:
    for i in range(data):
        if a[i] > a[i+1]:
            a[i], a[i+1] = a[i+1], a[i]
            swaps += 1
    data -= 1

print("Array is sorted in " + str(swaps) + " swaps.")
print("First Element: " + str(a[0]))
print("Last Element: " + str(a[-1]))
print("Array: " + str(a))

"""
Input number of integers to input: 3
Input integers elements with spaces in between: 10 20 30
Array is sorted in 0 swaps.
First Element: 10
Last Element: 30
Array: [10, 20, 30]
"""