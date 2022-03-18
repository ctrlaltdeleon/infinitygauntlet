def breaking_records(scores):
    mini = maxi = scores[0]
    min_count = max_count = 0
    for index in scores[1:]:
        if index > maxi:
            max_count += 1
            maxi = index
        if index < mini:
            min_count += 1
            mini = index
    return max_count, min_count

scores = [10, 5, 20, 4, 5, 25, 30, 10]
print("breaking_records():", breaking_records(scores))

"""
breaking_records(): (3, 2)
"""