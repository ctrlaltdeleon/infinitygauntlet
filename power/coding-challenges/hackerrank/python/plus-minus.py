def plus_minus(arr):
    positive, negative, zero = 0, 0, 0
    for index in arr:
        if index > 0:
            positive += 1
        elif index < 0:
            negative += 1
        else:
            zero += 1
    print(positive/len(arr))
    print(negative/len(arr))
    print(zero/len(arr))

arr = [-4, 3, -9, 0, 4, 1]
plus_minus(arr)

"""
0.5
0.3333333333333333
0.16666666666666666
"""