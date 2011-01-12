import settings

import pywapi
import re
import sys

def main():
	weather = pywapi.get_weather_from_google(settings.LOCATION)
	
	weather_dict = {}
	
	for key in settings.DATA:
		value = eval('weather' + settings.DATA[key][0])
		
		if len(settings.DATA[key]) == 2:
			matches = re.search(settings.DATA[key][1], value)
			
			if matches != None:
				value = matches.group(0)
		
		weather_dict[key] = value
	
	print weather_dict

if __name__ == '__main__':
	sys.exit(main())