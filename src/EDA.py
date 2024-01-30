import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import streamlit as st

from src.timestamp import categorize_shift


def EDA(df):
    df["actual_delivery_time"] = pd.to_datetime(df["actual_delivery_time"])
    df["created_at"] = pd.to_datetime(df["created_at"])
    total_days = (df["created_at"].max() - df["created_at"].min()).days + 1

    df["delivery_time"] = (
        df["actual_delivery_time"] - df["created_at"]
    ).dt.total_seconds() / 60

    # creating min,hour,day from created_at
    df["min"] = (df["created_at"].dt.minute) + 1
    df["hour"] = (df["created_at"].dt.hour) + 1
    df["day"] = (df["created_at"].dt.dayofweek) + 1
    df["shift"] = df["created_at"].apply(categorize_shift)

    # min basis graph
    minute_count = df["min"].value_counts().sort_index()
    st.title("Minute Count")
    st.line_chart(minute_count)

    # hour basis graph
    hourly_count = df["hour"].value_counts().sort_index()
    st.title("Hourly Count")
    st.line_chart(hourly_count)

    # daily basis graph
    daily_count = df["day"].value_counts().sort_index()
    st.title("Daily Count")
    st.line_chart(daily_count)
