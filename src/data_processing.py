import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

from src.data_loading import load_file


def preprocessing():
    file_path = "Data/DelhiNCR Restaurants.csv"
    df = load_file(file_path)
    if df["Delivery_Rating"].isnull().sum() > 0:
        mean_value = round(df["Delivery_Rating"].mean(), 1)
        df["Delivery_Rating"].fillna(value=mean_value, inplace=True)
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

    return df
