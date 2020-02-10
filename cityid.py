import json

def get_city_ID(city_name):
    """
    this function take city name and find it's ID from
    city.list.jason file
    """
    
    with open('city.list.json','r') as city_file:
        city_data = json.load(city_file)
    
    city_ID = [city['id'] for city in city_data if city['name'] == city_name  ]
    return  city_ID[0] if city_ID else 'None'
    
print(find_city_ID('Huzuf'))
