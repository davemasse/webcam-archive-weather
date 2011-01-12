# ZIP code
LOCATION = '00000'
# Data map - A dictionary of keys from the webcam archive plugin admin
# with corresponding values pulled from the Google weather values for
# the location above. The value of each dictionary element is a list
# containing the element name along with an optional regular expression,
# of which the first matching group will be used.
DATA = {
	'temp': ['["current_conditions"]["temp_f"]'],
	'weather': ['["current_conditions"]["condition"]'],
	'wind-direction': ['["current_conditions"]["wind_condition"]', r'(?<=: )([A-Z]+)'],
	'wind-speed': ['["current_conditions"]["wind_condition"]', r'(\d+ mph)$']
}