def maximum_toys(prices, k):
    prices.sort()
    cart = []
    for index in prices:
        if sum(cart)+index < k:
            cart.append(index)
    return len(cart)

if __name__ == '__main__':
    nk = input("Input number of items and budget: ").split()
    n = int(nk[0])
    k = int(nk[1])
    prices = list(
        map(int, input("Input the value of each item: ").rstrip().split()))
    print("maximum_toys():", maximum_toys(prices, k))

"""
Input number of items and budget: 5 20
Input the value of each item: 5 10 20 30 5 5
maximum_toys(): 3
"""