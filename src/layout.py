from pathlib import Path

import streamlit as st
from streamlit_option_menu import option_menu

from src.data_processing import order_preprocessing
from src.EDA import EDA
from src.location import selected_map, visualization_map
from src.optimization import optimization


def layout(df):
    unique = df["Restaurant_Name"].unique()
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
        st.title("Nearby Restaurants in Delhi NCR")
        st.write("Outstanding_delivery")
        st.sidebar.title("Select Restaurant")
        restaurant = st.sidebar.selectbox(
            "Choose the Category:",
            unique,
        )

        df, cust = visualization_map(df, restaurant)
        order_df = order_preprocessing(df, cust)
        if st.sidebar.button("Optimize Route"):
            selected_order = optimization(df, order_df)
            selected_map(selected_order)
