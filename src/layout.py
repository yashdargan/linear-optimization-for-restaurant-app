from pathlib import Path

import streamlit as st
from streamlit_option_menu import option_menu

from src.data_processing import preprocessing
from src.EDA import EDA
from src.location import optimize_restaurant, visualization_map
from src.optimization import find_nearest_restaurant


def layout(df):
    selected = option_menu(
        menu_title="Job Shop",
        options=["Home", "Data view", "EDA", "Result"],
        icons=["house", "database-fill", "graph-up", "journal"],
        menu_icon="cast",
        default_index=0,
        orientation="horizontal",
    )

    if selected == "Home":
        file = Path("README.md").read_text()
        st.markdown(file, unsafe_allow_html=True)

    if selected == "Data view":
        st.title("Delivery data")
        st.write(df)

    if selected == "EDA":
        EDA(df)

    if selected == "Result":
        unique = df['Restaurant_Name']
        st.sidebar.title("Select Restaurant")
        restaurant = st.sidebar.selectbox(
            "Choose the Category:",
            unique,
        )

        df = visualization_map(df, restaurant)
        #if st.sidebar.button("Optimize Route"):
            #nearest_restaurant = find_nearest_restaurant(df, loc1, loc2)
            #st.write(nearest_restaurant["Restaurant_Name"])
            #optimize_restaurant(nearest_restaurant, loc1, loc2)
