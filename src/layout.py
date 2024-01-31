from pathlib import Path

import streamlit as st
from streamlit_option_menu import option_menu

from src.EDA import EDA


def layout(df):
    selected = option_menu(
        menu_title="Job Shop",
        options=["Home", "Data view", "EDA"],
        icons=["house", "database-fill", "graph-up"],
        menu_icon="cast",
        default_index=0,
        orientation="horizontal",
    )

    if selected == "Home":
        file = Path("README.md").read_text()
        st.markdown(file, unsafe_allow_html=True)

    if selected == "Data view":
        st.title("Portal delivery data")
        st.write(df)

    if selected == "EDA":
        EDA(df)
