import folium
import numpy as np
import pandas as pd
import requests
import streamlit as st
from streamlit_folium import folium_static


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

def visualization_map(filtered_df, restaurant):
    st.title("Nearby Restaurants in Delhi NCR")
    
    # Mean latitude and longitude of restaurants
    mean_latitude_restaurant = filtered_df["Latitude"].mean()
    mean_longitude_restaurant = filtered_df["Longitude"].mean()
    
    # Create a Folium map centered around the mean latitude and longitude of restaurants
    m = folium.Map(location=[mean_latitude_restaurant, mean_longitude_restaurant], zoom_start=15)

    if restaurant is not None:
        filtered_df = filtered_df[filtered_df["Restaurant_Name"] == restaurant]

    # Mark restaurants on the map with red 
    for _, row in filtered_df.iterrows():
        folium.Marker(
            location=[row["Latitude"], row["Longitude"]],
            popup=row["Restaurant_Name"],
            icon=folium.Icon(color='red'),
        ).add_to(m)
    
    # Generate customer locations near the restaurant
    customer_data = pd.DataFrame(columns=['C_Longitude', 'C_Latitude'])

    for _, row in filtered_df.iterrows():
        customer_rows = []
        for i in range(int(row['total_outstanding_orders'])):  # Generate multiple locations for each order
            longitude = row["Longitude"] + np.random.uniform(-0.010, 0.010)
            latitude = row["Latitude"] + np.random.uniform(-0.010, 0.010)
            customer_rows.append({'C_Longitude': longitude, 'C_Latitude': latitude})
        customer_data = pd.concat([customer_data, pd.DataFrame(customer_rows)], ignore_index=True)

    # Mark customer locations on the map with purple
    for _, row in customer_data.iterrows():
        folium.Marker(
            location=[row["C_Latitude"], row["C_Longitude"]],
            popup="customer",
            icon=folium.Icon(color='purple'),
        ).add_to(m)

    # Fit the map bounds to the markers
    bounds = [
        [min(filtered_df["Latitude"].min(), customer_data["C_Latitude"].min()),
        min(filtered_df["Longitude"].min(), customer_data["C_Longitude"].min())],
        [max(filtered_df["Latitude"].max(), customer_data["C_Latitude"].max()),
        max(filtered_df["Longitude"].max(), customer_data["C_Longitude"].max())],
    ]
    m.fit_bounds(bounds)

    # Display the map
    folium_static(m)
    
    st.write("Outstanding_delivery",filtered_df[['total_outstanding_orders','total_onshift_partners']])

    return filtered_df


def optimize_restaurant(filtered_df, latitude, longitude):
    mean_lati = filtered_df["Latitude"].mean()
    mean_long = filtered_df["Longitude"].mean()
    m = folium.Map(location=[mean_lati, mean_long], zoom_start=15)
    folium.Marker(
        location=[mean_lati, mean_long],
        popup="restrurant",
        icon=folium.Icon(color="green"),
    ).add_to(m)

    folium.Marker(
        location=[latitude, longitude],
        popup="customer",
        icon=folium.Icon(color="Red"),
    ).add_to(m)
    bounds = [
        [
            filtered_df["Latitude"].min(),
        ],
        [filtered_df["Latitude"].max()],
    ]
    m.fit_bounds(bounds)
    folium_static(m)
