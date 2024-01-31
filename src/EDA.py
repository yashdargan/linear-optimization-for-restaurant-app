import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import streamlit as st

from src.timestamp import categorize_shift


def user_input_feature():
    st.sidebar.title("Line Graph")
    x_axis = st.sidebar.selectbox("X-axis", ("Minute", "Hour", "Day", "Shift"))
    return x_axis


def EDA(df):
    df["actual_delivery_time"] = pd.to_datetime(df["actual_delivery_time"])
    df["created_at"] = pd.to_datetime(df["created_at"])
    total_days = (df["created_at"].max() - df["created_at"].min()).days + 1

    df["delivery_time"] = (
        df["actual_delivery_time"] - df["created_at"]
    ).dt.total_seconds() / 60

    # title
    st.title("Exploratory Data Analysis")
    # sidebar
    feature = user_input_feature()

    # creating min,hour,day from created_at
    df[feature] = (
        (df["created_at"].dt.minute) + 1
        if feature == "Minute"
        else (
            (df["created_at"].dt.hour) + 1
            if feature == "Hour"
            else (
                (df["created_at"].dt.dayofweek) + 1
                if feature == "Day"
                else (
                    (df["created_at"].apply(categorize_shift))
                    if feature == "Shift"
                    else None
                )
            )
        )
    )
    # graphs
    graph_count = df[feature].value_counts().sort_index()
    st.write(f"## {feature} Graph")
    st.line_chart(graph_count)
