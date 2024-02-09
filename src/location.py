import folium
import numpy as np
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


def visualization_map(filtered_df, location, cat):
    st.title("Nearby Restaurants in Delhi NCR")
    mean_latitude = filtered_df["Latitude"].mean()
    mean_longitude = filtered_df["Longitude"].mean()

    location_customer = {
        "Mean": [mean_latitude, mean_longitude],
        "Random": [
            mean_latitude + np.random.uniform(-0.1, 0.1),
            mean_longitude + np.random.uniform(-0.1, 0.1),
        ],
        "Outer": [
            np.random.uniform(28.5, 28.51),
            np.random.uniform(76.5, 76.51),
        ],
    }

    # Create a Folium map centered around the mean latitude and longitude
    m = folium.Map(location=[mean_latitude, mean_longitude], zoom_start=15)

    # Add markers for each restaurant location
    colors = {
        "North Indian": "blue",
        "South Indian": "orange",
        "Beverages": "pink",
        "Chinese": "green",
    }

    # Filter DataFrame based on selected category
    if cat != "All":
        filtered_df = filtered_df[filtered_df["Broad_Category"] == cat]

    # Mark restaurants on the map with colors based on broader categories
    for index, row in filtered_df.iterrows():
        broader_category = row["Broad_Category"]
        color = colors.get(
            broader_category, "gray"
        )  # Default to gray if category not found in colors
        folium.Marker(
            location=[row["Latitude"], row["Longitude"]],
            popup=row["Restaurant_Name"],
            icon=folium.Icon(color=color),
        ).add_to(m)

    # Mark the selected location with a red marker
    latitude, longitude = location_customer.get(location, [None, None])

    if latitude is not None and longitude is not None:
        folium.Marker(
            location=[latitude, longitude],
            popup="Mean Location",
            icon=folium.Icon(color="red"),
        ).add_to(m)

    # Fit the map bounds to the markers
    bounds = [
        [filtered_df["Latitude"].min(), filtered_df["Longitude"].min()],
        [filtered_df["Latitude"].max(), filtered_df["Longitude"].max()],
    ]
    m.fit_bounds(bounds)

    filtered_df["Longitude"] = filtered_df["Longitude"].astype(float)
    filtered_df["Latitude"] = filtered_df["Latitude"].astype(float)

    # Display the map
    folium_static(m)

    return filtered_df, latitude, longitude


def optimize_restaurant(filtered_df, latitude, longitude):
    mean_lati = filtered_df["Latitude"].mean()
    mean_long = filtered_df["Longitude"].mean()
    m = folium.Map(location=[mean_lati, mean_long], zoom_start=15)
    folium.Marker(
        location=[mean_lati, mean_long],
        popup="restrurant",
        icon=folium.Icon(color="purple"),
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
