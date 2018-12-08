from weather import Weather, Unit
import argparse


def data(x):
    weather = Weather(unit=Unit.FAHRENHEIT)
    lookup = weather.lookup_by_location(f'{x}')

    # condition stats
    conDate = lookup.condition.date
    conDesc = lookup.condition.text
    conTemp = lookup.condition.temp
    conCode = lookup.condition.code
    # atmosphere stats
    atmHum = lookup.atmosphere.humidity
    atmVis = lookup.atmosphere.visibility
    atmPre = lookup.atmosphere.pressure
    atmRis = lookup.atmosphere.rising
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

    print(f'Date: {conDate}')
    print(f'Description: {conDesc}')
    print(f'Temperature: {conTemp}')
    print(f'Humidity: {atmHum}')
    print(f'Visibility: {atmVis}')
    print(f'Pressure: {atmPre}')
    print(f'Rising: {atmRis}')
    print(f'Sunrise: {astRise}')
    print(f'Sunset: {astSet}')
    print(f'Wind-chill: {winChill}')
    print(f'Wind Direction: {winDirection}')
    print(f'Wind Speed: {winSpeed}')
    print(f'Day Temperature High: {forStats[0]}')
    print(f'Day Temperature Low: {forStats[1]}')
    print(f'Day of The Week: {forStats[2]}')


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
