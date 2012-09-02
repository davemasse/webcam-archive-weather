# ZIP code
LOCATION = '00000'
# Data map - A dictionary of keys from the webcam archive plugin admin
# with corresponding values pulled from the Google weather values for
# the location above. The value of each dictionary element is a list
# containing the element name along with an optional regular expression,
# of which the first matching group will be used.
DATA = {
  'temp': {
    'key': '["condition"]["temp"]',
  },
  'weather': {
    'key': '["condition"]["text"]',
  },
  'wind-direction': {
    'key': '["wind"]["direction"]',
    'format': '%s&deg;',
  },
  'wind-speed': {
    'key': '["wind"]["speed"]',
    'format': '%s mph',
  },
}
# Units for measurements, if allowed by API ("metric" or empty string)
UNITS = ''