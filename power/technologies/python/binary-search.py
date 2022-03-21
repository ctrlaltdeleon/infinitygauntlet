

def binarySearch(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        # We do this instead of `mid = (low + high) // 2` due to possible overflow of adding two big numbers.
        mid = low + (high - low) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


arr = [1, 3, 5, 6, 7, 10]
target = 7

result = binarySearch(arr, target)

if result != -1:
    print("Element is present at index \"" + str(result) + "\".")
else:
    print("Element is not present.")
