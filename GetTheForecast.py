# 1. Imports
import pyowm
import argparse

# 2. API key from https://home.openweathermap.org/
owm = pyowm.OWM('[Insert API Key]')  # You MUST provide a valid API key

# 3. api call, data, parsing, and print function
def data(x):
    # Search for current weather provided by user input
    fc = owm.three_hours_forecast(f'{x}')

    # omw API forecast call for location
    f = fc.get_forecast()

    # iterate through returned data
    for date in f:
        # pull noon data for next 5 days
        if "12:00:00" in str(date.get_reference_time('iso')):
            d1 = str(date.get_reference_time('iso')).split('+')[0]  # date time of forecast
            d2 = date.get_detailed_status()                         # detailed status
            d3 = date.get_temperature('fahrenheit')                 # temp. dict.
            d31 = d3.get('temp')                                    # temp
            d4 = date.get_wind()                                    # wind dict.
            d41 = d4.get('speed')                                   # wind speed
            d5 = date.get_humidity()                                # humidity
            d6 = date.get_weather_icon_url()                        # weather icon url

            print(f'Date Time: {d1}')
            print(f'Condition: {d2}')
            print(f'Temperature: {d31} F')
            print(f'Wind Speed: {d41} mph')
            print(f'Humidity: {d5}%')
            print(f'\n')


# 4. main argument function
def main():
    # 3.1. Argparse help menu: display help menu
    parser = argparse.ArgumentParser(description='Python tool used to request and display real-time weather data')
    # 3.2. define flags
    parser.add_argument('-c', '--city', help='Enter city,country   Ex: --city Austin,US', required=True)
    # 3.3. save input
    args = parser.parse_args()
    # 3.4. perform minimal user validation then pass input to data function
    data(str(args.city).lower())


main()