# AMAZON

## Round 1 (Online)

- 1.5 hours, breaks in between.
- 20 minutes for code debugging. (Java, C, C++)
- 35 minutes for logic problems.
- Behavioral survey on your work style.
- Interview survey on the application process.

## Round 2 (Online)

- 3 hours, breaks in between.
- 120 minutes for work simulation. (Videos, Decisions)
- 70 minutes for coding. (Java, Python, C#, C++)
- **Literature Text.** Given a list of words and excluded words, find the most common words without the excluded words.

```py
"""
@author: acfromspace
"""

from collections import Counter


def retrieve_most(literature_text, excluded_words):
    maximum = 0
    solution = []
    # Make string into a list of strings.
    list_literature_text = literature_text.split()
    # Iterate through list, transform into dictionary with only exclusive words.
    list_literature_text = Counter([
        word for word in list_literature_text if word not in excluded_words]).most_common()
    # Create a dictionary.
    dict_literature_text = dict(list_literature_text)
    # Only find the most used words.
    for key, value in dict_literature_text.items():
        if value >= maximum:
            solution.append(key)
            maximum = value
    return " ".join(solution)


literature_text = "romeo oh romeo boi where art thou boi nice alright alright ok hello"
excluded_words = ["oh", "art", "thou"]
print("retrieve_most():", retrieve_most(literature_text, excluded_words))

"""
Output:

retrieve_most(): romeo boi alright
"""
```

- **Nearest Crates.** Given a list of coordinates (list of lists), find the nearest crates depending on capacity.

```py
"""
@author: acfromspace
"""

import math


def compute_euclidean_distance(x1, y1, x2, y2):
    # Calculates the distance from the truck.
    return math.sqrt(((x1-x2)**2)+((y1-y2)**2))


def nearest_crates(total_crates, all_locations, truck_capacity):
    distances = []
    # Retrieve all distances then sort the distances from smallest to biggest.
    for point in all_locations:
        # Distance from crate's point to origin point (can customize).
        distance = compute_euclidean_distance(
            point[0], point[1], 0, 0)
        distances.append([point, distance])
    else:
        distances.sort(key=lambda element: element[-1])
    # Obtain the truck_capacity crates to load.
    nearest = [distances[i][0] for i in range(0, truck_capacity)]
    return nearest


total_crates = 3
all_locations = [[6, 3], [2, 1], [5, 2], [3, 2], [9, 0], [-1, 1]]
truck_capacity = 2
neighbors = nearest_crates(total_crates, all_locations, truck_capacity)
print("nearest_crates():", neighbors)

"""
Output:

nearest_crates(): [[-1, 1], [2, 1]]
"""
```

- Interview survey on the application process.

## Round 3 (Phone)

- Did not make it.
