"""
@author: acfromspace
"""

import math


class TravelDistanceCalculator:
    def __init__(self):
        self.locations = {}

    def travel_distance(self, line):
        function = line.split(":")[0]

        if function == "LOC":
            return self.loc_update(line)
        elif function == "TRIP":
            return self.trip_update(line)
        else:
            return "INVALID"

    def loc_update(self, line):
        location, latitude, longitude = line.split(":")[1:]
        latitude = float(latitude)
        longitude = float(longitude)

        self.locations.update(
            {location: {"latitude": latitude, "longitude": longitude}})

        return "Location updated! " + line

    def trip_update(self, line):
        account, depart, arrive = line.split(":")[1:]

        if depart in self.locations.keys():
            if arrive in self.locations.keys():
                distance = self.distance_calculation(depart, arrive)
                return ":".join([account, depart, arrive, str(distance)])

        return "INVALID"

    def distance_calculation(self, depart, arrive):
        # Earth's radius in miles.
        radius = 3963
        lat1 = math.radians(self.locations[depart]["latitude"])
        lat2 = math.radians(self.locations[arrive]["latitude"])
        long1 = math.radians(self.locations[depart]["longitude"])
        long2 = math.radians(self.locations[arrive]["longitude"])

        beta = abs(long1 - long2)
        alpha = math.acos(math.sin(lat1) * math.sin(lat2) +
                          math.cos(lat1) * math.cos(lat2) * math.cos(beta))
        distance = radius * alpha
        return int(distance)


t = TravelDistanceCalculator()
print("travel_distance():", t.travel_distance("LOC:CHI:41.836944:-87.684722"))
print("travel_distance():", t.travel_distance("LOC:NYC:40.7127:-74.0059"))
print("travel_distance():", t.travel_distance("LOC:LA:34.0522:-118.2437"))
print("travel_distance():", t.travel_distance("LOC:TOKYO:35.6762:139.6503"))
print("travel_distance():", t.travel_distance("LOC:SANDIEGO:32.7157:-117.1611"))
print("travel_distance():", t.travel_distance("TRIP:C0FFEE1C:CHI:NYC"))
print("travel_distance():", t.travel_distance("TRIP:C0FFEE1C:SANDIEGO:TOKYO"))
print("travel_distance():", t.travel_distance("TRIP:C0FFEE1C:SANDIEGO:LA"))
