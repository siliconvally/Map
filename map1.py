import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

def color_map(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'

map = folium.Map(location=[40.690443, -74.044353], zoom_start=7, titles="Mapbox Bright")

fgv = folium.FeatureGroup(name="Volcanoes")

for lt, ln, el in zip(lat, lon, elev):
    fgv.add_child(folium.CircleMarker(location=[lt, ln], radius = 6, popup=str(el)+" meter",
    fill_color=color_map(el), color = 'grey', fill_opacity=0.7))
fgp = folium.FeatureGroup(name="Population")
fgp.add_child(folium.GeoJson(data=open('map.json', 'r', encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':"yellow" if x['properties']['POP2005'] < 10000000
else 'purple' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))
map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save("Map1.html")
