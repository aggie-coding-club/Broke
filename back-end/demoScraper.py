from googleMapScraper import *

def findLocations(locationType, item, address, radius):
    if locationType == 'gas':
        pass
    elif locationType == 'drink' or locationType == 'food':
        locationCandidates = googleMap(item, address)

        filtered_stores = distanceFunct(locationCandidates, radius, address)