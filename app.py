pip install streamlit
import pandas as pd
import geopandas as gpd
from shapely.geometry import Point
import folium
import streamlit as st 

data = pd.DataFrame({
    'longitude': [71.408928, 71.409000],
    'latitude': [51.187323, 51.188000],
    'name': ['Местоположение 1', 'Местоположение 2'],
    'type': ['Тип 1', 'Тип 2']
})

geometry = [Point(lon, lat) for lon, lat in zip(data['longitude'], data['latitude'])]
gdf = gpd.GeoDataFrame(data, geometry=geometry)
gdf.crs = "EPSG:4326"

def create_map():
    m = folium.Map(location=[51.187323, 71.408928], zoom_start=15)
    
    google_maps_url = "https://{s}.google.com/vt/lyrs=m&x={x}&y={y}&z={z}"

    folium.TileLayer(
        tiles=google_maps_url,
        attr="Google Maps",
        name="Google Maps",
    ).add_to(m)

    for _, row in gdf.iterrows():
        folium.Marker(
            location=[row['latitude'], row['longitude']],
            popup=f"<b>{row['name']}</b><br>Тип: {row['type']}",
            icon=folium.Icon(color="red")
        ).add_to(m)
    
    return m


st.title('Интерактивная карта') 
map_ = create_map()

st.write(map_) 
