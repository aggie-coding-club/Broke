from googleMapScraper import *
from uberEats import *

import sys

def findLocations(locationType, item, address, radius):
    if locationType == 'gas':
        pass
    elif locationType == 'drink' or locationType == 'food':
        locationCandidates = googleMap(item, address)

        filtered_stores = distanceFunct(locationCandidates, radius, address)

        final_items = uberEats(filtered_stores.keys(), item, address)

        print(final_items)

findLocations('food', 'burger', '2604 Zambia Dr, Cedar Park', 5)