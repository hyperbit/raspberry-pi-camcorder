# =====================================================================================
# weather.py
# =====================================================================================
# This module fetches sunrise and sunset times from either Yahoo!(primary) or 
# Weather.com(secondary)
# This module assumes the following files are in the local director:
#	SUNRISE.txt
#	SUNSET.txt
# =====================================================================================
import pywapi

ZIP = "92507"

SUNRISE_FILE = '/home/pi/scripts/SUNRISE.txt'
SUNSET_FILE = '/home/pi/scripts/SUNSET.txt'

def parseTimestamp(timestamp):
        tokens = timestamp.split()
        n = tokens[0].split(':')
        hour = int(n[0])
        minute = int(n[1])
        if tokens[1] == 'pm':
                hour += 12
        if hour == 24:
                hour = 0
        print hour, minute

''' Get weather from different weather stations '''
yahoo_weather = pywapi.get_weather_from_yahoo(ZIP)
weather_com_weather = pywapi.get_weather_from_weather_com(ZIP)

if 'astronomy' in yahoo_weather:
	print "Connected to YAHOO! weather server!"
	if 'sunrise' in yahoo_weather['astronomy']:
		sunrise = open(SUNRISE_FILE, 'w+')
		SUNRISE = str(yahoo_weather['astronomy']['sunrise'])
		sunrise.write(SUNRISE)
		sunrise.close()
	if 'sunset' in yahoo_weather['astronomy']:
		sunset = open(SUNSET_FILE, 'w+')
		SUNSET = str(yahoo_weather['astronomy']['sunset'])
		sunset.write(SUNSET)
		sunset.close()

elif 'forecasts' in weather_com_weather:
	print "Connected to Weather.com weather server!"
	sunrise = open(SUNRISE_FILE, 'w+')
        SUNRISE = str(weather_com_weather['forecasts'][0]['sunrise'])
	sunrise.write(SUNRISE)
	sunset = open(SUNSET_FILE, 'w+')
        SUNSET = str(weather_com_weather['forecasts'][0]['sunset'])
	sunset.write(SUNSET)

else:
	print "Cannot connect to weather server!"
	print "Loading contents from:"
	print SUNRISE_FILE
	print SUNSET_FILE
	sunrise = open(SUNRISE_FILE)
	sunset = open(SUNSET_FILE)
	SUNRISE = sunrise.read()
	SUNSET = sunset.read()
	sunrise.close()
	sunset.close()

print "Sunrise at:", SUNRISE
print "Sunset at:", SUNSET
