import streamlit as st
import folium
from streamlit_folium import folium_static
from opencage.geocoder import OpenCageGeocode

# Function to geocode location using OpenCage Geocoding API
def geocode_location(api_key, location_name):
    geocoder = OpenCageGeocode(api_key)
    result = geocoder.geocode(location_name)
    if result and len(result) > 0:
        latitude = result[0]['geometry']['lat']
        longitude = result[0]['geometry']['lng']
        return latitude, longitude
    else:
        st.write(f'Error: Unable to geocode the location of {location_name}.')
        return None, None

# Function to visualize restaurant locations on a map
def visualization_map(restaurant_names):
    # OpenCage Geocoding API key
    OPENCAGE_API_KEY = '71c2f368b7bd49c39c00b146242cbe16'
    restaurant_names = ['Hong Kong Express', 'Cafe Coffee Day', 'Dominos Pizza']

    # Create a Folium map centered at the first restaurant location
    first_restaurant = restaurant_names[0]
    first_latitude, first_longitude = geocode_location(OPENCAGE_API_KEY, first_restaurant)
    
    if first_latitude is not None and first_longitude is not None:
        m = folium.Map(location=[first_latitude, first_longitude], zoom_start=12)
        

        # Add markers for each restaurant location
        for restaurant_name in restaurant_names:
            # Geocode the location of the restaurant
            latitude, longitude = geocode_location(OPENCAGE_API_KEY, restaurant_name)

            if latitude is not None and longitude is not None:
                # Add a marker for the restaurant
                folium.Marker(location=[latitude, longitude], popup=restaurant_name).add_to(m)
            else:
                st.write(f'Error: Unable to geocode the location of {restaurant_name}.')

        # Display the map
        folium_static(m)
    else:
        st.write('Error: Unable to get coordinates for the first restaurant.')

