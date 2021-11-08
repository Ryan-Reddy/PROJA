# --- This is my weather importing tool, Will try to add this to the homescreen of module 3
from pprint import pprint
import requests

Location_input = 'Amsterdam'

def weatherget():
    Location_input = 'Amsterdam'

    r = requests.get('http://api.openweathermap.org/data/2.5/weather?q={}&APPID=bec405355763e158b82e587d6f63b06b'.format(Location_input))
    # pprint(r.json())
    location = r.json()['name']
    weather = r.json()['weather']
    dweather = weather[0]

    mainreturn = r.json()['main']
    temperature = round(mainreturn['temp']-273.15)
    tempmax = round(mainreturn['temp_max']-273.15)
    tempmin = round(mainreturn['temp_min']-273.15)

    weatherreport='Today in {} the weather will be {}.\nThe temperature right now is {}°C.\nThe minimum temperature will be {}°C and the max {}°C.\n'.format(location, dweather['description'],temperature,tempmin,tempmax)
    return weatherreport
weatherget()