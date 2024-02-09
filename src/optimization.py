import math

import numpy as np


def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees)
    """
    # Convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(math.radians, [lon1, lat1, lon2, lat2])

    # Haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = (
        math.sin(dlat / 2) ** 2
        + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
    )
    c = 2 * math.asin(math.sqrt(a))
    r = 6371  # Radius of earth in kilometers. Use 3956 for miles
    return c * r


def find_nearest_restaurant(filtered_df, customer_lati, customer_long):
    try:

        # Calculate distances between customer location and all restaurants
        distances = []
        for idx, row in filtered_df.iterrows():
            distance = haversine(
                row["Longitude"],
                row["Latitude"],
                customer_long,
                customer_lati,
            )
            distances.append(distance)

        # Find the index of the nearest restaurant
        nearest_idx = np.argmin(distances)

        return filtered_df.iloc[nearest_idx]
    except ValueError:
        # Handle the case where customer_location contains non-numeric values
        print(
            "Invalid customer location: Longitude and Latitude must be numeric values."
        )
        return None
