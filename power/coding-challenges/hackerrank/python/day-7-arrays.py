def reversal(arr):
    arr.reverse()
    solution = ' '.join(str(_) for _ in arr)
    return solution

n = int(input())
arr = list(map(int, input().rstrip().split()))
print(reversal(arr))

"""
4
1 4 3 2
2 3 4 1
"""

"""
print(" ".join(map(str, arr[::-1])))
"""