# Load local settings
import settings

import pywapi
import re
import simplejson
import sys

def main():
	# Grab the current weather from Google
	weather = pywapi.get_weather_from_google(settings.LOCATION)
	
	weather_dict = {}
	
	for key in settings.DATA:
		value = eval('weather' + settings.DATA[key][0])
		
		# Run the regex if a value was provided
		if len(settings.DATA[key]) == 2:
			matches = re.search(settings.DATA[key][1], value)
			
			if matches != None:
				value = matches.group(0)
		
		# Assign the returned value to the new dictionary key
		weather_dict[key] = value
	
	return simplejson.dumps(weather_dict)

if __name__ == '__main__':
	sys.stdout.write(main())