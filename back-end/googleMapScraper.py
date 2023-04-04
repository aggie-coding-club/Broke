number_of_stores = 25

def googleMap(item : str, address: str) -> dict : 
    
    '''
    Locate search bar
    Enter address, hit enter
    Enter item, hit enter
    Check $ checkbox
    Grab top <twenty five> titles of places
    This threshold will be a variable so we can easily change it
    Don’t include the same place twice (like McDonald)
    Return a dictionary of names and address
    {“McDonald” : “801 university dr, college station, tx”}, {“Hopdoddy” : “...”}, …

    '''
    
    pass

from geopy import Nominatim
from geopy import distance


def filterAddress(address : str) -> str:
    '''
    get rid of the unit and building address in the address
    '''
    unit_result = 'unit' in address.lower()
    building_result = 'building' in address.lower()
    if unit_result:
        unit_index = address.lower().index('unit')
        space_index = address.lower().index(' ', unit_index) + 1
        city_index = address.lower().index(' ', space_index)
        return address[0: unit_index] + address[city_index:]
    elif building_result:
        building_index = address.lower().index('building')
        space_index = address.lower().index(' ', building_index) + 1
        city_index = address.lower().index(' ', space_index)
        return address[0: building_index] + address[city_index:]
    return address


def distanceFunct(list_of_stores : dict, radius : int, address : str) -> dict:

    '''
    Filter out list of restaurants within the radius specified by the user 
    Return dictionary of qualified restaurants
    '''
    filtered_stores = {}
    g = Nominatim(user_agent="Broke")
    
    _, addr = g.geocode(address)

    address = filterAddress(address)
    
    for store in list_of_stores:
        store_address = filterAddress(list_of_stores[store])
        _, dict = g.geocode(store_address)
        d = distance.distance(dict, addr).miles
        if d <= radius:
            filtered_stores.update({store : store_address})
    

    return filtered_stores
   
''' for checking purposes '''
list_of_stores = {'McDonalds' : '801 University Dr College Station, Texas', 'Home' : '801 Luther St W, Unit 1102, College Station, Texas', 'Star Cinema Grill' : '1037 University Dr, College Station, Texas'}
filtered_stores = distanceFunct(list_of_stores, 2, '125 Spence St, College Station, Texas')
for store in filtered_stores:
        print(store + " : " + filtered_stores[store])