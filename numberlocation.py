import phonenumbers
import folium
from mynumber import  number
from phonenumbers import geocoder
key ="58f9b0853fde4c0ead34a92f54f527ff"
samNumber = phonenumbers.parse(number)
yourLocation = geocoder.description_for_number(samNumber, "en")
print(yourLocation)

##get phone number provider
from phonenumbers import carrier
service_provider =phonenumbers.parse(number)
print(carrier.name_for_number(service_provider, "en"))

from opencage.geocoder import OpenCageGeocode
geocoder =OpenCageGeocode(key)

query = str(yourLocation)
results =geocoder.geocode(query)
# print(results)
lat =results[0]['geometry']['lat']

lng=results[0]['geometry']['lng']

print(lat,lng)

myMap =folium.Map(Location=[lat, lng], zoom_start= 9)
folium.Marker([lat, lng],popup=yourLocation).add_to((myMap))
## save my map in html
myMap.save("myLocation.html")
