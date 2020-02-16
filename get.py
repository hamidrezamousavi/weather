import requests, json, time

API_KEY = 'f9f5bd14bbc6b24dc1620b7c1d58b826'


def get_city_ID(city_name):
    """
    this function take city name and find it's ID from
    city.list.jason file
    """
    
    with open('city.list.json','r') as city_file:
        city_data = json.load(city_file)
    
    city_ID = [city['id'] for city in city_data if city['name'].casefold() == city_name.casefold()  ]
    return  city_ID[0] if city_ID else 'None'




def get_current_data(city_name,unitformat='metric',language='en'):
    '''
    this function take city name , unitformat(imperial,metric)
    and data language and return dictionary useful data of current weather data  
    '''
    API_URL = 'http://api.openweathermap.org/data/2.5/weather'
    city_id = get_city_ID(city_name)
    payload = {'id':city_id,'units':unitformat,'lang':language,"APPID":API_KEY}
    weather = requests.get(API_URL,params=payload).json()
    useful_data = {
            'temperature':weather['main']['temp'] ,
            'temperature_feel':weather['main']['feels_like'] ,  
            'weather_condition':weather['weather'][0]['description'],
            'humidity':weather['main']['humidity'],
            'wind':weather['wind']['speed'],
            'clouds':(weather['clouds']['all']),
            'pressure':weather['main']['pressure'],
            'sunrise':weather['sys']['sunrise'],
            'sunset':weather['sys']['sunset'],
            'time':time.localtime(weather['dt']),
            }
   
    return useful_data


def get_forecast_data(city_name,unitformat='metric',language='en'):
    '''
    this function take city name , unitformat(imperial,metric)
    and data language and return list of tuple that first element of tuple
    is time and second element of tuple is dictionary that has weather forecast data
    for 5 days with data every 3 hours 
    '''
    API_URL = 'http://api.openweathermap.org/data/2.5/forecast'
    city_id = get_city_ID(city_name)
    payload = {'id':city_id,'units':unitformat,'lang':language,"APPID":API_KEY}
    weather = requests.get(API_URL,params=payload).json()
    
    
    useful_data = [(time.localtime(item['dt']),{'temprature':item['main']['temp'],
                                'temprature_feel':item['main']['feels_like'],  
                                'pressure':item['main']['pressure'],
                                'weather_condition':item['weather'][0]['description'],
                                'clouds':item['clouds']['all'],
                                'wind':item['wind']['speed'],
                                }
                    )
                   for item in weather['list'] ]
    
    
    
    return useful_data

