from http.client import responses

import requests

url = 'https://api.openweathermap.org/data/2.5/weather'
params = {'q': 'Лондон', 'appid': 'a225f00ca2bc19c48c68bae004d231ba', 'units': 'metric', 'lang': 'ru'}
city = input('Выберите город: ')
params['q'] = city
response = requests.get(url, params=params).json()
print(f'Город: {city} Погода: {response ['weather'][0]['description']}\n'
      f' Температура: + {response['main']['temp']}C, по ощущениям +{response['main']['feels_like']}C')
