# Imports
import pyowm
import argparse

# API key from https://home.openweathermap.org/
owm = pyowm.OWM('f3900e22393501d865da1c81b1b2addc')  # You MUST provide a valid API key


def data(x):
    # Search for current weather in London (Great Britain)
    observation = owm.weather_at_place(f'{x}')

    # return location data
    loc = observation.get_location()
    loc1 = loc.get_name()
    loc2 = loc.get_lon()
    loc3 = loc.get_lat()
    loc4 = loc.get_ID()

    # assign variables to returned weather data
    w = observation.get_weather()
    w1 = str(w.get_reference_time('date')).split('+')[0]    # update time
    w2 = str(w.get_clouds())                # cloud coverage
    w3 = str(w.get_rain())                  # rain volume
    w4 = str(w.get_snow())                  # snow volume
    w5 = w.get_wind()                       # wind dict.
    w51 = w5.get('speed')                   # current wind speed
    w52 = w5.get('deg')                     # current wind angle
    w6 = w.get_humidity()                   # humidity
    w7 = w.get_pressure()                   # pressure dict.
    w71 = w7.get('press')                   # atmospheric pressure
    w72 = w7.get('sea_level')               # sea level air pressure
    w8 = w.get_temperature('fahrenheit')    # temp. dict.
    w81 = w8.get('temp')                    # current temp
    w82 = w8.get('temp_max')                # daily max temp
    w83 = w8.get('temp_min')                # daily min temp
    w9 = w.get_status()                     # short status
    w10 = w.get_detailed_status()           # detailed status
    w11 = w.get_weather_code()              # weather code
    w12 = w.get_weather_icon_name()         # weather icon name
    w13 = w.get_weather_icon_url()          # weather icon url
    w14 = str(w.get_sunrise_time('date')).split('+')[0]     # sunrise time
    w15 = str(w.get_sunset_time('date')).split('+')[0]      # sunset time

    print(f'Date: {w1}')
    print(f'Description: {w10}')
    print(f'Location: {loc1}')
    print(f'Temperature: {w81}')
    print(f'Humidity: {w6}')
    print(f'Pressure: {w71}')
    print(f'Sunrise: {w14}')
    print(f'Sunset: {w15}')
    print(f'Wind Direction: {w52}')
    print(f'Wind Speed: {w51}')
    print(f'Temp. High: {w14}')
    print(f'Temp. Low: {w15}')
    print(f'Cloud coverage: {w2}%')
    if w3 != "{}":
        print(f'Rain volume: {w3}')
    if w3 != "{}":
        print(f'Snow volume: {w3}')


# 3. main argument function
def main():
    # 3.1. Argparse help menu: display help menu
    parser = argparse.ArgumentParser(description='Python tool used to request and display real-time weather data')
    # 3.2. define flags
    parser.add_argument('-c', '--city', help='Enter city,country   Ex: Austin,US', required=True)
    # 3.3. save input
    args = parser.parse_args()
    # 3.4. perform minimal user validation then pass input to data function
    data(str(args.city).lower())


main()

