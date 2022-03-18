def designer_door_mat(rows, columns):
    # If you put 5, gives 1, 3.
    for index in range(1, rows, 2):
        print((index * ".|.").center(columns, "-"))

    # Print "WELCOME" in the center surrounded by "-" till there's a total of `len(column)`
    print("WELCOME".center(columns, "-"))

    # If you put 5, gives 3, 1.
    for index in range(rows-2, -1, -2):
        print((index * ".|.").center(columns, "-"))

print("Please input rows and columns:")
rows, columns = map(int, input().split())
designer_door_mat(rows, columns)

"""
Please input rows and columns:
5 5
-.|.-
.|..|..|.
WELCOME
.|..|..|.
-.|.-
"""