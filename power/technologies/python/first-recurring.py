

def first_recurring(data):
    seen = []
    for index in data:
        if index not in seen:
            seen.append(index)
        else:
            return index
    return "All unique characters."


data = [1, 2, 3, 3, 2, 1, 3]
print("first_recurring():", first_recurring(data))
