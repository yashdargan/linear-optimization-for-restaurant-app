from pathlib import Path

import streamlit as st
from streamlit_option_menu import option_menu

from src.data_processing import preprocessing
from src.EDA import EDA
from src.location import visualization_map
from src.optimization import optimize_route


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
        st.sidebar.title("Select Location Type")
        loc = st.sidebar.selectbox(
            "Choose location type:", ["Mean", "Outer", "Random"]
        )
        df,loc=visualization_map(df, loc)
        if st.sidebar.button('Optimize Route'):
            optimized_route=optimize_route(df,loc)
            st.write("optimized route",optimize_route)
