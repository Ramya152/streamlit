from geopy.geocoders import Nominatim
import folium

#geocode the user-entered location
def geocode_location(location):
    geolocator = Nominatim(user_agent="my_app")
    location = geolocator.geocode(location)
    return location.latitude, location.longitude

def search_nearby_police_stations(location):
    latitude, longitude = geocode_location(location)

    mymap = folium.Map(location=[latitude, longitude], zoom_start=12)

    folium.Marker(location=[latitude, longitude], popup=location).add_to(mymap)

    nearby_stations = fetch_nearby_police_stations(latitude, longitude)

    for station in nearby_stations:
        folium.Marker(location=[station["latitude"], station["longitude"]], popup=station["name"]).add_to(mymap)
    map_html = mymap._repr_html_()

    return map_html

def fetch_nearby_police_stations(latitude, longitude):
    nearby_stations = [
        {"name": "Police Station 1", "address": "Address 1", "latitude": latitude + 0.01, "longitude": longitude},
        {"name": "Police Station 2", "address": "Address 2", "latitude": latitude - 0.01, "longitude": longitude},
        {"name": "Police Station 3", "address": "Address 3", "latitude": latitude, "longitude": longitude + 0.01}
    ]
    return nearby_stations