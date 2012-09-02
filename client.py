# Load local settings
import settings

import pywapi
import re
import simplejson
import sys

def main():
	# Grab the current weather from Google
	weather = pywapi.get_weather_from_yahoo(settings.LOCATION, settings.UNITS)
	
	weather_dict = {}
	
	for key in settings.DATA:
		value = eval('weather' + settings.DATA[key]['key'])
		
		# Run the regex if a value was provided
		if 'regex' in settings.DATA[key]:
			matches = re.search(settings.DATA[key]['regex'], value)
			
			if matches != None:
				value = matches.group(0)
		
		if 'format' in settings.DATA[key]:
			value = settings.DATA[key]['format'] % value
		
		# Assign the returned value to the new dictionary key
		weather_dict[key] = value
	
	return simplejson.dumps(weather_dict)

if __name__ == '__main__':
	sys.stdout.write(main())