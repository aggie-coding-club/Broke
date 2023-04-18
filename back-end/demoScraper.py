from googleMapScraper import *
from uberEats import *

import time

import sys

def findLocations(locationType, item, address, radius):    
    time.sleep(100)
    return {'McDad': ('Burger', 10.99, 'College Station'), 'Store2': ('Sammy', 20.36, 'My address')}
    if locationType == 'gas':
        pass
    elif locationType == 'drink' or locationType == 'food':
        locationCandidates = googleMap(item, address)

        filtered_stores = distanceFunct(locationCandidates, radius, address)

        final_items = uberEats(filtered_stores.keys(), item, address)   

        print(final_items)  

#findLocations('food', 'burger', '2604 Zambia Dr, Cedar Park', 5)