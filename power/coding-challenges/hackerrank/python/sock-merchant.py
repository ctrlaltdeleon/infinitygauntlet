def sock_merchant(n, ar):
    stock = set()
    pairs = 0
    for socks in ar:
        if socks in stock:
            stock.remove(socks)
            pairs += 1
        else:
            stock.add(socks)
    return pairs

n = int(input("Number of socks: "))
ar = list(
    map(int, input("Different socks (spaces in between): ").rstrip().split()))
print("sock_merchant():", sock_merchant(n, ar))

"""
Number of socks: 10
Different socks (spaces in between): 1 2 2 2 1 2 2 2 1 2
sock_merchant(): 4
"""