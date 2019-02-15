"""
@author: acfromspace
"""

import math


def compute_euclidean_distance(x1, y1, x2, y2):

    return math.sqrt(((x1-x2)**2)+((y1-y2)**2))


def nearestCrates(totalCrates, allLocations, truckCapacity):

    distances = []

    for point in allLocations:
        distance = compute_euclidean_distance(
            point[0], point[1], 0, 0)
        distances.append([point, distance])
    else:
        distances.sort(key=lambda element: element[-1])

    nearest = [distances[i][0] for i in range(0, truckCapacity)]

    return nearest


if __name__ == "__main__":

    totalCrates = 3
    allLocations = [[6, 3], [2, 1], [5, 2], [3, 2], [9, 0], [-1, 1]]
    truckCapacity = 2
    neighbors = nearestCrates(totalCrates, allLocations, truckCapacity)
    print(neighbors)
