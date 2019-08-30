def isPossible(a, b, c, d):
    print("test")
    pairs = []
    pairs.append([a, b])
    while len(pairs) > 0:
        print("tesst1")
        print(pairs[0][1])
        if pairs[0] == [c, d]:
            return "Yes"
        sumo = pairs[0][0] + pairs[0][1]
        if sumo <= c:
            pairs.append([sumo, pairs[0][1]])
        if sumo <= d:
            pairs.append([pairs[0][1], sumo])
        pairs.pop(0)
    return "No"


isPossible(1, 4, 5, 9)
