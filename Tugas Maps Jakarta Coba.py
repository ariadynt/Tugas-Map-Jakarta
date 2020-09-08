# In[1]

from IPython.display import IFrame
documentation = IFrame(src='https://ipyleaflet.readthedocs.io/en/latest', width=1000, height=600)
display(documentation)
# In[2]

# imports
import ipyleaflet
# from ipyleaflet import map

# create map
basic_map = ipyleaflet.Map(zoom=8)
# basic_map = Map(zoom4)

# display map
#basic_map
display(basic_map)


# In[61]:

import folium
from folium import plugins
import ipywidgets
import geocoder
import geopy
import numpy as np
import pandas as pd
from vega_datasets import data as vds


# using ipywidgets
# plot route with distance measure
# import geopy & geocoder
# can probably use geopy to geocode also
# if geopy.distance.distance does not work try import geopy.distance

import geopy.distance

# text widgets
route_start_widget = ipywidgets.Text(value='', placeholder='address', description='start:')
route_stop_widget = ipywidgets.Text(value='', placeholder='address', description='stop:')

# widget function
def get_distance(start_address, stop_address):
    
    # string addresses to location information
    start_location = geocoder.osm(start_address)
    stop_location = geocoder.osm(stop_address)
    
    # pull out latitude and longitude from location information
    start_latlng = [start_location.lat, start_location.lng]
    stop_latlng = [stop_location.lat, stop_location.lng]
    
    # calculate distance from start point to stop point using latitudes and longitudes
    distance = geopy.distance.distance(start_latlng, stop_latlng).miles
    print(f'distance: {distance:.2f} miles')
    
    # map
    distance_path = [(start_latlng), (stop_latlng)]
    map_distance = folium.Map(location=[-6.2293867,106.6894301], zoom_start=4)
    plugins.AntPath(distance_path).add_to(map_distance)
    display(map_distance)
    
# interaction between widgets and function    
ipywidgets.interact_manual(get_distance, start_address=route_start_widget, stop_address=route_stop_widget)
# notice animation moves in the direction from start to stop and distance prints above map


# In[11]

import googlemaps
from datetime import datetime

gmaps = googlemaps.Client (key = 'AIzaSyBQ4MrOpZVoBaTYAesnQRb7px0iI60w9Lo')

now = datetime.now ()
directions_result = gmaps.directions("-6.159959000000014 , 106.85342529999998" , "-6.261159618804859, 106.90502015000003", mode = "driving", avoid = "car", departure_time=now)

print(directions_result[0]['legs'][0]['distance']['text'])
print(directions_result[0]['legs'][0]['duration']['text'])


# In[3]
# Types Map
import ipyleaflet
import ipywidgets
from ipyleaflet import basemaps, Map

radio_button = ipywidgets.RadioButtons(options=['Positron', 'DarkMatter', 'WorldStreepMap', 'DeLorme',
                                                'WorldTopoMap', 'WorldImagery', 'NatGeoWorldMap', 'HikeBike',
                                                'HyddaFull', 'Night', 'ModisTerra', 'Mapnik', 'HOT', 'OpenTopoMap',
                                                'Toner', 'Watercolor'],
                                        value='Positron',
                                        description='map types:')
def toggle_maps(map):
    if map == 'Positron': m = Map(zoom=2, basemap=basemaps.CartoDB.Positron)
    if map == 'DarkMatter': m = Map(zoom=1, basemap=basemaps.CartoDB.DarkMatter)
    if map == 'WorldStreetMap': m = Map(center=(-6.200000, 106.816666),zoom=4, basemap=basemaps.Esri.WorldStreetMap)
    if map == 'DeLorme': m = Map(center=(-6.200000, 106.816666),zoom=5, basemap=basemaps.Esri.DeLorme)
    if map == 'WorldTopoMap': m = Map(center=(-6.200000, 106.816666),zoom=6, basemap=basemaps.Esri.WorldTopoMap)
    if map == 'WorldImagery': m = Map(center=(-6.200000, 106.816666),zoom=7, basemap=basemaps.Esri.WorldImagery)
    if map == 'NatGeoWorldMap': m = Map(center=(-6.200000, 106.816666),zoom=8, basemap=basemaps.Esri.NatGeoWorldMap)
    if map == 'HikeBike': m = Map(center=(-6.200000, 106.816666),zoom=9, basemap=basemaps.HikeBike.HikeBike)
    if map == 'HyddaFull': m = Map(center=(-6.200000, 106.816666),zoom=5, basemap=basemaps.Hydda.Full)
    if map == 'Night': m = Map(center=(-6.200000, 106.816666),zoom=4, basemap=basemaps.NASAGIBS.ViirsEarthAtNight2012)
    if map == 'ModisTerra': m = Map(center=(-6.200000, 106.816666),zoom=9, basemap=basemaps.NASAGIBS.ModisTerraTrueColorCR)
    if map == 'Mapnik': m = Map(center=(-6.200000, 106.816666),zoom=8, basemap=basemaps.OpenStreetMap.Mapnik)
    if map == 'HOT': m = Map(center=(-6.200000, 106.816666),zoom=7, basemap=basemaps.OpenStreetMap.HOT)
    if map == 'OpenTopoMap': m = Map(center=(-6.200000, 106.816666),zoom=6, basemap=basemaps.OpenTopoMap)
    if map == 'Toner': m = Map(center=(-6.200000, 106.816666),zoom=5, basemap=basemaps.Stamen.Toner)
    if map == 'Watercolor': m = Map(center=(-6.200000, 106.816666),zoom=4, basemap=basemaps.Stamen.Watercolor)
    display(m)

ipywidgets.interact(toggle_maps, map=radio_button)
# In[4]
# Marker

from ipyleaflet import Map, Marker
import geocoder

# location address
location = geocoder.osm('DKI Jakarta')

# to view location details use location.json

# latitude and longitude of location
latlng = [location.lat, location.lng]

# create map
maps_jakarta = Map(center=latlng)

# marker
marker = Marker(location=latlng, title='DKI Jakarta')
maps_jakarta.add_layer(marker)

# display_map
maps_jakarta

# In[5]
# Marker

from ipyleaflet import Map, Marker
import geocoder

# location address
location1 = geocoder.osm('DKI Jakarta') 
location2 = geocoder.osm('Jakarta Pusat')
location3 = geocoder.osm('Jakarta Timur')
location4 = geocoder.osm('Jakarta Barat')
location5 = geocoder.osm('Jakarta Selatan')

# to view location details use location.json

# latitude and longitude of location
latlng1 = [location1.lat, location1.lng]
latlng2 = [location2.lat, location2.lng]
latlng3 = [location3.lat, location3.lng]
latlng4 = [location4.lat, location4.lng]
latlng5 = [location5.lat, location5.lng]

# create map
maps_jakarta = Map(center=latlng1)

# marker
marker1 = Marker(location=latlng1, title = 'DKI Jakarta')
marker2 = Marker(location=latlng2, title = 'Jakarta Pusat')
marker3 = Marker(location=latlng3, title = 'Jakarta Timur')
marker4 = Marker(location=latlng4, title = 'Jakarta Barat')
marker5 = Marker(location=latlng5, title = 'Jakarta Selatan')
maps_jakarta.add_layer(marker1)
maps_jakarta.add_layer(marker2)
maps_jakarta.add_layer(marker3)
maps_jakarta.add_layer(marker4)
maps_jakarta.add_layer(marker5)

# display_map
maps_jakarta

# In[6]

location1.json
# In[7]
location2.json

# In[8]
location3.json
# In[9]
location4.json
# In[10]
location5.json