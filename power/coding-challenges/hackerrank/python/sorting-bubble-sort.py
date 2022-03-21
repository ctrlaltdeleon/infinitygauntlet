def count_swaps(a):
    swaps = 0
    for index in a:
        for index in range(len(a)-1):
            if a[index] > a[index+1]:
                a[index], a[index+1] = a[index+1], a[index]
                swaps += 1
    return print("Array is sorted in %i swaps.\nFirst Element: %i\nLast Element: %i" % (swaps, a[0], a[-1]))

n = int(input("Input number of values in list: "))
a = list(map(int, input("Input the values in list: ").rstrip().split()))
count_swaps(a)

"""
Input number of values in list: 5
Input the values in list: 1 5 4 3 2
Array is sorted in 6 swaps.
First Element: 1
Last Element: 5
"""