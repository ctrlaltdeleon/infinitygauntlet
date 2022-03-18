def left_rotation(list_data, rotations):
    left = rotations % len(list_data)
    return list_data[left:] + list_data[:left]

numbers_and_rotations = input(
    "Input number of integers used and number of rotations separated by a space: ").split()
numbers = int(numbers_and_rotations[0])
rotations = int(numbers_and_rotations[1])
list_data = list(
    map(int, input("Input the integers separated by space(s): ").rstrip().split()))
print("left_rotation():", left_rotation(list_data, rotations))

"""
Input number of integers used and number of rotations separated by a space: 2 2
Input the integers separated by space(s): 1 2 3 4
left_rotation(): [3, 4, 1, 2]
"""