from googleMapScraper import *
from uberEats import *

import time

import sys

def findLocations(locationType: str, item: str, address: str, radius: int) -> dict[str, tuple]:
    """Finds stores within the desired radius that contain\n
    the requested item at the cheapest price

    Parameters
    ----------
    locationType : str
        The item catagory to be searched (food, gas, drink, grocery)
    item : str
        The item that is being requested
    address : str
        The address of the user
    radius : int
        The maxiumum radius (in miles) from the user's address that can be searched

    Returns
    -------
    dict
        Dictionary containing stores that have the desired item along with the\n
        store's name for the item, the price, and the location of the store
    """

    time.sleep(1)
    return {'McDad': ('Burger', 10.99, 'College Station'), 'Store2': ('Sammy', 20.36, 'My address')}
    if locationType == 'gas':
        pass
    elif locationType == 'drink' or locationType == 'food':
        locationCandidates = googleMap(item, address)

        filtered_stores = distanceFunct(locationCandidates, radius, address)

        final_items = uberEats(filtered_stores.keys(), item, address)   

        print(final_items)  

#findLocations('food', 'burger', '2604 Zambia Dr, Cedar Park', 5)