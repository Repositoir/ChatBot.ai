import requests

api_key = 'e01885723d98b23975ca5e08a4e4e2e1'

city = input('Enter city name: ')

url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data)
    # temp = data['main']['temp']
    # desc = data['weather'][0]['description']
    # print(f'Temperature: {temp - 273.15} C')
    # print(f'Description: {desc}')
else:
    print('Error fetching weather data')
