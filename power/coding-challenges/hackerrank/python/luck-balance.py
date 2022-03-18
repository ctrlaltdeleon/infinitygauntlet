def luck_balance(k, contests):
    contests.sort(reverse=True)
    luck = 0
    for contest in contests:
        if contest[1] == 0:
            luck += contest[0]
        elif k > 0:
            luck += contest[0]
            k -= 1
        else:
            luck -= contest[0]
    return luck

nk = input(
    "Input number of contests and number of important contests to at least lose: ").split()
n = int(nk[0])
k = int(nk[1])
contests = []
for index in range(n):
    contests.append(list(map(int, input(
        "Input points and importance (0 is not important, 1 is) for contest %i: " % (index+1)).rstrip().split())))
print("luck_balance():", luck_balance(k, contests))

"""
Input number of contests and number of important contests to at least lose: 5 2
Input points and importance (0 is not important, 1 is) for contest 1: 5 1
Input points and importance (0 is not important, 1 is) for contest 2: 2 0
Input points and importance (0 is not important, 1 is) for contest 3: 6 0
Input points and importance (0 is not important, 1 is) for contest 4: 3 1
Input points and importance (0 is not important, 1 is) for contest 5: 4 1
luck_balance(): 14
"""