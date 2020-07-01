import requests

place_list = [(34.155834, -119.202789, 'Port Hueneme'),(-33.924870, 18.424055, 'Cape Town'),(4.710989,-74.072090, 'Bogotá'),(6.248220, -75.580032, 'Medellín'),(6.524379, 3.379206, 'Lagos'),(30.044420, 31.235712, 'Cairo'),(41.0082, 28.9784, 'Istanbul'),(18.5944, 72.3074, 'Port Au Prince'),(39.9042, 116.4074, 'Beijing'),(29.9511, 90.0715, 'New Orleans'), (33.7490, 84.3880 'Atlanta'),]

# Next 
# If you want to use classes

class Place:
  def __init__(self, lat, long, name):
    self.lat = lat
    self.long = long
    self.name = name

  def __str__(self):
    return(f'{self.name} latitude: {self.lat} longitude: {self.long} ') 

def create_placelist(list):
  places = []
  for city in list:
    place = Place(city[0], city[1], city[2])
    places.append(place)
  return places
    

places = create_placelist(place_list)
print(places[0])

# Next 

class WeatherReport:
  def __init__(self, place, temp, precip):

   pass


# Next 


def get_weather_data(place_list):
  # get lats and longs from tuples
  # give me temp and precip for a location, given lat and long
  # it will make a request to the 'realtime' url that we used below
  pass


def get_weather_data(lat, long):
  
  url = "https://api.climacell.co/v3/weather/realtime"
  payload = {
    # NEED KEY
  "apikey": '  ',"lat":lat, 
  "lon":long,
  "fields": ["temp", "precipitation", "wind_gust"],
  "unit_system":"us", 

   }

  response = requests.get(url, params=payload).json()

  print(response)
  get_weather_data(places.lat, places.long)