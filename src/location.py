import folium
import requests
import streamlit as st
from streamlit_folium import folium_static


# Function to fetch nearby restaurants using the OpenStreetMap API
def fetch_nearby_restaurants(latitude, longitude):
    # OpenStreetMap API endpoint for nearby places
    endpoint = "https://nominatim.openstreetmap.org/reverse"
    # Parameters for the API request
    params = {
        "format": "json",
        "lat": latitude,
        "lon": longitude,
        "zoom": 18,
        "addressdetails": 1,
    }
    # Send a GET request to the API endpoint
    response = requests.get(endpoint, params=params)
    # Parse the JSON response
    data = response.json()
    return data


# Function to visualize nearby restaurants on a Folium map
def visualization_map(df):
    st.title("Nearby Restaurants in Delhi NCR")
    latitude = 28.7041  # Latitude of Delhi NCR
    longitude = 77.1025  # Longitude of Delhi NCR
    # Fetch nearby restaurants using the OpenStreetMap API
    data = fetch_nearby_restaurants(latitude, longitude)
    # Visualize nearby restaurants on a Folium map

    # Create a Folium map centered around the specified latitude and longitude
    m = folium.Map(location=[data["lat"], data["lon"]], zoom_start=15)
    # Add a marker for the location
    folium.Marker(
        location=[data["lat"], data["lon"]], popup=data["display_name"]
    ).add_to(m)
    # Display the map
    folium_static(m)
