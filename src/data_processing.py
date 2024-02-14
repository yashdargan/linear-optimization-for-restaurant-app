import pandas as pd
import streamlit as st

from src.data_loading import load_file
from src.optimization import haversine
from src.timestamp import map_to_broader_category


def preprocessing():
    file_path = "Data/DelhiNCR Restaurants.csv"
    df = load_file(file_path)

    df.drop(
        columns=[
            "Dining_Rating",
            "Dining_Review_Count",
            "Dining_Review_Count",
            "Delivery_Rating_Count",
            "Known_For2",
            "Known_For22",
        ],
        inplace=True,
    )

    file_path = "Data/dataset.csv"
    df1 = load_file(file_path)
    rf1 = df1[df1["total_outstanding_orders"] > df1["total_onshift_partners"]]
    df.reset_index(inplace=True)
    rf1.reset_index(inplace=True)

    # Merge df2 with df1 based on their indices
    merged_df = pd.merge(
        df, rf1, left_index=True, right_index=True, suffixes=("_df", "_rf1")
    )

    # Filter the rows based on the distance criteria
    filtered_rows = []
    for index1, row1 in merged_df.iterrows():
        include_row = True
        for index2, row2 in merged_df.iterrows():
            if index1 != index2:
                # Calculate the distance between the two restaurants
                distance = haversine(
                    row1["Longitude"],
                    row1["Latitude"],
                    row2["Longitude"],
                    row2["Latitude"],
                )
                if distance < 1:
                    include_row = False
                    break
        if include_row:
            filtered_rows.append(row1)

    # Create a new DataFrame containing only the filtered rows
    filtered_df = pd.DataFrame(filtered_rows)

    filtered_df["Broad_Category"] = filtered_df["Category"].apply(
        map_to_broader_category
    )

    return filtered_df
