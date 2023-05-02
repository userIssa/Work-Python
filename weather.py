import requests

api_key = '8d71d1f706df2bf32edebe9bcbee7faf'
city = input('Enter city name: ')

url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
response = requests.get(url)

if response.status_code == 200:
    weather_data = response.json()
    print(f"Temperature: {weather_data['main']['temp']}°K")
    print(f"Description: {weather_data['weather'][0]['description']}")
else:
    print('Error fetching weather data')
