import requests, cityid

API_KEY = 'f9f5bd14bbc6b24dc1620b7c1d58b826'
API_URL = 'http://api.openweathermap.org/data/2.5/weather'

def get_data(city_name,unitformat='metric',language='en'):
    city_id = cityid.get_city_ID(city_name)
    payload = {'id':city_id,'units':unitformat,'lang':language,"APPID":API_KEY}
    weather = requests.get(API_URL,params=payload)
    return weather.json()

