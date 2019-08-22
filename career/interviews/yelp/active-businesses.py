import fileinput


class Event:

    def __init__(self, event_type, occurrences, biz_id):
        self.event_type = event_type
        self.occurrences = occurrences
        self.biz_id = biz_id


def find_active_businesses(events):
    active_businesses, secondary, preliminary = [], [], []
    ads_average, ads_number = 0, 0
    page_views_average, page_views_number = 0, 0
    photos_views_average, photo_views_number = 0, 0
    reviews_average, reviews_number = 0, 0

    # Look for average `occurrences` in `event_type`.
    for event in events:
        if event.event_type == "ads" and event.occurrences > 0:
            ads_average += event.occurrences
            ads_number += 1
        if event.event_type == "page_views" and event.occurrences > 0:
            page_views_average += event.occurrences
            page_views_number += 1
        if event.event_type == "photo_views" and event.occurrences > 0:
            photos_views_average += event.occurrences
            photo_views_number += 1
        if event.event_type == "reviews" and event.occurrences > 0:
            reviews_average += event.occurrences
            reviews_number += 1
        if event.biz_id not in preliminary:
            preliminary.append(event.biz_id)
        else:
            secondary.append(event.biz_id)

    ads_average = ads_average/ads_number
    page_views_average = page_views_average/page_views_number
    photos_views_average = photos_views_average/photo_views_number
    reviews_average = reviews_average/reviews_number

    # Create a list of `biz_id` with >= 2 `event_type`.
    secondary = list(set(secondary))

    # If the `event.occurrences` >= `event_type.occurrence` average, it is an `active_business`.
    for event in events:
        if event.biz_id in secondary:
            if event.event_type == "ads" and event.occurrences >= ads_average:
                active_businesses.append(event.biz_id)
            if event.event_type == "page_views" and event.occurrences >= page_views_average:
                active_businesses.append(event.biz_id)
            if event.event_type == "photos_views" and event.occurrences >= photos_views_average:
                active_businesses.append(event.biz_id)
            if event.event_type == "reviews" and event.occurrences >= reviews_average:
                active_businesses.append(event.biz_id)

    return list(set(active_businesses))


if __name__ == "__main__":
    lines = [line.strip() for line in list(
        fileinput.input("career\interviews\yelp\input2.txt"))]
    events = [
        Event(line.split()[0], int(line.split()[1]), int(line.split()[2]))
        for line in lines
    ]
    active_businesses = find_active_businesses(events)
    for biz_id in active_businesses:
        print(biz_id)
