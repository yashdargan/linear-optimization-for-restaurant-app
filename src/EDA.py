import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import streamlit as st

from src.timestamp import price_stamp


def EDA(df):
    cost_per_rest = price_stamp(df["Pricing_for_2"])
    st.title("No. of Restaurants in each price Catergory")
    st.bar_chart(cost_per_rest)
