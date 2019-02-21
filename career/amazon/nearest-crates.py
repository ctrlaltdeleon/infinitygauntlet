"""
@author: acfromspace
"""

import math


def compute_euclidean_distance(x1, y1, x2, y2):
    # Calculates the distance from the truck
    return math.sqrt(((x1-x2)**2)+((y1-y2)**2))


def nearest_crates(total_crates, all_locations, truck_capacity):
    distances = []
    # Retrieve all distances then sort the distances from smallest to biggest
    for point in all_locations:
        # Distance from crate[point] to origin point (can customize)
        distance = compute_euclidean_distance(
            point[0], point[1], 0, 0)
        distances.append([point, distance])
    else:
        distances.sort(key=lambda element: element[-1])
    # Obtain the truck_capacity crates to load
    nearest = [distances[i][0] for i in range(0, truck_capacity)]
    return nearest


total_crates = 3
all_locations = [[6, 3], [2, 1], [5, 2], [3, 2], [9, 0], [-1, 1]]
truck_capacity = 2
neighbors = nearest_crates(total_crates, all_locations, truck_capacity)
print(neighbors)
