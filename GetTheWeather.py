# 1. imports
from weather import Weather, Unit
import argparse

# 2. main data function
def data(x):
    weather = Weather(unit=Unit.FAHRENHEIT)
    lookup = weather.lookup_by_location(f'{x}')

    # condition stats
    conDate = lookup.condition.date
    conDesc = lookup.condition.text
    conTemp = lookup.condition.temp
    # atmosphere stats
    atmHum = lookup.atmosphere.humidity
    atmVis = lookup.atmosphere.visibility
    # astronomy stats
    astRise = lookup.astronomy.sunrise
    astSet = lookup.astronomy.sunset
    # wind stats
    winChill = lookup.wind.chill
    winDirection = lookup.wind.direction
    winSpeed = lookup.wind.speed
    # forecast stats
    forData = lookup.forecast
    forStats = []
    for i in forData:
        high = i.high
        low = i.low
        day = i.day
        forStats.append(high)
        forStats.append(low)
        forStats.append(day)

    print(f'[+] Weather for {conDate} - - - - - - - - - - - [+]')
    print(f'\t[-] Temp')
    print(f'\t\t- Current:\t\t{conTemp} degress and {conDesc}')
    print(f'\t\t- Feels like:\t\t{winChill} degrees with wind chill')
    print(f'\t\t- Humidity:\t\t{atmHum}%')
    print(f'\t\t- High:\t\t\t{forStats[0]} degrees')
    print(f'\t\t- Low:\t\t\t{forStats[1]} degrees')
    print(f'\t[-] Wind')
    print(f'\t\t- Speed:\t\t{winSpeed} mph')
    print(f'\t\t- Wind Chill:\t\t{winChill} degrees')
    print(f'\t[-] Daylight')
    print(f'\t\t- Sunrise:\t\t{astRise}')
    print(f'\t\t- Sunrise:\t\t{astSet}')
    print(f'[+] - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - [+]')


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

