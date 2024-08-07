import folium
import requests

re = requests.get('https://ipinfo.io')
# print(re.status_code)
data = re.json()

location =data['loc'].split(',')
# print(location)
lat = float(location[0])
log = float(location[1])
print(log)
print(lat)

fg=folium.FeatureGroup("my map")


fg.add_child(folium.Marker(
    location = [lat, log],
    popup = "Arslan Arshad",
    tooltip = 'Click Me',
    icon = folium.Icon(color="green",icon='home')
    ))


map=folium.Map(location=[lat,log],zoom_start=5)
map.add_child(fg)
map.save("test1.html")