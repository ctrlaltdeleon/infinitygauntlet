def hourglass_sum(list_data):
    sum = []
    # 4x4 = 16 solutions.
    for row in range(len(list_data)-2):
        for col in range(len(list_data)-2):
            # This is the hourglass shape.
            sum.append(list_data[row][col] + list_data[row][col+1] + list_data[row][col+2] + list_data[row+1]
                       [col+1] + list_data[row+2][col] + list_data[row+2][col+1] + list_data[row+2][col+2])
    return max(sum)

list_data = []
for _ in range(6):
    # Input should be a 6 by 6 2D array.
    list_data.append(list(map(int, input(
        """Input row %i (6 integers, for example: "1 2 3 4 5 6"): """ % (_+1)).rstrip().split())))
print("hourglass_sum():", hourglass_sum(list_data))

"""
Input row 1 (6 integers, for example: "1 2 3 4 5 6"): 1 2 3 4 5 6
Input row 2 (6 integers, for example: "1 2 3 4 5 6"): 4 5 6 7 8 9 
Input row 3 (6 integers, for example: "1 2 3 4 5 6"): 1 2 3 4 5 6 
Input row 4 (6 integers, for example: "1 2 3 4 5 6"): 3 4 5 6 7 8
Input row 5 (6 integers, for example: "1 2 3 4 5 6"): 2 3 4 5 6 7
Input row 6 (6 integers, for example: "1 2 3 4 5 6"): 1 2 3 4 5 6
hourglass_sum(): 50

Input row 1 (6 integers, for example: "1 2 3 4 5 6"): 0 0 0 0 0 0
Input row 2 (6 integers, for example: "1 2 3 4 5 6"): 1 0 0 0 0 1
Input row 3 (6 integers, for example: "1 2 3 4 5 6"): 1 1 0 0 1 1
Input row 4 (6 integers, for example: "1 2 3 4 5 6"): 1 1 0 0 1 1
Input row 5 (6 integers, for example: "1 2 3 4 5 6"): 1 0 0 0 0 1
Input row 6 (6 integers, for example: "1 2 3 4 5 6"): 0 0 0 0 0 0
hourglass_sum(): 4
"""