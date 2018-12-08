from weather import Weather, Unit
import argparse


def data(x):
    weather = Weather(unit=Unit.FAHRENHEIT)
    lookup = weather.lookup_by_location(f'{x}')
    condition = lookup.forecast

    print('\n[+] The 7-Day Weather forecast for Columbus [+]\n\n')
    for forecast in condition:
        # define forecast variables
        wDate = forecast.date
        wDay = forecast.day
        wHigh = forecast.high
        wLow = forecast.low
        wText = forecast.text
        print(f'[+] The weather for {wDay}, {wDate} is: ')
        print(f'\t[- High of: \t{wHigh}')
        print(f'\t[-- Low of: \t{wLow}')
        print(f'\t[--- Condition: {wText}')
        print("\n")


# 3. main argument function
def main():
    # 3.1. Argparse help menu: display help menu
    parser = argparse.ArgumentParser(description='Python tool used to request and display real-time weather data')
    # 3.2. define flags
    parser.add_argument('-c', '--city', help='Enter your city to return weather data', required=True)
    # 3.3. save input
    args = parser.parse_args()
    # 3.4. perform minimal user validation then pass input to data function
    data(str(args.city).lower())


main()



