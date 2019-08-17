# <-- EXPAND to see the data classes
import fileinput
import math


class Event:

    def __init__(self, event_type, occurrences, biz_id):
        self.event_type = event_type
        self.occurrences = occurrences
        self.biz_id = biz_id


def find_active_businesses(events):
    active_businesses = []
    ads_average, ads_number = 0
    page_views_average, page_views_number = 0
    photos_views_average, photo_views_number = 0
    reviews_average, reviews_number = 0

    for index in range(len(events)):
        if events.index.event_type == "ads" and events.index.occurrences > 0:
            ads_average += events.index.occurrences
            ads_number += 1
        if events.index.event_type == "page_views" and events.index.occurrences > 0:
            page_views_average += events.index.occurrences
            page_views_number += 1
        if events.index.event_type == "photo_views" and events.index.occurrences > 0:
            photos_views_average += events.index.occurrences
            photo_views_number += 1
        if events.index.event_type == "reviews" and events.index.occurrences > 0:
            reviews_average += events.index.occurrences
            reviews_number += 1
    ads_average = ads_average/ads_number
    page_views_average = page_views_average/page_views_number
    photos_views_average = photos_views_average/photos_views_number
    reviews_average = reviews_average/reviews_number

    for index in range(len(events)):
        biz_ids = []
        if events.index.biz_id != biz_ids:
            biz_ids.append(events.index.biz_id)
        # Compare if the business has more than 2 event types.
        # Compare if the business has a greater than average number.
        active_businesses.append(biz_id)  # If it applies.

    return active_businesses


if __name__ == "__main__":
    lines = [line.strip() for line in list(fileinput.input())]
    events = [
        Event(line.split()[0], int(line.split()[1]), int(line.split()[2]))
        for line in lines
    ]
    active_businesses = find_active_businesses(events)
    for biz_id in active_businesses:
        print(biz_id)
