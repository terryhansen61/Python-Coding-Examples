# This demo will ask for a location and then rendor the map for that location
# in your browser.  You can then zoom in, out, etc.
# It saves the map as an HTML file in your PyCharm project folder
import folium
from geopy.geocoders import Nominatim
import webbrowser
import os

location_name = input('Enter location: ')
geolocator = Nominatim(user_agent="geoapi")
location = geolocator.geocode(location_name)

if location:
    lat = location.latitude
    lon = location.longitude

    # Create the map
    my_map = folium.Map(location=[lat, lon], zoom_start=12)

    # Add a marker
    folium.Marker(
        location=[lat, lon],
        popup=location_name
    ).add_to(my_map)

    # Save the map to HTML
    file_path = os.path.abspath("map.html")
    my_map.save(file_path)

    print(f"Map saved to: {file_path}")
    print("Opening map in your browser...")

    # Open the map in your browser automatically
    webbrowser.open(f"file://{file_path}")
else:
    print("Location not found. Please try again.")



